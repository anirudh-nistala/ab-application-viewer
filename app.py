import streamlit as st
import pandas as pd

st.title("AB Application Responses Viewer")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load CSV data
    df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")

    # Ensure "Applicant" column exists
    if "Applicant" not in df.columns:
        st.error("The CSV file must have an 'Applicant' column.")
    else:
        # Select an applicant from the dropdown
        applicant_names = df["Applicant"].unique()
        selected_applicant = st.selectbox("Select an Applicant", applicant_names)

        # Filter responses for the selected applicant
        applicant_data = df[df["Applicant"] == selected_applicant].iloc[0, 1:]  # Exclude 'Applicant' column

        # Display the responses in a structured format
        st.subheader(f"Responses for {selected_applicant}")
        for question, response in applicant_data.items():
            st.markdown(f"**{question}:**")
            st.write(response)
            st.divider()  #

