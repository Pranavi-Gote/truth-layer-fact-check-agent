import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""

    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()

    return text