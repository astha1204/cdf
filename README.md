# 📦 Metadata Ingestion API (FastAPI + MongoDB)

This project provides a lightweight backend API built with **FastAPI** to ingest and store metadata of uploaded files (like CSV, JSON, etc.) into **MongoDB**, using a well-defined schema.

---

## ✅ Features

- Accepts file metadata as JSON payloads
- Validates input using **Pydantic** models
- Stores data in MongoDB with **schema validation**
- Provides a basic GET endpoint to fetch all documents

---

## 🔧 Technologies Used

- ⚡ FastAPI – for creating high-performance REST APIs
- 🍃 MongoDB Atlas – for storing structured metadata
- 🧪 Pydantic – for schema validation and type enforcement
- 🐍 Python – the core runtime

---
## 📁 Folder Structure
app/
├── db.py # MongoDB connection + schema enforcement
├── models.py # Pydantic models for metadata structure
├── main.py # API route handlers (upload + get)
main.py # FastAPI app entrypoint
