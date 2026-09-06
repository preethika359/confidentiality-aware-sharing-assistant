SENSITIVE_PATTERNS = [
    "disciplinary investigation",
    "strictly confidential",
    "salary revision",
    "restricted to university administrators",
    "faculty performance review",
    "staff evaluation"
]


def detect_sensitive_content(text):
    text_lower = text.lower()

    detected = [
        pattern
        for pattern in SENSITIVE_PATTERNS
        if pattern in text_lower
    ]

    return {
        "sensitive": len(detected) > 0,
        "items": detected
    }