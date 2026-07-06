# Sandbox Lab V0.1 - Signature Database

## Overview

This project is the first sandbox lab for the **Secure Cloud Sandbox** graduation project.

The goal of this lab is to apply the concepts learned in **Python 101 (Tuwaiq Academy)** by building a simple malware signature database using only the topics covered in the course.

---

## Python Concepts Used

- Variables
- Dictionary
- Functions
- Conditions
- Loops
- Return Statements

---

## Features

- Search for a threat using its hash.
- Search for a hash using the threat name.
- Add a new malware signature.
- Prevent duplicate hash entries.
- Basic hash length validation.

---

## Project Structure

```text
Sandbox_Lab_V0.1/
│
├── signature_database.py
└── README.md
```

---

## Example

```python
signature_database = {
    "A1B2C3": "trojan",
    "D4E5F6": "worm",
    "G7H8I9": "ransomware",
}
```

---

## Purpose

This lab is **not** the final implementation.

It is a learning milestone designed to gradually build the core components of the Secure Cloud Sandbox project while following the Python learning path.

Future labs will replace the in-memory dictionary with file storage, databases, object-oriented design, and more advanced features.

---

## Version

**Sandbox Lab V0.1**
