# Metadata Ingestion API (FastAPI + MongoDB + MinIO)

This project provides a FastAPI-based backend for ingesting file metadata (like CSV, JSON) into a MongoDB database, with optional file storage in MinIO.

## Features

- Upload metadata of files (structured/unstructured)
- Store metadata in MongoDB
- Optional file storage in MinIO (S3 compatible)
- Supports normalized, raw, and enriched content structure

## Technologies

- 🐍 Python
- ⚡ FastAPI
- 🍃 MongoDB (local or cloud)
- ☁️ MinIO (S3-compatible storage)
- 🧪 Pydantic Schema Validation

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
