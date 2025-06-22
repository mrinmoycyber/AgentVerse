import pandas as pd
import re
from utils import get_search_link


dc_df = pd.read_csv("dc_cleaned.csv")

def extract_character(question):
    """
    Attempts to extract a DC character name from the question using strict word-based matching.
    """
    question_lower = question.lower()
    question_tokens = set(re.findall(r"\b\w+\b", question_lower))

    for name in dc_df["NAME"].dropna():
        name_lower = name.lower()
        name_tokens = set(re.findall(r"\b\w+\b", name_lower))

        if len(name_tokens & question_tokens) >= 2:
            print(f"🔎 Matched: {name}")
            return name

    return None

def build_csv_response(character_data):
    """
    Formats CSV row information into a response.
    """
    row = character_data.iloc[0]
    return (
        f"🦸 **{row['NAME']}** is a DC character.\n"
        f"- **Alignment:** {row.get('ALIGN', 'Unknown')}\n"
        f"- **Alive:** {row.get('ALIVE', 'Unknown')}\n"
        f"- **First Appearance:** {row.get('FIRST APPEARANCE', 'Unknown')}\n"
        f"- **Comic Appearances:** {row.get('APPEARANCES', 'Unknown')}"
    )

def answer_question(question: str) -> dict:
    """
    Answers using only the DC CSV dataset. No LLM fallback.
    """
    character_name = extract_character(question)

    if character_name:
        matched = dc_df[dc_df["NAME"].str.lower().str.contains(re.escape(character_name.lower()), na=False)]
        if not matched.empty:
            return {
                "response": build_csv_response(matched),
                "source": "DC Dataset"
            }

    # No match: fallback to Google
    return {
        "response": "I couldn't find this character in the DC dataset.",
        "source": "Fallback Search",
        "search_link": get_search_link(question, domain="dc")
    }
