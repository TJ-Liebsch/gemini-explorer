import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
from vertexai.preview.language_models import TextGenerationModel
import time

# Set up VERTEXAI
PROJECT_ID = "sample-gemini-423220"
LOCATION = "us-central1"
client = vertexai.init(project = PROJECT_ID, location=LOCATION)

config = generative_models.GenerationConfig(
    temperature=0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)

chat = model.start_chat()

# helper function to display streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    # Uncomment if you want a good format
    # Potentially switch assistant to model if assistant is too weak
    # with st.chat_message("assistant"):
    #     # st.markdown(output)

    # Uncomment if you want a typewriter effect
    # Displays response in chat message container
    with st.chat_message("assistant"):
        # Speed of the typewriter
        speed = 15

        # Tpewriter program but it ruins the formating
        tokens = response.text.split()
        container = st.empty()
        for index in range(len(tokens) + 1):
            curr_full_text = " ".join(tokens[:index])
            container.markdown(curr_full_text)
            time.sleep(1 / speed)
        
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": output
        }
    )

# Streamlit title
st.title('Gemini Explorer')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Enumerates though all the messages
for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],
            parts = [ Part.from_text(message["content"]) ]
        )
    # prevents seeing the first question
    if index != 0:
        # prints the history
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Appends the content to history for each message
    chat.history.append(content)

# If it is the start of the chat then Rex introduces himself
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive. You also should try to learn the user's name, remember it, and use it."
    llm_function(chat, initial_prompt)

# For captureing user input
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)