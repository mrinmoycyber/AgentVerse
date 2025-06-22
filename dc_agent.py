from utils import call_llm

def answer_question(question: str) -> dict:
    """
    Answers the question using the LLM, assuming the context is DC Comics.
    No CSV or character matching used.
    """
    prompt = (
        "You are a helpful assistant with deep expertise in DC comics.\n"
        "Answer the question below truthfully and clearly.\n"
        "Avoid discussing Marvel characters or unrelated topics.\n\n"
        f"User question: {question}\n"
        f"Answer:"
    )

    response = call_llm(prompt)

    return {
        "response": response,
        "source": "Pretrained LLM"
    }
