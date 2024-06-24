
import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to validate the algorithm name
def validate_algorithm_name(query):
    conversation = [
        {"role": "system",
         "content": "You are a knowledgeable assistant well-versed in computer science. Determine if the following is a recognized algorithm, Please respond in English only:"},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50
    )
    
    return "yes" in response.choices[0].message['content'].lower()

# Function to get the algorithm description
def get_algorithm_description(query):
    conversation = [
        {"role": "system",
         "content": "You are a knowledgeable assistant well-versed in computer science, particularly in algorithms. Answer the code template for the following algorithm (JAVA VERSION). Please respond in English only, just reply to me with the code, your other words can be written in the form of comments:"},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=1000
    )
    
    return response.choices[0].message['content']

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set the title of the web app
st.title('ACM Algorithm Template Query System')

# Input the query
user_query = st.text_input("Input your algorithm query here:")

# If the user clicks the button, show the answer
if st.button('Query'):
    if user_query:
        # Validate the algorithm name
        if validate_algorithm_name(user_query):
            # If the algorithm is valid, get the algorithm description
            answer = get_algorithm_description(user_query)
            st.session_state.messages.append({"role": "user", "content": user_query})
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.session_state.messages.append({"role": "user", "content": user_query})
            st.session_state.messages.append({"role": "assistant", "content": "Algorithm not found. Please input a valid algorithm name."})
    else:
        st.error("Input a valid algorithm name.")

# Display the chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.text_area("User", message["content"], height=100, max_chars=None, disabled=True)
    else:
        st.code(message["content"])

# Restart and clean cache
if st.button('Clear Cache'):
    st.session_state.messages = []
    st.experimental_rerun()
