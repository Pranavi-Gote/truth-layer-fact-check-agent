# Truth Layer — Automated Fact-Checking Agent

## Objective

Truth Layer is a PDF-based fact-checking web app that identifies factual claims and verifies them using structured validation.

The system helps detect outdated, inaccurate, or false statistics commonly found in marketing and business content.

---

## Features

- PDF Upload Interface
- Automatic Claim Extraction
- Detection of:
  - percentages
  - statistics
  - market share
  - financial figures
  - growth metrics
  - user numbers
- Verification Classification:
  - Verified
  - Inaccurate
  - Review Required
- Final Verification Report

---

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- Pandas
- Regex-based claim extraction
- Rule-based verification engine

---

## Deployment

Deployed using Streamlit Cloud

---

## Project Structure

truth-layer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── pdf_reader.py
│   ├── claim_extractor.py
│   ├── verifier.py
│
├── sample_files/
│
└── demo_video.mp4

---

## Demo Example

Sample tested claims:

- India's GDP growth was 9.5% in 2024
- AWS owns 70% cloud market share
- ChatGPT has 500 million daily users

The system successfully flags suspicious claims and generates a structured report.
