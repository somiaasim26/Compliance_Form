# --- 📦 Required Libraries ---
# pip install streamlit pandas

import streamlit as st
import datetime
import pandas as pd

# --- 🎯 Page Configuration ---
st.set_page_config(page_title="Weekly Compliance Form", layout="centered")
st.title("📝 Enforcement Officer Weekly Update Form - Restaurant Compliance Tracking")

# --- 🧑 1. Enforcement Officer Information ---
st.header("1. Enforcement Officer Information")
officer_name = st.text_input("Enforcement Officer Name")
officer_id = st.text_input("Enforcement Officer ID")
interview_date = st.date_input("Interview Date", datetime.date.today())
interview_method = st.radio("Interview Method", ["Call", "In-Person", "Other (Specify)"])

# --- 🍽️ 2. Restaurant Information ---
st.header("2. Restaurant Information")
restaurant_id = st.text_input("Restaurant ID")

# --- 📋 3. Formality Status ---
st.header("3. Formality Status (as of the date of this survey)")
formality_status = st.radio("Formality Status", [
    "Unregistered (No record with PRA)",
    "Registered but Not Filing",
    "Registered & Filing"
])

compliance_status = ""
if formality_status == "Registered & Filing":
    compliance_status = st.radio("Compliance Status with PRA", [
        "Active Filer", "Late Filer", "Filing with Errors", "Other (Specify)"
    ])

# --- 🚦 4. Existence & Operational Status ---
st.header("4. Existence & Operational Status")
status_today = st.radio("Status Today", ["Open", "Closed"])
closure_reason = ""
if status_today == "Closed":
    closure_reason = st.radio("If Closed, Reason", ["Temporary Closure", "Permanent Closure", "Relocated", "Unknown"])

# --- Conditional Blocks ---
ur_data = {}
rnf_data = {}
rf_data = {}

# --- 📟 5. For Unregistered Businesses ---
if formality_status == "Unregistered (No record with PRA)":
    st.header("5. For Unregistered Businesses")
    ur_data["LastContact"] = st.date_input("Date of Last Contact with Business", datetime.date.today())
    ur_data["NoticesSent"] = st.radio("Notices Sent (Since Last Survey)", ["Yes", "No"])
    ur_data["NoticeType"] = st.selectbox("Type of Notice", ["Voluntary Compliance", "Advance Notice-CR", "Compulsory Registration", "Other (Specify)"])
    ur_data["OtherContact"] = st.radio("Any Other Contacts with Business?", ["Yes", "No"])
    ur_data["ContactMethod"] = st.multiselect("Nature of Contact", ["Call", "Field Visit", "Email", "In-Person Meeting", "Other (Specify)"])
    ur_data["InteractionSummary"] = st.text_area("Summarize the Interaction with the Business")
    ur_data["ResponseReceived"] = st.radio("Response Received from Business?", ["Yes", "No"])
    ur_data["ResponseDate"] = st.date_input("Date of Response Received", datetime.date.today())
    ur_data["ResponseMethod"] = st.multiselect("Nature of Response", ["Call", "Field Visit", "Letter", "Email", "In-Person Meeting", "Other (Specify)"])
    ur_data["ResponseSummary"] = st.text_area("Summarize Response from Business (if no evidence)")
    ur_data["NextStep"] = st.selectbox("Next Step", ["Send Awareness Material", "Schedule Field Visit", "Issue Notice", "Escalate to Higher Authority", "No Further Action Needed"])
    ur_data["Comments"] = st.text_area("Additional Comments")

