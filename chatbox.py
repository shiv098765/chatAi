import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv


load_dotenv()



st.title("chat box")
st.write("Gemini 1.5 Flash model")

prompt = st.text_input("Enter your question:")


if st.button("Get Answer"):
    if prompt:
        try:
            
            model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

          
            response = model.invoke([
                HumanMessage(content=prompt)
            ])

           
            st.subheader("AI Answer:")
            st.write(response.content)

        except Exception as e:
            st.error(f" Error: {e}")
    else:
        st.warning(" Please enter a question.")
