# RustFS
Repository for Laerning Rustfs

# RustFS Object Storage

## What is RustFS?

RustFS is an open-source object storage server written in **Rust**. It provides an **Amazon S3-compatible API**, allowing applications to store and retrieve objects such as documents, images, videos, backups, and datasets using standard S3 tools and SDKs.


<img width="1080" height="806" alt="architecture_design_852f73b2c8" src="https://github.com/user-attachments/assets/cf8c7daf-fb24-4b48-acfa-0698957e2a9d" /> <br>


## How RustFS Works

```text
+------------+      S3 API      +------------------+
| Application| ---------------> |     RustFS       |
+------------+                  +------------------+
                                        |
                           +------------+------------+
                           |                         |
                    Metadata Storage          Object Storage
                           |                         |
                     Object Information      Images, Videos,
                                             Documents, Backups
```

## Key Features

- Written in Rust for safety and performance.
- S3-compatible API.
- Stores unstructured data as objects.
- Scalable and reliable.
- Suitable for cloud-native applications, backups, and data lakes.

## Object Storage Concept

Each stored object consists of:
- Object data
- Metadata
- Unique Object ID

Unlike traditional file systems, object storage uses a flat namespace instead of folders, making it highly scalable.


**JBOD (Just a Bunch Of Disks)** is a storage configuration where multiple physical disks are used **independently** rather than combined into a RAID array. In Linux, each disk is treated as its own separate storage device unless you explicitly combine them with tools like LVM or `mdadm`.

## How JBOD Works

Imagine you have four hard drives:

```text
Disk 1  → 500 GB
Disk 2  → 1 TB
Disk 3  → 2 TB
Disk 4  → 4 TB
```

In a JBOD setup:

* Each disk is visible separately.
* Data is stored on whichever disk you choose.
* There is **no striping**, **no mirroring**, and **no parity**.

```text
Linux

/dev/sda  → 500 GB
/dev/sdb  → 1 TB
/dev/sdc  → 2 TB
/dev/sdd  → 4 TB
```

You can mount each disk individually:

```bash
sudo mount /dev/sdb1 /mnt/disk1
sudo mount /dev/sdc1 /mnt/disk2
sudo mount /dev/sdd1 /mnt/disk3
```

---

## JBOD vs RAID

| Feature         | JBOD                                             | RAID 0          | RAID 1                                    |
| --------------- | ------------------------------------------------ | --------------- | ----------------------------------------- |
| Data Protection | ❌ No                                             | ❌ No            | ✅ Yes                                     |
| Performance     | Normal                                           | High            | Read performance can improve              |
| Combines Disks  | No (or simple concatenation on some controllers) | Yes             | Yes                                       |
| Disk Sizes      | Can differ                                       | Usually matched | Usually matched                           |
| Fault Tolerance | None                                             | None            | Can survive one disk failure (per mirror) |

---

## Advantages

* Very simple to set up
* No RAID controller required
* Can mix different disk sizes
* Easy to add or remove disks
* Each disk can use its own filesystem

---

## Disadvantages

* No redundancy
* No automatic failover
* If one disk fails, the data on that disk is lost
* No performance improvements from RAID striping

---

## Checking Disks in Linux

List available disks:

```bash
lsblk
```

Example:

```text
NAME   SIZE TYPE
sda    500G disk
sdb      1T disk
sdc      2T disk
sdd      4T disk
```

Show detailed information:

```bash
sudo fdisk -l
```

Or:

```bash
sudo parted -l
```

---

## JBOD in Object Storage (e.g., RustFS, MinIO)

Many modern object storage systems, including RustFS and MinIO, often use **JBOD-style storage**.

Instead of creating a RAID array:

```text
Application
      │
      ▼
   RustFS
      │
 ┌────┼─────┐
 │    │     │
Disk1 Disk2 Disk3 Disk4
```

The object storage software itself decides:

* where to place objects,
* how to replicate or distribute data,
* how to recover from failures.

This shifts data protection and distribution from the storage hardware (RAID) into the application layer, allowing more flexibility and scalability.

---

### When should you use JBOD?

JBOD is a good choice when:

* You want to use disks independently.
* Your application (such as an object storage system) manages data redundancy itself.
* You need flexibility with different disk sizes.
* You don't require RAID-managed redundancy.

For traditional file servers where hardware-level redundancy is important, RAID may be more appropriate. For distributed object storage systems, JBOD is often the preferred approach because the software handles replication and fault tolerance.


