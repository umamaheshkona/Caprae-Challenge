import streamlit as st
import pandas as pd
import re
from fuzzywuzzy import fuzz

st.set_page_config(page_title="LeadGen Enhancer", layout="centered")

st.title("🚀 LeadGen Enhancer Tool")
st.markdown("Improve your lead quality with smarter email validation and deduplication.")

st.header("1️⃣ Enter Leads")
uploaded_file = st.file_uploader("Upload CSV with 'Name' and 'Email'", type=["csv"])
df = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.header("2️⃣ Email Validation")
    def is_valid_email(email):
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regex, str(email)))

    df['Valid Email'] = df['Email'].apply(is_valid_email)

    st.header("3️⃣ Deduplication Check (Fuzzy Matching)")
    emails = df['Email'].tolist()
    duplicates = set()

    for i in range(len(emails)):
        for j in range(i + 1, len(emails)):
            if fuzz.ratio(str(emails[i]), str(emails[j])) > 90:
                duplicates.add(emails[j])

    df['Potential Duplicate'] = df['Email'].apply(lambda x: x in duplicates)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Cleaned Leads", data=csv, file_name="cleaned_leads.csv", mime='text/csv')
else:
    st.info("Upload a CSV file to begin.")
