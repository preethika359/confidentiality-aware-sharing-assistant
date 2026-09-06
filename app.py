import streamlit as st
import pandas as pd
from datetime import datetime

from modules.access_control import check_access
from modules.detector import detect_sensitive_content
from modules.summarizer import generate_safe_summary
from modules.sharing import (
    create_sharing_request,
    evaluate_sharing_request
)

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Confidentiality-Aware Sharing Assistant",
    page_icon="🔐",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "audit_log" not in st.session_state:
    st.session_state.audit_log = []

if "sharing_request" not in st.session_state:
    st.session_state.sharing_request = None

if "sharing_result" not in st.session_state:
    st.session_state.sharing_result = None

if "sensitive_result" not in st.session_state:
    st.session_state.sensitive_result = None

if "requester_access" not in st.session_state:
    st.session_state.requester_access = None

if "target_access" not in st.session_state:
    st.session_state.target_access = None


# --------------------------------------------------
# AUDIT LOG FUNCTION
# --------------------------------------------------

def add_audit_log(
    action,
    user_role,
    document_id,
    document_title,
    target_role,
    decision,
    reason
):
    st.session_state.audit_log.append({
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Action": action,
        "User Role": user_role,
        "Document ID": document_id,
        "Document": document_title,
        "Target Role": target_role,
        "Decision": decision,
        "Reason": reason
    })


# --------------------------------------------------
# LOAD DOCUMENTS
# --------------------------------------------------

@st.cache_data
def load_documents():
    return pd.read_csv("data/documents.csv")


documents = load_documents()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "🔐 Confidentiality-Aware Summarisation & Sharing Assistant"
)

st.write(
    "This system checks user permissions and sensitive content "
    "before allowing university information to be accessed, "
    "summarised, or shared."
)


# --------------------------------------------------
# SIDEBAR - USER ROLE
# --------------------------------------------------

st.sidebar.header("👤 User Access")

user_role = st.sidebar.selectbox(
    "Select User Role",
    ["Student", "Faculty", "Admin"]
)


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

