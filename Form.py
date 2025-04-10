# --- 📦 Required Libraries ---
# You can install these using pip
# pip install streamlit pandas

import streamlit as st
import datetime
import pandas as pd

# --- 🎯 Page Configuration ---
st.set_page_config(page_title="Weekly Compliance Form", layout="centered")
st.title("📝 Enforcement Officer Weekly Compliance Form")

# --- 🧑 Section 1: Officer Information ---
st.header("1. Officer Information")
officer_name = st.text_input("Officer Name")
officer_id = st.text_input("Officer ID")
interview_date = st.date_input("Interview Date", datetime.date.today())
interview_method = st.selectbox("Interview Method", ["Call", "In-Person", "Other"])

# --- 🍽️ Section 2: Restaurant Information ---
st.header("2. Restaurant Information")
restaurant_id = st.text_input("Restaurant ID")

# --- ✅ Section 3: Compliance Status ---
st.header("3. Compliance & Operational Status")
formality_status = st.selectbox("Formality Status", [
    "Unregistered", 
    "Registered but Not Filing", 
    "Registered & Filing"
])

status_today = st.selectbox("Status Today", ["Open", "Closed"])
closure_reason = ""
if status_today == "Closed":
    closure_reason = st.radio("Reason for Closure", [
        "Temporary Closure", "Permanent Closure", "Relocated", "Unknown"
    ])

# --- 📞 Section 4: Contact & Notice Tracking ---
st.header("4. Contact & Notice Follow-Up")
last_contact_date = st.date_input("Date of Last Contact", datetime.date.today())
notices_sent = st.radio("Notices Sent Since Last Survey", ["Yes", "No"])
notice_type = st.selectbox("Type of Notice", [
    "Voluntary Compliance", "Advance Notice-CR", 
    "Compulsory Registration", "Other"
])
other_contact = st.radio("Any Other Contact?", ["Yes", "No"])
contact_method = st.multiselect("Nature of Contact", [
    "Call", "Field Visit", "Email", "In-Person Meeting", "Other"
])
interaction_summary = st.text_area("Summarize Interaction with the Business")
response_received = st.radio("Response Received from Business?", ["Yes", "No"])
response_date = st.date_input("Date of Response", datetime.date.today())
response_method = st.multiselect("Nature of Response", [
    "Call", "Field Visit", "Letter", "Email", "In-Person Meeting", "Other"
])
response_summary = st.text_area("Summarize Response")
next_step = st.selectbox("Next Step", [
    "Send Awareness Material", "Schedule Field Visit", "Issue Notice",
    "Escalate to Higher Authority", "No Further Action Needed"
])
comments = st.text_area("Additional Comments")

# --- 💾 Save Data (In-Memory/CSV for now) ---
if st.button("Submit Entry"):
    entry = {
        "OfficerName": officer_name,
        "OfficerID": officer_id,
        "InterviewDate": interview_date,
        "InterviewMethod": interview_method,
        "RestaurantID": restaurant_id,
        "FormalityStatus": formality_status,
        "StatusToday": status_today,
        "ClosureReason": closure_reason,
        "LastContactDate": last_contact_date,
        "NoticesSent": notices_sent,
        "NoticeType": notice_type,
        "OtherContact": other_contact,
        "ContactMethod": ", ".join(contact_method),
        "InteractionSummary": interaction_summary,
        "ResponseReceived": response_received,
        "ResponseDate": response_date,
        "ResponseMethod": ", ".join(response_method),
        "ResponseSummary": response_summary,
        "NextStep": next_step,
        "Comments": comments
    }
    df = pd.DataFrame([entry])
    df.to_csv("weekly_compliance_entries.csv", mode='a', index=False, header=False)
    st.success("✅ Entry submitted and saved!")
