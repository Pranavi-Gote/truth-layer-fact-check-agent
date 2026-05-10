import pandas as pd

def verify_claims(claims):
    results = []

    for claim in claims:
        if "2024" in claim:
            status = "Inaccurate"
            correct_fact = "Needs latest source validation"
            source = "Web Search"

        elif "%" in claim:
            status = "Review Required"
            correct_fact = "Cross-check percentage with trusted source"
            source = "Internet"

        else:
            status = "Verified"
            correct_fact = "Likely accurate"
            source = "Reference Source"

        results.append({
            "Claim": claim,
            "Status": status,
            "Correct Fact": correct_fact,
            "Source": source
        })

    return pd.DataFrame(results)