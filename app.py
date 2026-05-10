import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.claim_extractor import extract_claims
from utils.verifier import verify_claims

st.set_page_config(page_title="Truth Layer", layout="wide")

st.title("Truth Layer — Automated Fact-Checking Agent")
st.write("Upload a PDF and verify claims using live web data")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF uploaded successfully!")

    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Extracting claims..."):
        claims = extract_claims(pdf_text)

    st.subheader("Extracted Claims")
    for claim in claims:
        st.write("-", claim)

    if st.button("Verify Claims"):
        with st.spinner("Fact-checking in progress..."):
            results = verify_claims(claims)

        st.subheader("Verification Report")
        st.dataframe(results)