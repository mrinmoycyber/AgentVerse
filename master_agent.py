import re
from utils import call_llm, get_search_link
import marvel_agent, dc_agent

def detect_universe_llm(question: str) -> str:
    prompt = (
        "You are an expert comic-book classifier.\n"
        "Read the user question below and reply with **exactly one word**:\n"
        "  marvel   → if the question is about a Marvel character, place, or event.\n"
        "  dc       → if it is about a DC character, place, or event.\n"
        "  unknown  → if you are not sure.\n\n"
        f"Question: {question}\n"
        "One-word answer:"
    )
    raw = call_llm(prompt).strip().lower()

    # Clean up common noise
    if "marvel" in raw:
        return "marvel"
    elif "dc" in raw:
        return "dc"
    elif "unknown" in raw:
        return "unknown"
    else:
        return "unknown"


def process_user_query(question: str) -> dict:
    universe = detect_universe_llm(question)

    if universe == "marvel":
        result = marvel_agent.answer_question(question)
    elif universe == "dc":
        result = dc_agent.answer_question(question)
    else:
        return {
            "response": "I’m not sure whether this is Marvel or DC related.",
            "source":   "Unknown",
            "search_link": get_search_link(question)
        }


    if result.get("source") == "Pretrained LLM":
        result["search_link"] = get_search_link(question, domain=universe)

    return result

