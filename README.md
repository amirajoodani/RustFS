# RustFS
Repository for Laerning Rustfs

# RustFS Object Storage

## What is RustFS?

RustFS is an open-source object storage server written in **Rust**. It provides an **Amazon S3-compatible API**, allowing applications to store and retrieve objects such as documents, images, videos, backups, and datasets using standard S3 tools and SDKs.

> **Add an architecture image here:**  
> You can replace the placeholder below with a RustFS architecture diagram or screenshot.

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

