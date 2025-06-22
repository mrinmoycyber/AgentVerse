import streamlit as st
from master_agent import process_user_query
from marvel_dataset_agent import answer_question as marvel_dataset_answer
from dc_dataset_agent import answer_question as dc_dataset_answer


st.set_page_config(page_title="Marvel/DC AI Assistant", layout="centered")
st.title("🦸 Marvel/DC Comic Assistant")


mode = st.selectbox(
    "Select Mode:",
    ["AI Assistant (LLM)", "Marvel Dataset", "DC Dataset"]
)


question = st.text_input("Ask your question:")


if st.button("Submit") and question:
    with st.spinner("Thinking..."):
        # LLM AI Assistant via master_agent
        if mode == "AI Assistant (LLM)":
            result = process_user_query(question)

        
        elif mode == "Marvel Dataset":
            result = marvel_dataset_answer(question)

        
        elif mode == "DC Dataset":
            result = dc_dataset_answer(question)

        
        st.markdown(f"### 🔍 Source: {result.get('source', 'N/A')}")
        st.markdown(f"### 💬 Response:\n{result.get('response', 'No answer.')}")

        
        if result.get("search_link"):
            st.markdown(f"[🌐 Google Search Link]({result['search_link']})")
