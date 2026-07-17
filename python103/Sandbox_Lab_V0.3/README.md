# Sandbox Lab V0.3 – Secure Sample Registry (OOP Edition)

## Overview

Sandbox Lab V0.3 is the Object-Oriented Programming (OOP) version of the Secure Sample Registry developed as part of my cybersecurity learning journey.

The goal of this version is not to introduce new functionality, but to redesign the previous procedural implementation using OOP principles learned in Python 103.

---

## Objective

Transform the Secure Sample Registry from a procedural application into an object-oriented architecture.

---

## Python Concepts Used

- Classes
- Objects
- Constructors
- Encapsulation
- Private Attributes
- Getters
- Setters
- Object Collaboration

---

## Project Structure

```text
Sandbox_Lab_V0.3/
│
├── sandbox_lab_v0_3.py
└── README.md
```

---

## Classes

### Sample

Represents a single malware sample.

Responsibilities:

- Store sample information
- Validate data
- Generate a fake SHA-256 hash
- Display sample information

---

### SampleRegistry

Represents the registry that manages multiple samples.

Responsibilities:

- Add samples
- Display samples
- Search by:
  - File Name
  - SHA-256
  - Threat Type
- Show statistics
- Find oldest/newest sample
- Sort samples
- Reverse samples
- Calculate days since upload

---

## Features

- Generate fake SHA-256 hashes
- Encapsulated sample data
- Input validation
- Malware sample management
- Searching
- Statistics
- Sorting
- Date calculations

---

## Version History

- V0.1 — Malware Signature Database
- V0.2 — Secure Sample Registry (Procedural)
- V0.3 — Secure Sample Registry (Object-Oriented)

---

## Future Improvements

- Split the project into multiple modules.
- Separate user interface from business logic.
- Export data to JSON.
- Replace fake hashes with real SHA-256 values.
- Integrate with the Secure Cloud Sandbox project.

---

Developed as part of my cybersecurity and Python learning journey.
