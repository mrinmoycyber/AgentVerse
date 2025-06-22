import requests
from hf_token import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def call_llm(prompt: str):
    """
    Sends a prompt to the Hugging Face text generation model and extracts only the answer.
    """
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.1,
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()

        if isinstance(result, list):
            full_text = result[0]["generated_text"]

            # Return only the text after "Answer:" (if exists)
            if "Answer:" in full_text:
                return full_text.split("Answer:")[-1].strip()
            else:
                return full_text.strip()

        elif isinstance(result, dict) and "error" in result:
            return f"[LLM ERROR] {result['error']}"
        else:
            return "[LLM ERROR] Unexpected format in model response."

    except Exception as e:
        return f"[LLM ERROR] {str(e)}"

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
