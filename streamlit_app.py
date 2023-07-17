# import libraries\
import os # for getenv
import streamlit as st # framework for front end app user-interaction
from langchain.llms import OpenAI #framework for working w/ LLM models

# pip install python-dotenv (For getenv)
from dotenv import load_dotenv
load_dotenv()

# ! Troubleshooting with missing LLM model:
# https://python.langchain.com/docs/get_started/installation
# https://python.langchain.com/docs/modules/model_io/models/llms/

# display title
st.title("Kristy Leigh's OpenAI API")
st.write('''This is an app created using Streamlit, Langchain and OpenAI LLM. Thank you to WADSIH for sponsoring my OpenAI API Token.''')

# take OPENAI secret API key from variable
openai_api_key = os.getenv("OPENAI_API_KEY")
# st.write(f"openai_api_key: {openai_api_key}") # find where the key is saved

def env_or_input(openai_api_key):
    '''
    This function: 
    * determines if the user has entered an API key in their environment
    * provides an input field to enter the key if it isn't saved locally
    * returns the value of the api key

    Sidebar: renders a side section for the input

    '''

    if openai_api_key:
        st.sidebar.write("Thank you for setting your OpenAI in your environment")
    else:
        openai_api_key = st.sidebar.text_input('OpenAI API Key')
    return openai_api_key

    # if not openai_api_key:
    #     st.write("Option 2: Enter your OpenAI API Key below")
    #     openai_api_key_input = st.sidebar.text_input('OpenAI API Key')
    #     openai_api_key=openai_api_key_input
    # else:
    #     st.write("Thank you for setting your OpenAI in your environment")
    #     openai_api_key=openai_api_key

openai_api_key = env_or_input(openai_api_key)

def generate_response(input_text):

    '''
    This function accesses OpenAI module, sets the temperature and sends the api key to OpenAI for authentication.

    Temperature: 0.7 is the default, 0.0 is the most conservative, 1.0 is the most creative

    '''

    llm = OpenAI(
        temperature=0.7,
        openai_api_key=openai_api_key
    )
    
    # create a box to display output of text from the LLM model
    ai_response = llm(input_text)

    st.write("Ms-KL Bot: ")
    st.info(
        ai_response
    )

st.title("Ms-KL Bot")

# create a form for submission
with st.form("kristy's_form"):
    # create a text area for submitting a question.
    # st.form to create a text box (st.text_area) for user to enter prompt input.
    # user click submit - it will call the generate_response function using the input text.
    
    # check for the openAI key and warn user if there isn't one available
    # if not openai_api_key.startswith('sk-'):
    if not openai_api_key:
        st.warning('Please enter your OpenAI API Key on the left, or save your API Key to your .env file', icon='⚠')
    text = st.text_area('User:', 'When was Walt Disney born?')

    # create a submit button called "submit your question kristy"
    # when the button is pressed, it is set to submitted
    submitted = st.form_submit_button('Submit your Question Kristy')

    # if the button is pressed and the api key exists, return response
    # if submitted and openai_api_key.startswith('sk-'):
    if submitted and openai_api_key:
        generate_response(text)
