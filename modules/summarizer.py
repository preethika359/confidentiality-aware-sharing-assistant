def generate_safe_summary(user_role, content, sensitive_result):

    if not content:
        return "No summary available."

    # ==============================================
    # UNAUTHORIZED USER - SENSITIVE CONTENT
    # ==============================================

    if user_role != "Admin" and sensitive_result["sensitive"]:

        safe_sentences = []

        sentences = [
            sentence.strip()
            for sentence in content.split(".")
            if sentence.strip()
        ]

        sensitive_items = [
            item.lower()
            for item in sensitive_result["items"]
        ]

        for sentence in sentences:

            sentence_lower = sentence.lower()

            contains_sensitive_info = any(
                item in sentence_lower
                for item in sensitive_items
            )

            if not contains_sensitive_info:
                safe_sentences.append(sentence)

        if safe_sentences:
            return (
                "Safe Summary: "
                + safe_sentences[0]
                + ". "
                "Restricted details have been removed."
            )

        return (
            "⚠️ This document contains restricted information. "
            "Sensitive details have been removed to protect confidentiality."
        )

    # ==============================================
    # ADMIN USER - SENSITIVE CONTENT
    # ==============================================

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

    # ==============================================
    # NORMAL NON-SENSITIVE CONTENT
    # ==============================================

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