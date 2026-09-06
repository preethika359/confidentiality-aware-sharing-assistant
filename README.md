# Confidentiality-Aware Summarisation and Sharing Assistant

## 1. Project Overview

This project is a software-based Confidentiality-Aware Summarisation and Sharing Assistant designed for university environments.

The system checks user roles and document permission levels before allowing access to university information. It also detects sensitive content and warns against unauthorized sharing.

## 2. Problem Statement

University documents may contain public, internal, faculty-only, confidential, and administrator-only information.

If confidential information is shared with unauthorized users, it can cause privacy and security problems.

This project provides a controlled system that checks access permissions and detects sensitive information before sharing.

## 3. Objective

The main objectives are:

- To control document access based on user roles.
- To classify documents using permission labels.
- To detect sensitive information in documents.
- To prevent unauthorized sharing of confidential information.
- To provide a dashboard for monitoring document permissions and sensitive content.
- To provide clear explanations for access decisions.

## 4. User Roles

The system currently supports three user roles:

- Student
- Faculty
- Admin

## 5. Permission Levels

The system uses configurable permission rules:

- PUBLIC
- INTERNAL
- FACULTY_ONLY
- CONFIDENTIAL
- ADMIN_ONLY

The permission rules are stored in `rules.json`.

## 6. Key Features Completed

### Role-Based Access Control

The system checks whether the selected user role is authorized to access a document.

### Sensitive Content Detection

The system detects predefined sensitive phrases such as:

- Disciplinary investigation
- Strictly confidential
- Salary revision
- Restricted administrator information
- Faculty performance review
- Staff evaluation

### Dashboard

The Streamlit dashboard displays:

- Total documents
- Public documents
- Restricted documents
- Sensitive documents
- Permission distribution chart

### Access Decision Explanation

The system explains why access is allowed or denied.

## 7. Current Working Modules

### `app.py`

Main Streamlit application containing the user interface, dashboard, document selection, and access checking workflow.

### `modules/access_control.py`

Handles role-based permission checking using the configurable rules in `rules.json`.

### `modules/detector.py`

Detects sensitive content using predefined patterns.

### `data/documents.csv`

Contains synthetic university documents used for testing.

### `rules.json`

Contains configurable access rules for different permission levels.

## 8. Current System Workflow

```text
User Role
    ↓
Select Document
    ↓
Permission Check
    ↓
Sensitive Content Detection
    ↓
Access Decision
    ↓
Explanation / Warning
    ↓
Dashboard Monitoring