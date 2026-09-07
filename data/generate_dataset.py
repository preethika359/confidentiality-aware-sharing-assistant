import csv
import os


# ==================================================
# SYNTHETIC UNIVERSITY DOCUMENT DATASET
# ==================================================

documents = [
    {
        "document_id": "DOC001",
        "title": "Examination Policy",
        "permission_label": "PUBLIC",
        "content": "Semester examination starts on June 10. Students must report 30 minutes before the exam."
    },
    {
        "document_id": "DOC002",
        "title": "Internal Timetable",
        "permission_label": "INTERNAL",
        "content": "The university internal assessment schedule will be published next week."
    },
    {
        "document_id": "DOC003",
        "title": "Faculty Meeting",
        "permission_label": "FACULTY_ONLY",
        "content": "Faculty meeting will be conducted on June 5. Internal staff evaluation will be discussed."
    },
    {
        "document_id": "DOC004",
        "title": "Student Disciplinary Case",
        "permission_label": "CONFIDENTIAL",
        "content": "Student STU001 is under disciplinary investigation. This information is strictly confidential."
    },
    {
        "document_id": "DOC005",
        "title": "Faculty Salary Revision",
        "permission_label": "ADMIN_ONLY",
        "content": "Faculty salary revision details are restricted to university administrators."
    },
    {
        "document_id": "DOC006",
        "title": "Library Policy",
        "permission_label": "PUBLIC",
        "content": "The library is open from 8 AM to 6 PM on working days."
    },
    {
        "document_id": "DOC007",
        "title": "Student Attendance",
        "permission_label": "INTERNAL",
        "content": "Students must maintain the minimum attendance requirement according to university regulations."
    },
    {
        "document_id": "DOC008",
        "title": "Staff Performance",
        "permission_label": "FACULTY_ONLY",
        "content": "Faculty performance review information is available only to authorised faculty members and administrators."
    },
    {
        "document_id": "DOC009",
        "title": "Scholarship Policy",
        "permission_label": "PUBLIC",
        "content": "Eligible students can apply for university scholarships before the announced deadline."
    },
    {
        "document_id": "DOC010",
        "title": "Administrative Budget",
        "permission_label": "ADMIN_ONLY",
        "content": "The annual departmental budget contains restricted financial information for administrators."
    }
]


# ==================================================
# GENERATE CSV FILE
# ==================================================

output_file = os.path.join(
    os.path.dirname(__file__),
    "documents.csv"
)

with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "document_id",
        "title",
        "permission_label",
        "content"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(documents)


print("Synthetic dataset generated successfully!")
print(f"Total documents: {len(documents)}")
print(f"Output file: {output_file}")