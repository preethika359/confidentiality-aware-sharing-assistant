def generate_safe_summary(user_role, content, sensitive_result):

    # Unauthorized users
    if user_role != "Admin" and sensitive_result["sensitive"]:
        return (
            "⚠️ This document contains restricted information. "
            "Sensitive details have been removed to protect confidentiality."
        )

    # Admin users
    if user_role == "Admin" and sensitive_result["sensitive"]:

        sentences = [
            sentence.strip()
            for sentence in content.split(".")
            if sentence.strip()
        ]

        if sentences:
            return (
                "Administrative Summary: "
                + " ".join(sentences[:2])
                + "."
            )

        return (
            "Administrative Summary: "
            "Sensitive university information is available "
            "for authorised administrative review."
        )

    # Normal non-sensitive document
    sentences = [
        sentence.strip()
        for sentence in content.split(".")
        if sentence.strip()
    ]

    if sentences:
        return (
            "Safe Summary: "
            + sentences[0]
            + "."
        )

    return "No summary available."