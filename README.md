# OpenAI Python App

Exploring OpenAI via Python Package and API Endpoint
Here is a simplified version of the instructions:

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
