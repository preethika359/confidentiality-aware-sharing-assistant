import json


def load_rules():
    with open("rules.json", "r") as file:
        return json.load(file)


def check_access(user_role, permission_label):
    rules = load_rules()

    allowed_roles = rules.get(permission_label, [])

    if user_role in allowed_roles:
        return {
            "allowed": True,
            "reason": f"{user_role} role is authorised for {permission_label} content."
        }

    return {
        "allowed": False,
        "reason": (
            f"{user_role} role is NOT authorised for {permission_label} content."
        )
    }