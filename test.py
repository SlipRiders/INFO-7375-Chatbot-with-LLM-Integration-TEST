
import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def validate_algorithm_name(query):
    # validate the algorithm name
    conversation = [
        {"role": "system",
         "content": "You are a knowledgeable assistant well-versed in computer science. Determine if the following is a recognized algorithm, Please respond in English only:"},
        {"role": "user", "content": query}
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50
    )

    # JUDGE THE RESPONSE
    return "yes" in response.choices[0].message.content.lower()

def get_algorithm_description(query):
    # Constructing the chat-like prompt
    conversation = [
        {"role": "system",
         "content": "You are a knowledgeable assistant well-versed in computer science, particularly in algorithms. Answer the code template for the following algorithm(JAVA VERSION), Please respond in English only,Just reply to me with the code, your other words can be written in the form of comments:"},
        {"role": "user", "content": query}
    ]

    # Using the Chat Completion API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=1000
    )
    return response.choices[0].message.content

# set the title of the web app
st.title('ACM Alogorithm Template Query System')

# input the query
user_query = st.text_input("Input your algorithm query here:")

# if the user clicks the button, show the answer
if st.button('Query'):
    if user_query:
        # Validate the algorithm name
        if validate_algorithm_name(user_query):
            # if the algorithm is valid, get the algorithm description
            answer = get_algorithm_description(user_query)
            st.code(answer)  # show the template
        else:
            st.error("Alorithm not found. Please input a valid algorithm name.")
    else:
        st.error("Input a valid algorithm name.")

# restart and clean cache
if st.button('clear cache'):
    st.cache_data.clear()
    st.experimental_rerun()
