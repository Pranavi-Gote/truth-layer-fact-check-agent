import re

def extract_claims(pdf_text):
    claims = []

    lines = pdf_text.split("\n")

    patterns = [
        r"\d+%",                         # percentages
        r"\$\d+",                        # dollar values
        r"\d+\s?(million|billion|crore|lakh)",
        r"\d{4}",                        # years
        r"market share",
        r"growth rate",
        r"revenue",
        r"users",
        r"downloads",
        r"valuation"
    ]

    for line in lines:
        cleaned = line.strip()

        if len(cleaned) < 20:
            continue

        for pattern in patterns:
            if re.search(pattern, cleaned, re.IGNORECASE):
                claims.append(cleaned)
                break

    # remove duplicates
    claims = list(dict.fromkeys(claims))

    return claims[:20]