import re


SENSITIVE_PATTERNS = [
    "disciplinary investigation",
    "strictly confidential",
    "salary revision",
    "restricted to university administrators",
    "faculty performance review",
    "staff evaluation",
    "confidential information",
    "restricted information",
    "internal investigation",
    "performance evaluation",
    "disciplinary action",
    "salary details",
    "financial information"
]


SENSITIVE_REGEX_PATTERNS = [
    r"\bSTU\d+\b",                 # Student ID like STU001
    r"\b\d{10}\b",                 # 10-digit number
    r"\bsalary\s+(?:is|was|of)?\s*\$?\d+",
    r"\b\d+%\s*(?:salary|increment|hike)\b"
]


def detect_sensitive_content(text):
    if not text:
        return {
            "sensitive": False,
            "items": []
        }

    text_lower = text.lower()

    detected = []

    # Keyword-based detection
    for pattern in SENSITIVE_PATTERNS:
        if pattern in text_lower:
            detected.append(pattern)

    # Pattern-based detection
    for pattern in SENSITIVE_REGEX_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:
            if match not in detected:
                detected.append(match)

    return {
        "sensitive": len(detected) > 0,
        "items": detected
    }