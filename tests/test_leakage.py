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
# FINAL RESULT
# ==================================================

print(
    "\nAll leakage tests passed successfully!"
)