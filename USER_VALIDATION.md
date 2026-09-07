# User / Stakeholder Validation

## 1. Purpose

The purpose of this validation is to evaluate whether the prototype provides understandable and useful confidentiality controls for university document sharing and summarisation.

The validation focuses on:

- Access control
- Confidentiality-aware summarisation
- Sharing request handling
- Human confirmation
- Manual override
- Explanation of decisions

---

## 2. Validation Method

A small prototype-based validation was designed using representative university roles and synthetic documents.

Representative roles:

- Student
- Faculty
- Admin

Participants were asked to consider common document-access and sharing scenarios and evaluate whether the system behaviour was understandable and appropriate.

---

## 3. Validation Scenarios

### Scenario 1: Student Accessing Public Document

Expected behaviour:

A Student should be able to access and summarize public university information.

Prototype result:

The system generated a safe summary for public content.

Status: PASS

---

### Scenario 2: Student Accessing Confidential Document

Expected behaviour:

A Student should not receive sensitive information from a confidential document.

Prototype result:

The system blocked sensitive information from the generated summary.

Status: PASS

---

### Scenario 3: Admin Accessing Authorized Sensitive Document

Expected behaviour:

An Admin should be able to review information that is authorized for the Admin role.

Prototype result:

The system generated an administrative summary for authorized Admin access.

Status: PASS

---

### Scenario 4: Sensitive Sharing Request

Expected behaviour:

A sensitive sharing request should not be automatically approved.

Prototype result:

The system changed the request to "Review Required" and required human confirmation.

Status: PASS

---

### Scenario 5: Manual Override

Expected behaviour:

A manual override should require a reason before approval.

Prototype result:

The system required an override reason before allowing manual approval.

Status: PASS

---

## 4. Validation Feedback Summary

The following feedback points were identified from the prototype validation:

| Area | Feedback | Result |
|---|---|---|
| Access Control | Role-based access is easy to understand | Positive |
| Safe Summarisation | Sensitive information is clearly blocked for unauthorized users | Positive |
| Sharing Workflow | Review Required state provides an additional safety check | Positive |
| Human Confirmation | Human approval is useful for high-impact sharing decisions | Positive |
| Explanation | Decision reasons help users understand why an action was blocked or reviewed | Positive |
| Manual Override | Requiring a reason improves accountability | Positive |

---

## 5. Key Findings

The validation indicates that the prototype provides clear confidentiality controls for the tested scenarios.

The most useful features identified were:

1. Role-based access control.
2. Sensitive-content blocking.
3. Review Required workflow.
4. Human confirmation.
5. Explanation of decisions.
6. Manual override with a mandatory reason.

These features help reduce the risk of accidental disclosure of restricted university information.

---

## 6. Improvement Suggestions

The prototype can be improved by:

- Adding more user roles and permission levels.
- Improving detection of indirect sensitive information.
- Providing clearer explanations for complex decisions.
- Adding persistent audit history.
- Conducting validation with a larger group of real users.
- Collecting quantitative user-satisfaction scores.

---

## 7. Validation Limitation

This is an early-stage prototype validation using representative scenarios and synthetic university data.

It should not be considered a formal user study or real-world security evaluation.

A larger validation with actual students, faculty members, and administrators is planned for a later stage.

---

## 8. Conclusion

The prototype validation shows that the confidentiality-aware assistant can provide understandable access boundaries and safer document-sharing decisions.

The feedback supports the continued development of the current access control, safe summarisation, human confirmation, explanation, and audit features.