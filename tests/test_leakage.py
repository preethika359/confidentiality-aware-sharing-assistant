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
# TEST 1: UNAUTHORIZED USER - DISCIPLINARY INFORMATION
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

print("Test 1 Passed: Disciplinary information blocked.")


# ==================================================
# TEST 2: AUTHORIZED ADMIN - SENSITIVE CONTENT
# ==================================================

admin_summary = generate_safe_summary(
    "Admin",
    content,
    sensitive_result
)

assert "disciplinary investigation" in admin_summary

print("Test 2 Passed: Admin sensitive summary generated.")


# ==================================================
# TEST 3: PUBLIC CONTENT
# ==================================================

public_content = (
    "Semester examination starts on June 10. "
    "Students must report 30 minutes before the exam."
)

public_sensitive = detect_sensitive_content(public_content)

public_summary = generate_safe_summary(
    "Student",
    public_content,
    public_sensitive
)

assert "Semester examination starts on June 10" in public_summary

print("Test 3 Passed: Public content summarised.")


# ==================================================
# TEST 4: SALARY INFORMATION
# ==================================================

salary_content = (
    "Faculty salary revision details are restricted "
    "to university administrators."
)

salary_sensitive = detect_sensitive_content(salary_content)

salary_summary = generate_safe_summary(
    "Student",
    salary_content,
    salary_sensitive
)

assert "salary revision" not in salary_summary
assert "university administrators" not in salary_summary

print("Test 4 Passed: Salary information blocked.")


# ==================================================
# TEST 5: FACULTY PERFORMANCE
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

print("Test 5 Passed: Faculty performance information blocked.")


# ==================================================
# TEST 6: NORMAL PUBLIC CONTENT
# ==================================================

library_content = (
    "The library is open from 8 AM to 6 PM on working days."
)

library_sensitive = detect_sensitive_content(library_content)

library_summary = generate_safe_summary(
    "Student",
    library_content,
    library_sensitive
)

assert library_sensitive["sensitive"] is False
assert "library is open" in library_summary.lower()

print("Test 6 Passed: Normal content processed.")


# ==================================================
# TEST 7: STUDENT ID DETECTION
# ==================================================

student_id_content = (
    "Student STU245 is eligible for the examination."
)

result = detect_sensitive_content(student_id_content)

assert result["sensitive"] is True

print("Test 7 Passed: Student ID pattern detected.")


# ==================================================
# TEST 8: RESTRICTED INFORMATION
# ==================================================

restricted_content = (
    "This document contains restricted information "
    "for authorised university staff."
)

result = detect_sensitive_content(restricted_content)

assert result["sensitive"] is True
assert "restricted information" in result["items"]

print("Test 8 Passed: Restricted information detected.")


# ==================================================
# TEST 9: FINANCIAL INFORMATION
# ==================================================

financial_content = (
    "The annual departmental budget contains "
    "restricted financial information."
)

result = detect_sensitive_content(financial_content)

assert result["sensitive"] is True
assert "financial information" in result["items"]

print("Test 9 Passed: Financial information detected.")


# ==================================================
# TEST 10: PERFORMANCE EVALUATION
# ==================================================

evaluation_content = (
    "The employee performance evaluation is confidential."
)

result = detect_sensitive_content(evaluation_content)

assert result["sensitive"] is True
assert "performance evaluation" in result["items"]

print("Test 10 Passed: Performance evaluation detected.")


# ==================================================
# TEST 11: DISCIPLINARY ACTION
# ==================================================

disciplinary_content = (
    "The university has initiated disciplinary action "
    "against the student."
)

result = detect_sensitive_content(disciplinary_content)

assert result["sensitive"] is True
assert "disciplinary action" in result["items"]

print("Test 11 Passed: Disciplinary action detected.")


# ==================================================
# TEST 12: EMPTY INPUT
# ==================================================

result = detect_sensitive_content("")

assert result["sensitive"] is False
assert result["items"] == []

print("Test 12 Passed: Empty input handled safely.")


# ==================================================
# TEST 13: NONE INPUT
# ==================================================

result = detect_sensitive_content(None)

assert result["sensitive"] is False
assert result["items"] == []

print("Test 13 Passed: None input handled safely.")


# ==================================================
# TEST 14: MULTIPLE SENSITIVE PATTERNS
# ==================================================

multiple_content = (
    "The disciplinary investigation includes salary revision "
    "details and strictly confidential information."
)

result = detect_sensitive_content(multiple_content)

assert result["sensitive"] is True
assert len(result["items"]) >= 3

print("Test 14 Passed: Multiple sensitive patterns detected.")


# ==================================================
# TEST 15: CASE INSENSITIVE DETECTION
# ==================================================

case_content = (
    "THIS INFORMATION IS STRICTLY CONFIDENTIAL."
)

result = detect_sensitive_content(case_content)

assert result["sensitive"] is True
assert "strictly confidential" in result["items"]

print("Test 15 Passed: Case-insensitive detection works.")


# ==================================================
# TEST 16: ADMIN SUMMARY FOR SENSITIVE CONTENT
# ==================================================

admin_content = (
    "Faculty salary revision details are restricted "
    "to university administrators."
)

result = detect_sensitive_content(admin_content)

admin_summary = generate_safe_summary(
    "Admin",
    admin_content,
    result
)

assert "salary revision" in admin_summary

print("Test 16 Passed: Admin can review authorised sensitive content.")


# ==================================================
# FINAL RESULT
# ==================================================

print("\n==============================================")
print("ALL 16 LEAKAGE AND EDGE-CASE TESTS PASSED!")
print("Synthetic Test Pass Rate: 100%")
print("==============================================")