from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


st.set_page_config(page_title="AI-Powered Research Tool", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #1c1c1c;
        color: #f5f5f5;
    }
    .stApp {
        background-color: #1c1c1c;
    }
    .stTextInput > div > div > input {
        background-color: #2b2b2b;
        color: white;
        border: 2px solid #4A90E2;
        border-radius: 12px;
        padding: 10px;
        font-size: 18px;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3b78c4;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color:#2a2a2a;padding:20px;border-radius:15px;">
        <h1 style="color:white;text-align:center;">🔍 LLM Research Assistant</h1>
        <p style="color:#cccccc;text-align:center;">Fast, Smart & Reliable – Powered by Groq</p>
        <p style="color:#888888;text-align:center;">Developed with ❤️ by <strong>Kiran Hayat</strong></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 💬 Enter your research prompt:")
user_input = st.text_input("", placeholder="e.g. Explain RAG in simple terms...")

if st.button("🚀 Ask Now") and user_input:
    try:
    
        llm = ChatGroq(
            temperature=0.7,
            model_name="llama3-8b-8192",  
            api_key=os.getenv("GROQ_API_KEY")
        )

        
        response = llm.invoke(user_input)

       
        st.markdown("### 📘 Response:")
        st.success(response.content if hasattr(response, 'content') else response)

    except Exception as e:
        st.error(f"❌ Error: {e}")
