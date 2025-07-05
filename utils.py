import google.generativeai as genai
from hf_token import GEMINI_API_KEY  

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash",
    generation_config={
        "temperature": 0.1,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 150,
    }
)

def call_llm(prompt: str):
    
    try:
        response = model.generate_content(prompt)
        full_text = response.text

        # extract only the answer portion if "Answer:" is present
        if "Answer:" in full_text:
            return full_text.split("Answer:")[-1].strip()
        else:
            return full_text.strip().replace("*", "")
    except Exception as e:
        return f"[GEMINI ERROR] {str(e)}"

def get_search_link(query, domain='marvel'):
    """
    Generates a Google search link for the given query restricted to
    Marvel or DC fandom domains.
    """
    base = "https://www.google.com/search?q="
    query = query.replace(" ", "+")
    if domain.lower() == 'marvel':
        return f"{base}site:marvel.fandom.com+{query}"
    elif domain.lower() == 'dc':
        return f"{base}site:dc.fandom.com+{query}"
    else:
        return f"{base}{query}"
