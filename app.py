import streamlit as st
import pandas as pd

from modules.access_control import check_access
from modules.detector import detect_sensitive_content


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Confidentiality-Aware Sharing Assistant",
    page_icon="🔐",
    layout="wide"
)


# -----------------------------
# Load Documents
# -----------------------------
@st.cache_data
def load_documents():
    return pd.read_csv("data/documents.csv")


documents = load_documents()


# -----------------------------
# Title
# -----------------------------
st.title("🔐 Confidentiality-Aware Summarisation & Sharing Assistant")
st.write(
    "This system checks user permissions and sensitive content "
    "before allowing university information to be shared."
)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("User Access")

user_role = st.sidebar.selectbox(
    "Select User Role",
    ["Student", "Faculty", "Admin"]
)


# -----------------------------
# Dashboard
# -----------------------------
st.header("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

total_documents = len(documents)

public_count = len(
    documents[documents["permission_label"] == "PUBLIC"]
)

restricted_count = len(
    documents[documents["permission_label"] != "PUBLIC"]
)

sensitive_count = sum(
    detect_sensitive_content(content)["sensitive"]
    for content in documents["content"]
)

col1.metric("📄 Total Documents", total_documents)
col2.metric("🌐 Public Documents", public_count)
col3.metric("🔒 Restricted Documents", restricted_count)
col4.metric("⚠️ Sensitive Documents", sensitive_count)


st.subheader("Permission Distribution")

permission_counts = documents["permission_label"].value_counts()

st.bar_chart(permission_counts)


# -----------------------------
# Document Selection
# -----------------------------
st.header("📄 Document Access")

selected_document = st.selectbox(
    "Select a document",
    documents["title"].tolist()
)


document = documents[
    documents["title"] == selected_document
].iloc[0]


permission_label = document["permission_label"]
content = document["content"]


st.write("**Document ID:**", document["document_id"])
st.write("**Permission Level:**", permission_label)


# -----------------------------
# Access Check
# -----------------------------
if st.button("🔍 Check Access"):

    access_result = check_access(
        user_role,
        permission_label
    )

    sensitive_result = detect_sensitive_content(content)


    # -----------------------------
    # Allowed
    # -----------------------------
    if access_result["allowed"]:

        st.success("✅ Access Allowed")

        st.info(access_result["reason"])

        if sensitive_result["sensitive"]:
            st.warning("⚠️ Sensitive content detected.")

            st.write("Detected patterns:")

            for item in sensitive_result["items"]:
                st.write("•", item)

            st.warning(
                "Sensitive information should not be included "
                "in an unauthorized summary or sharing request."
            )

        else:
            st.success("No sensitive content detected.")

        st.subheader("📋 Document Content")
        st.write(content)


    # -----------------------------
    # Denied
    # -----------------------------
    else:

        st.error("🚫 Access Denied")

        st.warning(access_result["reason"])

        st.info(
            "This document cannot be shared with the selected user role."
        )

        if sensitive_result["sensitive"]:
            st.error(
                "🔐 Sensitive information detected. "
                "Sharing is blocked."
            )


# -----------------------------
# Document Table
# -----------------------------
st.header("📚 Document Overview")

display_data = documents[
    ["document_id", "title", "permission_label"]
]

st.dataframe(
    display_data,
    use_container_width=True
)