st.header("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

total_documents = len(documents)

public_count = len(
    documents[
        documents["permission_label"] == "PUBLIC"
    ]
)

restricted_count = len(
    documents[
        documents["permission_label"] != "PUBLIC"
    ]
)

sensitive_count = sum(
    detect_sensitive_content(content)["sensitive"]
    for content in documents["content"]
)

col1.metric(
    "📄 Total Documents",
    total_documents
)

col2.metric(
    "🌐 Public Documents",
    public_count
)

col3.metric(
    "🔒 Restricted Documents",
    restricted_count
)

col4.metric(
    "⚠️ Sensitive Documents",
    sensitive_count
)


# --------------------------------------------------
# PERMISSION DISTRIBUTION
# --------------------------------------------------

st.subheader("📈 Permission Distribution")

permission_counts = documents[
    "permission_label"
].value_counts()

st.bar_chart(permission_counts)


# --------------------------------------------------
# DOCUMENT ACCESS
# --------------------------------------------------

st.header("📄 Document Access")

selected_document = st.selectbox(
    "Select a document",
    documents["title"].tolist()
)

document = documents[
    documents["title"] == selected_document
].iloc[0]

document_id = document["document_id"]
permission_label = document["permission_label"]
content = document["content"]


st.write(
    "**Document ID:**",
    document_id
)

st.write(
    "**Permission Level:**",
    permission_label
)


# --------------------------------------------------
# CHECK ACCESS
# --------------------------------------------------

if st.button("🔍 Check Access"):

    access_result = check_access(
        user_role,
        permission_label
    )

    sensitive_result = detect_sensitive_content(
        content
    )

    if access_result["allowed"]:

        st.success("✅ Access Allowed")

        st.info(
            access_result["reason"]
        )

        if sensitive_result["sensitive"]:

            st.warning(
                "⚠️ Sensitive content detected."
            )

            st.write(
                "**Detected patterns:**"
            )

            for item in sensitive_result["items"]:
                st.write("•", item)

            st.warning(
                "Sensitive information should not be included "
                "in an unauthorized summary or sharing request."
            )

        else:

            st.success(
                "✅ No sensitive content detected."
            )

        st.subheader("📋 Document Content")

        st.write(content)

        add_audit_log(
            action="Document Access",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role="-",
            decision="Allowed",
            reason=access_result["reason"]
        )

    else:

        st.error("🚫 Access Denied")

        st.warning(
            access_result["reason"]
        )

        st.info(
            "This document cannot be accessed or shared "
            "with the selected user role."
        )

        if sensitive_result["sensitive"]:

            st.error(
                "🔐 Sensitive information detected. "
                "Access and sharing are restricted."
            )

        add_audit_log(
            action="Document Access",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role="-",
            decision="Denied",
            reason=access_result["reason"]
        )


# --------------------------------------------------
# SAFE SUMMARISATION
# --------------------------------------------------

st.header("📝 Confidentiality-Aware Summarisation")

st.write(
    "Generate a summary according to the selected user's "
    "access permissions. Sensitive information is protected "
    "from unauthorized summaries."
)


if st.button(
    "🧠 Generate Safe Summary",
    key="summary_button"
):

    access_result = check_access(
        user_role,
        permission_label
    )

    sensitive_result = detect_sensitive_content(
        content
    )

    summary = generate_safe_summary(
        user_role,
        content,
        sensitive_result
    )

    if user_role != "Admin" and sensitive_result["sensitive"]:

        st.error(
            "🚫 Summary Blocked"
        )

        st.warning(
            summary
        )

        add_audit_log(
            action="Safe Summarisation",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role="-",
            decision="Blocked",
            reason=summary
        )

    elif not access_result["allowed"]:

        st.error(
            "🚫 Summary Blocked"
        )

        st.warning(
            "You are not authorised to access this document."
        )

        add_audit_log(
            action="Safe Summarisation",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role="-",
            decision="Blocked",
            reason="User role is not authorised."
        )

    else:

        st.success(
            "✅ Safe Summary Generated"
        )

        st.info(summary)

        add_audit_log(
            action="Safe Summarisation",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role="-",
            decision="Allowed",
            reason="Summary generated according to access rules."
        )


# --------------------------------------------------
# SHARING REQUEST
# --------------------------------------------------

st.header("📤 Sharing Request")

st.write(
    "Create a request to share the selected document "
    "with another university user role."
)


target_role = st.selectbox(
    "Select Target User Role",
    ["Student", "Faculty", "Admin"],
    key="target_role"
)


if st.button(
    "📤 Create Sharing Request",
    key="create_sharing_button"
):

    requester_access = check_access(
        user_role,
        permission_label
    )

    target_access = check_access(
        target_role,
        permission_label
    )

    sensitive_result = detect_sensitive_content(
        content
    )

    sharing_request = create_sharing_request(
        requester_role=user_role,
        document_id=document_id,
        document_title=selected_document,
        target_role=target_role
    )

    result = evaluate_sharing_request(
        sharing_request,
        target_access,
        sensitive_result
    )

    st.session_state.sharing_request = sharing_request
    st.session_state.sharing_result = result
    st.session_state.sensitive_result = sensitive_result
    st.session_state.requester_access = requester_access
    st.session_state.target_access = target_access


# --------------------------------------------------
# SHARING REQUEST DETAILS
# --------------------------------------------------

if st.session_state.sharing_request is not None:

    request = st.session_state.sharing_request
    result = st.session_state.sharing_result
    sensitive_result = st.session_state.sensitive_result
    requester_access = st.session_state.requester_access
    target_access = st.session_state.target_access

    st.subheader(
        "📋 Sharing Request Details"
    )

    st.write(
        "**Requester Role:**",
        request["requester_role"]
    )

    st.write(
        "**Document:**",
        request["document_title"]
    )

    st.write(
        "**Target Role:**",
        request["target_role"]
    )


    # --------------------------------------------------
    # REQUESTER NOT AUTHORISED
    # --------------------------------------------------

    if not requester_access["allowed"]:

        st.error(
            "🚫 Sharing Request Blocked"
        )

        reason = (
            "The requester is not authorised "
            "to access this document."
        )

        st.warning(reason)

        add_audit_log(
            action="Sharing Request",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role=target_role,
            decision="Blocked",
            reason=reason
        )

        st.session_state.sharing_request = None


    # --------------------------------------------------
    # TARGET NOT AUTHORISED
    # --------------------------------------------------

    elif not target_access["allowed"]:

        st.error(
            "🚫 Sharing Request Blocked"
        )

        reason = (
            "The target user role is not authorised "
            "to receive this document."
        )

        st.warning(reason)

        add_audit_log(
            action="Sharing Request",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role=target_role,
            decision="Blocked",
            reason=reason
        )


    # --------------------------------------------------
    # SENSITIVE CONTENT
    # --------------------------------------------------

    elif sensitive_result["sensitive"]:

        st.warning(
            "⚠️ Review Required"
        )

        st.info(
            "Sensitive content was detected. "
            "Human confirmation is required before sharing."
        )

        st.write(
            "**Detected sensitive patterns:**"
        )

        for item in sensitive_result["items"]:
            st.write("•", item)


        # --------------------------------------------------
        # HUMAN CONFIRMATION
        # --------------------------------------------------

        st.subheader(
            "👤 Human Confirmation"
        )

        st.write(
            "A human reviewer must confirm this sharing "
            "request before sensitive information can be shared."
        )

        confirmation = st.checkbox(
            "I confirm that this sharing request has been reviewed.",
            key="human_confirmation"
        )


        override_reason = st.text_area(
            "Mandatory reason for approval/override",
            placeholder=(
                "Enter the reason for allowing this "
                "sensitive sharing request..."
            ),
            key="override_reason"
        )


        if st.button(
            "🔓 Confirm Manual Override",
            key="manual_override_button"
        ):

            if not confirmation:

                st.error(
                    "❌ Human confirmation is required."
                )

            elif not override_reason.strip():

                st.error(
                    "❌ Override reason is mandatory."
                )

            else:

                add_audit_log(
                    action="Manual Override",
                    user_role=user_role,
                    document_id=document_id,
                    document_title=selected_document,
                    target_role=target_role,
                    decision="Approved",
                    reason=override_reason
                )

                st.success(
                    "✅ Manual Override Approved"
                )

                st.info(
                    "Sensitive sharing was approved "
                    "after human confirmation."
                )

                st.write(
                    "**Override Reason:**",
                    override_reason
                )


    # --------------------------------------------------
    # NORMAL APPROVAL
    # --------------------------------------------------

    else:

        st.success(
            "✅ Sharing Request Approved"
        )

        st.info(
            result["reason"]
        )

        add_audit_log(
            action="Sharing Request",
            user_role=user_role,
            document_id=document_id,
            document_title=selected_document,
            target_role=target_role,
            decision="Approved",
            reason=result["reason"]
        )


# --------------------------------------------------
# AUDIT TRAIL
# --------------------------------------------------

st.header(
    "📝 Auditable Decision Trail"
)

st.write(
    "This section records important access, sharing, "
    "summarisation, and manual override decisions "
    "made during the session."
)


if st.session_state.audit_log:

    audit_dataframe = pd.DataFrame(
        st.session_state.audit_log
    )

    st.dataframe(
        audit_dataframe,
        width="stretch"
    )

else:

    st.info(
        "No decisions have been recorded yet."
    )


# --------------------------------------------------
# DOCUMENT OVERVIEW
# --------------------------------------------------

st.header(
    "📚 Document Overview"
)

display_data = documents[
    [
        "document_id",
        "title",
        "permission_label"
    ]
]

st.dataframe(
    display_data,
    width="stretch"
)