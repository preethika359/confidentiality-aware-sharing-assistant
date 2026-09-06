# Confidentiality-Aware Summarisation and Sharing Assistant

## 1. Project Overview

This project is a software-based Confidentiality-Aware Summarisation and Sharing Assistant designed for university environments.

The system checks user roles and document permission levels before allowing access to university information. It also detects sensitive content and prevents unauthorized summarisation and sharing.

The system provides explanations for access decisions and maintains an auditable decision trail for important actions.

---

## 2. Problem Statement

University documents may contain different levels of information such as:

- Public information
- Internal information
- Faculty-only information
- Confidential information
- Administrator-only information

If confidential information is shared with unauthorized users, it can cause privacy and security problems.

This project provides a controlled system that checks access permissions and detects sensitive information before allowing summarisation or sharing.

---

## 3. Objective

The main objectives of the project are:

- To control document access based on user roles.
- To classify documents using permission labels.
- To detect sensitive information in documents.
- To prevent unauthorized sharing of confidential information.
- To prevent sensitive information from appearing in unauthorized summaries.
- To provide a dashboard for monitoring document permissions and sensitive content.
- To provide clear explanations for access decisions.
- To require human confirmation for sensitive sharing requests.
- To maintain an auditable decision trail.

---

## 4. User Roles

The system currently supports three user roles:

- Student
- Faculty
- Admin

---

## 5. Permission Levels

The system uses configurable permission rules:

- PUBLIC
- INTERNAL
- FACULTY_ONLY
- CONFIDENTIAL
- ADMIN_ONLY

The permission rules are stored in `rules.json`.

Example:

```text
PUBLIC
    ↓
Student + Faculty + Admin

INTERNAL
    ↓
Student + Faculty + Admin

FACULTY_ONLY
    ↓
Faculty + Admin

CONFIDENTIAL
    ↓
Admin

ADMIN_ONLY
    ↓
Admin