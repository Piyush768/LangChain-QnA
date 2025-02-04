import streamlit as st
import os
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI  # Updated import

# ✅ Load environment variables
load_dotenv()

# ✅ Ensure API key is loaded correctly
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OpenAI API Key is missing! Check your .env file and restart the script.")
    st.stop()

print("🔍 Debugging: API Key Loaded -", api_key[:10] + "..." + api_key[-5:])  # Masked for security

# ✅ Initialize OpenAI chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, max_tokens=500)

# ✅ Streamlit UI Setup
st.set_page_config(page_title="Conversational Q&A Chatbot", page_icon="🤖")
st.title("🗨️ Conversational Q&A Chatbot")

# ✅ Initialize chat history in session_state
if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"] = [
        SystemMessage(content="You are a helpful AI assistant. Provide clear, friendly, and engaging responses!")
    ]

## 🔹 Function to get OpenAI response
def get_chatmodel_response(question):
    """Handles user questions and returns OpenAI-generated answers."""
    if not question.strip():  # Prevent empty inputs
        return "⚠️ Please enter a valid question."

    st.session_state["flowmessages"].append(HumanMessage(content=question))

    try:
        answer = llm.invoke(st.session_state["flowmessages"])  # ✅ Corrected invocation method
        st.session_state["flowmessages"].append(AIMessage(content=answer.content))
        return answer.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ✅ Text input for user query
question = st.text_input("💬 Ask me anything:")

# ✅ Submit button
if st.button("🚀 Ask the Question"):
    response = get_chatmodel_response(question)

    if response:
        st.subheader("💡 The Response is:")
        st.write(response)
