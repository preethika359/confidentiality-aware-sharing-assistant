def create_sharing_request(
    requester_role,
    document_id,
    document_title,
    target_role
):
    return {
        "requester_role": requester_role,
        "document_id": document_id,
        "document_title": document_title,
        "target_role": target_role,
        "status": "Pending"
    }


def evaluate_sharing_request(request, access_result, sensitive_result):
    if not access_result["allowed"]:
        return {
            "status": "Blocked",
            "reason": "Sharing request blocked because the target role is not authorised."
        }

    if sensitive_result["sensitive"]:
        return {
            "status": "Review Required",
            "reason": "Sensitive content detected. Human confirmation is required before sharing."
        }

    return {
        "status": "Approved",
        "reason": "Sharing request passed permission and sensitivity checks."
    }