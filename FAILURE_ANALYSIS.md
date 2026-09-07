# Failure Mode Analysis

## 1. Purpose

This document analyses important failure and edge cases in the Confidentiality-Aware Summarisation and Sharing Assistant.

The purpose is to verify that unauthorized users cannot access or receive sensitive information and that the system handles sensitive sharing requests safely.

---

## 2. Failure Cases

| Test Case | Failure / Edge Case | Expected Behaviour | Actual Result | Status |
|---|---|---|---|---|
| 1 | Student requests summary of confidential disciplinary case | Sensitive information must not be included in the summary | Sensitive information was blocked | PASS |
| 2 | Admin requests summary of confidential content | Authorised Admin should be able to review authorised sensitive content | Admin summary was generated | PASS |
| 3 | Student requests summary of public examination policy | Public content should be summarised normally | Public summary was generated | PASS |
| 4 | Student requests restricted faculty salary information | Salary information must not be leaked | Restricted information was blocked | PASS |
| 5 | Student requests faculty performance information | Faculty-only information must not be leaked | Restricted information was blocked | PASS |
| 6 | Student requests normal library information | Normal public content should not be incorrectly blocked | Public content was processed successfully | PASS |

---

## 3. Human Confirmation Failure Case

### Scenario

A sharing request contains sensitive information and requires human confirmation before approval.

### Expected Behaviour

The system must not immediately approve the request.

It should display:

- Sensitive content detected
- Review Required
- Human confirmation required
- Manual override reason required

### Result

The system changes the sharing request to **Review Required** and requires human confirmation before manual approval.

### Status

**PASS**

---

## 4. Missing Override Reason

### Scenario

A user attempts to approve a sensitive sharing request without providing a reason.

### Expected Behaviour

The system should prevent manual override approval.

### Result

The application requires an override reason before allowing manual approval.

### Status

**PASS**

---

## 5. Unauthorized Sharing

### Scenario

A user attempts to share a document with a role that is not authorised for its permission level.

### Expected Behaviour

The sharing request should be blocked.

### Result

The system checks the target role against the configured permission rules and blocks unauthorized sharing.

### Status

**PASS**

---

## 6. Error Analysis

The prototype was tested using synthetic university policy and administrative documents.

The tests showed that:

- Sensitive information was blocked for unauthorized users.
- Authorized administrative users could access permitted sensitive information.
- Public documents were summarized normally.
- Restricted salary and performance information was protected.
- Sensitive sharing requests required human confirmation.
- Manual overrides required a reason.
- Normal public content was not falsely blocked.

The current synthetic test suite achieved:

**6/6 tests passed (100% pass rate).**

This result applies only to the current synthetic test cases and does not represent a real-world security guarantee.

---

## 7. Remaining Risks

The current prototype still has some limitations:

1. The sensitive-content detector uses predefined keyword patterns.
2. New types of confidential information may not be detected.
3. The audit trail is currently maintained during the application session.
4. The prototype uses synthetic data rather than real university documents.
5. More adversarial leakage tests are required.
6. User/stakeholder validation is still pending.

---

## 8. Future Improvements

Future versions will improve the system by:

- Adding more sensitive-content patterns.
- Adding adversarial and indirect leakage tests.
- Improving semantic sensitivity detection.
- Adding persistent audit-log storage.
- Performing formal error analysis.
- Collecting user/stakeholder feedback.
- Adding more realistic synthetic datasets.

---

## 9. Conclusion

The failure-mode analysis demonstrates that the prototype can identify and prevent several important confidentiality risks.

The current implementation successfully passed all six synthetic leakage and edge-case tests and provides additional safeguards through human confirmation, manual override controls, and access-based decision making.