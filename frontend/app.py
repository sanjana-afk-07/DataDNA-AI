import streamlit as st
import pandas as pd

from dna_engine.generator import generate_datadna


st.set_page_config(
    page_title="DataDNA AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 DataDNA AI")
st.subheader("Every Dataset Has a Fingerprint")

st.write(
    "Upload a CSV dataset and generate its Data DNA fingerprint."
)

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.write("### 📊 Dataset Preview")
    st.dataframe(df.head())

    temp_file = "uploaded_dataset.csv"
    df.to_csv(temp_file, index=False)

    if st.button("🧬 Generate DataDNA"):

        result = generate_datadna(temp_file)

        st.write("## 🧬 DataDNA Report")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                result["fingerprint"]["rows"]
            )

        with col2:
            st.metric(
                "Columns",
                result["fingerprint"]["columns"]
            )

        with col3:
            st.metric(
                "Missing Values",
                result["quality"]["missing_cells"]
            )

        st.write("### 🔎 Quality")
        st.json(result["quality"])

        st.write("### 🚨 Anomalies")
        st.json(result["anomalies"])

        st.write("### 🧩 Patterns")
        st.json(result["patterns"])

        st.success("🧬 DataDNA generated successfully!")
