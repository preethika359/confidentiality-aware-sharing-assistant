import sys
import os

# Add project root folder to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from modules.detector import detect_sensitive_content
from modules.summarizer import generate_safe_summary


# ==================================================
# TEST 1: UNAUTHORIZED USER - SENSITIVE CONTENT
# ==================================================

content = (
    "Student STU001 is under disciplinary investigation. "
    "This information is strictly confidential."
)

sensitive_result = detect_sensitive_content(content)

summary = generate_safe_summary(
    "Student",
    content,
    sensitive_result
)

assert "STU001" not in summary
assert "disciplinary investigation" not in summary
assert "strictly confidential" not in summary

print(
    "Test 1 Passed: Sensitive information blocked for Student."
)


# ==================================================
# TEST 2: AUTHORIZED ADMIN - SENSITIVE CONTENT
# ==================================================

admin_summary = generate_safe_summary(
    "Admin",
    content,
    sensitive_result
)

assert "disciplinary investigation" in admin_summary

print(
    "Test 2 Passed: Authorised Admin summary generated."
)


# ==================================================
# TEST 3: PUBLIC CONTENT
# ==================================================

public_content = (
    "Semester examination starts on June 10. "
    "Students must report 30 minutes before the exam."
)

public_sensitive = detect_sensitive_content(
    public_content
)

public_summary = generate_safe_summary(
    "Student",
    public_content,
    public_sensitive
)

assert (
    "Semester examination starts on June 10"
    in public_summary
)

print(
    "Test 3 Passed: Public content summarised successfully."
)


# ==================================================
# TEST 4: UNAUTHORIZED USER - SALARY INFORMATION
# ==================================================

salary_content = (
    "Faculty salary revision details are restricted "
    "to university administrators."
)

salary_sensitive = detect_sensitive_content(
    salary_content
)

salary_summary = generate_safe_summary(
    "Student",
    salary_content,
    salary_sensitive
)

assert "salary revision" not in salary_summary
assert "university administrators" not in salary_summary

print(
    "Test 4 Passed: Restricted salary information blocked for Student."
)


# ==================================================
# TEST 5: UNAUTHORIZED USER - FACULTY PERFORMANCE
# ==================================================

performance_content = (
    "Faculty performance review information is available "
    "only to authorised faculty members and administrators."
)

performance_sensitive = detect_sensitive_content(
    performance_content
)

performance_summary = generate_safe_summary(
    "Student",
    performance_content,
    performance_sensitive
)

assert "faculty performance review" not in performance_summary

print(
    "Test 5 Passed: Faculty performance information blocked for Student."
)


# ==================================================
# TEST 6: NORMAL PUBLIC CONTENT - NO FALSE BLOCKING
# ==================================================

library_content = (
    "The library is open from 8 AM to 6 PM on working days."
)

library_sensitive = detect_sensitive_content(
    library_content
)

library_summary = generate_safe_summary(
    "Student",
    library_content,
    library_sensitive
)

assert "library is open" in library_summary.lower()
assert library_sensitive["sensitive"] is False

print(
    "Test 6 Passed: Normal public content processed without false blocking."
)


# ==================================================
# FINAL RESULT
# ==================================================

print(
    "\nAll 6 leakage and edge-case tests passed successfully!"
)