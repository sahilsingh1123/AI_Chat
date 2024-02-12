import streamlit as st
import requests
from dotenv import load_dotenv
import cohere
import os
from openai import OpenAI


load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Define the API endpoints for the chat models
API_ENDPOINTS = {
    'cohere': 'https://api.cohere.ai/generate',
    'openai': 'https://api.openai.com/v1/engines/davinci-codex/completions',
    'bard': 'https://api.bard.com/chat'
}

# Function to call the appropriate chat model API and get a response
def get_chat_model_response(model, prompt):
    headers = {
        # Replace 'your_api_key' with your actual API keys for each service
        'cohere': {'Authorization': 'Bearer your_cohere_api_key'},
        'openai': {'Authorization': f'Bearer {OPENAI_API_KEY}'},
        'bard': {'Authorization': 'Bearer your_bard_api_key'}
    }
    
    data = {
        'cohere': {'prompt': prompt, 'max_tokens': 50},
        'openai': {'prompt': prompt, 'max_tokens': 50},
        'bard': {'prompt': prompt}
    }
    
    response = requests.post(API_ENDPOINTS[model], headers=headers[model], json=data[model])
    print(f"response - {response}")
    if response.status_code == 200:
        # Extract the text response based on the model
        if model == 'cohere':
            return response.json().text
        elif model == 'openai':
            return response.json().choices[0].text
        elif model == 'bard':
            return response.json().message
    else:
        return f"Error: {response.status_code}"

# Streamlit chat interface
def chat_interface():
    st.title("AI Chat Interface")

    # User selects which chat model to use
    model_choice = st.selectbox("Choose a chat model:", options=['cohere', 'openai', 'bard'])
    
    # Chat history is stored in a session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # User inputs their message
    user_message = st.text_input("Enter your message:", key="user_message")

    # Send button is clicked
    if st.button("Send"):
        if user_message:
            # Display the user's message
            st.session_state['chat_history'].append(f"You: {user_message}")
            with st.spinner(f"Waiting for {model_choice} response..."):
                # Get the response from the selected chat model
                response_message = get_chat_model_response(model_choice, user_message)
                # Display the AI's response
                st.session_state['chat_history'].append(f"{model_choice.capitalize()}: {response_message}")
            # Clear the message input box
            # st.session_state.user_message = ""

    # Display the chat history
    for message in st.session_state['chat_history']:
        st.text_area("", value=message, height=35, disabled=True)

def get_cohere_client():
    return cohere.Client(api_key=COHERE_API_KEY)

def get_chatbot_response_bard(message):
    return "bard response not configured at this time"

def get_chatbot_response_openai(message):
    try:
        # Call the OpenAI API
        model = "gpt-3.5-turbo"
        # model = "code-davinci-002"
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ]
        )
        # Parse the response
        return response.choices[0].message
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_chatbot_response_cohere(user_input):
    client = cohere.Client(api_key=COHERE_API_KEY)
    chat_resp = client.chat(
        message=user_input,
        model="command",
        temperature=0.3,
    )

    return chat_resp.text


def chat_interface_2():
    st.title("💬 AI Chat")
    st.caption("🚀 Chatbot Powered by AI")
    model_choice = st.selectbox("Choose a chat model:", options=['cohere', 'openai', 'bard'])
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        if model_choice == "cohere":
            msg = get_chatbot_response_cohere(prompt)
        elif model_choice == "openai":
            msg = get_chatbot_response_openai(prompt)
        elif model_choice == "bard":
            msg = get_chatbot_response_bard(prompt)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)


###########=========================================================================
# start

st.set_page_config(page_title="💬 Night's Watch", page_icon=":robot:", layout="wide")
with st.sidebar:
    st.title("💬 Night's Watch")

chat_interface_2()
# chat_interface()

