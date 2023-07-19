# Streamlit OpenAI Python App

Exploring OpenAI via Python Packages (Streamlit, Langchain, OpenAI) and API Endpoint

- See: [Streamlit OpenAI Python App](/streamlit_app.py) & [OpenAI App Jupyter Notebook](/openai_python.ipynb)

![image](https://github.com/Ms-KL/openai-python-app/assets/92511648/dde36356-4782-4ca3-aebf-52483743699f)

## Goals:

- ✅ create appropriate environments for Jupyter Notebook and app(s)
- ✅ create OpenAI interactive bot script using Jupyter Notebooks
- ✅ create simple Streamlit / Langchain / OpenAI App taking text and OpenAI App Key as input
- ✅ embed .env variable for openai_api_key and incorporate check for env versus user input in app
- add ability to upload document & ask questions on data
- build on app to incorporate career history:
  - pre-defined personal context: my resume, linkedin and github readme
  - set prompt for users to ask questions regarding my personal data

## Resources:

- [How to use ChatGPT API Python for Beginners - Full ChatBOT Tutorial](https://www.youtube.com/watch?v=Vurdg6yrPL8&list=PLpdmBGJ6ELUIYHjmzYTuePlNRf7yeCACz)
- [Build an LLM Powered App with Langchain, Streamlit & OpenAI](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/)
- [OpenAI Documentation - API Reference](https://platform.openai.com/docs/api-reference/introduction)

## Create a Python environment

### Using Anaconda (for Jupyter Notebook):

1. Open the Anaconda PowerShell prompt.
2. Create a new environment with Python 3.9: `conda create --name envpy39 python=3.9`
3. Activate the environment: `conda activate envpy39`
4. Install required packages: `pip install -q openai python-dotenv notebook`

### Using venv (for .py files):

1. Open a terminal or command prompt.
2. Navigate to your project directory: `cd <path>`
3. Create a new virtual environment: `python -m venv venv`
4. Activate the environment:
   - On Windows (PowerShell): `.\venv\Scripts\Activate`
   - On macOS/Linux (bash): `source venv/bin/activate`
   5. Install required packages: `pip install streamlit openai langchain langchain[llms]` or `pip install -r requirements.txt` or `python -m pip install langchain streamlit openai`
      - [langchain llm troubleshooting](https://www.reddit.com/r/LangChain/comments/143c2ny/comment/jnago5c/?utm_source=share&utm_medium=web2x&context=3) • [also this](https://python.langchain.com/docs/modules/model_io/models/llms/)

### Check versions of packages installed in environment:

- `pip list --user` (specific packages I installed)
- `pip list` (all packages installed)

## Run the project

### Jupyter Notebook:

1. Open the Anaconda PowerShell prompt.
2. Navigate to your project directory: `cd <path>`
3. Activate the environment: `conda activate envpy39`
4. Start Jupyter Notebook: `jupyter notebook`

### .py files:

1. Open a terminal or command prompt.
2. Navigate to your project directory: `cd <path>`
3. Activate the environment:
   - On Windows (PowerShell): `.\venv\Scripts\Activate`
   - On macOS/Linux (bash): `source venv/bin/activate`
4. Run the server using Framework:
   - DRF: `python manage.py runserver`
   - Streamlit: `streamlit run <projectname.py>` view: http://localhost:8501/

## Set your OpenAI API Key:

Don't have an OpenAI API Key? [Get one here](https://platform.openai.com/account/api-keys).

### Save to your environment:

1. Create a file called: `.env`
2. Enter the following: `OPENAI_API_KEY = <yourkeyhere>`

### Enter in the App:

1. Run the app
2. Enter the OpenAI API Key in the window to the left

<br>

---

# ChatGPT with PDF Data (Langchain)

See: [Jupyter Notebook: ChatGPT with PDF Data](/chatgpt_with_pdf_app.ipynb)

## How it works:

- take pdf as input
- break into smaller pieces (chunks <=512 tokens)
  - allows receiving smaller responses based on queries
- take chunks and embed one by one (1536 dimension vectors ADA-002)
- put each chunk/embedding into vector db (FAISS) -> ready for recall when user queries
- allow user to query database
  - take in user query
  - put through embedding model
  - get back number of matched docs/embeddings
  - parse through LLM (GPT3.5)
  - send answer back to user

## Note:

- need to upload documents to reports folder

## Resources:

- [Youtube](https://youtu.be/au2WVVGUvc8)