# --- 🧳 6. Registered but Not Filing ---
elif formality_status == "Registered but Not Filing":
    st.header("6. For Registered but Not Filing Businesses")
    rnf_data["Filed"] = st.radio("Has the Business Filed since the last survey?", ["Yes", "No"])
    rnf_data["LastContact"] = st.date_input("Date of Last Contact with Business", datetime.date.today())
    rnf_data["NoticesSent"] = st.radio("Notices Sent (Since Last Survey)", ["Yes", "No"])
    rnf_data["NoticeType"] = st.selectbox("Type of Notice", ["Non-Filing Notice", "Non-Filing Penalty", "Other (Specify)"])
    rnf_data["Contact"] = st.multiselect("Nature of Contact", ["Call", "Field Visit", "Email", "In-Person Meeting", "Other (Specify)"])
    rnf_data["Interaction"] = st.text_area("Summarize the Interaction with the Business")
    rnf_data["ResponseReceived"] = st.radio("Response Received from Business?", ["Yes", "No"])
    rnf_data["ResponseDate"] = st.date_input("Date of Response Received", datetime.date.today())
    rnf_data["ResponseMethod"] = st.multiselect("Nature of Response", ["Call", "Field Visit", "Letter", "Email", "In-Person Meeting", "Other (Specify)"])
    rnf_data["ResponseSummary"] = st.text_area("Summarize Response from Business (if no evidence)")
    rnf_data["ReasonNonFiling"] = st.text_input("Reason for Non-Filing (if known)")
    rnf_data["NextStep"] = st.selectbox("Next Step", ["Send Reminder", "Offer Assistance with Filing", "Conduct Field Visit", "Issue Penalty", "Escalate to Higher Authority", "No Further Action Needed"])
    rnf_data["Comments"] = st.text_area("Additional Comments")

# --- 📓 7. For Registered & Filing ---
elif formality_status == "Registered & Filing":
    st.header("7. For Registered & Filing Businesses")
    rf_data["FiledLastMonth"] = st.radio("Has the Tax-Payer Filed within the Last Month?", ["Yes", "No"])
    rf_data["LastContact"] = st.date_input("Date of Last Contact with Business", datetime.date.today())
    
    if rf_data["FiledLastMonth"] == "No" or st.radio("Did Tax Payer File of their own accord?", ["Yes", "No"]) == "No":
        rf_data["NoticesSent"] = st.radio("Notices Sent", ["Yes", "No"])
        rf_data["NoticeType"] = st.selectbox("Type of Notice", ["Non-Filing Notice", "Non-Filing Penalty", "Other (Specify)"])
        rf_data["Contact"] = st.multiselect("Nature of Contact", ["Call", "Field Visit", "Email", "In-Person Meeting", "Other (Specify)"])
        rf_data["Interaction"] = st.text_area("Summarize the Interaction with the Business")
        rf_data["ResponseReceived"] = st.radio("Response Received from Business?", ["Yes", "No"])
        rf_data["ResponseDate"] = st.date_input("Date of Response Received", datetime.date.today())
        rf_data["ResponseMethod"] = st.multiselect("Nature of Response", ["Call", "Field Visit", "Letter", "Email", "In-Person Meeting", "Other (Specify)"])
        rf_data["ResponseSummary"] = st.text_area("Summarize Response from Business (if no evidence)")
    
    rf_data["Comments"] = st.text_area("Additional Comments")

# --- 🧾 Final Surveyor Details ---
st.header("Surveyor Follow-up")
survey_date = st.date_input("Date", datetime.date.today())
survey_followup_required = st.radio("Follow-up Action Required with Enforcement Officers?", ["Yes", "No"])
survey_followup_date = st.date_input("Next Follow-up Date", datetime.date.today())

# --- 💾 Save Entry ---
if st.button("Submit Entry"):
    entry = {
        "OfficerName": officer_name,
        "OfficerID": officer_id,
        "InterviewDate": interview_date,
        "InterviewMethod": interview_method,
        "RestaurantID": restaurant_id,
        "FormalityStatus": formality_status,
        "ComplianceStatus": compliance_status,
        "StatusToday": status_today,
        "ClosureReason": closure_reason,
        "SurveyDate": survey_date,
        "SurveyFollowUp": survey_followup_required,
        "SurveyFollowUpDate": survey_followup_date,
        **{f"UR_{k}": v for k, v in ur_data.items()},
        **{f"RNF_{k}": v for k, v in rnf_data.items()},
        **{f"RF_{k}": v for k, v in rf_data.items()},
    }

    df = pd.DataFrame([entry])
    df.to_csv("weekly_compliance_entries.csv", mode='a', index=False, header=False)
    st.success("✅ Entry submitted and saved!")
