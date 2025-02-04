# QnAChatbot-Langchain

## Description

QnAChatbot-Langchain is an interactive conversational Q&A chatbot built using **Streamlit** and **LangChain**. The app uses OpenAI's GPT-3.5 to generate human-like responses based on user input. The chatbot is designed to provide clear, friendly, and engaging answers for any questions asked.

## Features

- **Streamlit Interface**: Clean and user-friendly interface to ask questions and get responses.
- **GPT-3.5 Model**: Uses OpenAI’s GPT-3.5 Turbo model to generate answers.
- **Persistent Chat History**: Maintains conversation history for context.
- **Environment Variables**: Loads API keys from a `.env` file for secure access.

## Technologies Used

- **Streamlit**: A Python library to create the interactive user interface for the chatbot.
- **LangChain**: Used for building and orchestrating the logic behind handling user queries with the OpenAI model.
- **OpenAI API**: Utilized to interact with GPT-3.5 for generating natural language responses.
- **RAG (Retrieval-Augmented Generation)**: Although not fully integrated in this version, the app can be extended to include external data retrieval methods alongside language generation.
- **python-dotenv**: Used to securely load the OpenAI API key from a `.env` file.

## Requirements

Before running the project, ensure you have the following:

- Python 3.7+
- An OpenAI API key (for accessing GPT-3.5)

### Install dependencies

```bash
pip install streamlit langchain langchain-community python-dotenv
```

### Environment Setup

Create a `.env` file in the project directory and add your OpenAI API key like this:

```
OPENAI_API_KEY=your-api-key-here
```

## Running the Application

To start the chatbot:

1. Clone the repository or download the script.
2. Make sure you have the required dependencies installed.
3. Run the following command to start the Streamlit app:

```bash
streamlit run chatbot_qa.py
```

This will launch the application, and you can interact with the chatbot via your browser.

## Usage

1. **Ask Questions**: Type your question in the input box and hit "Ask the Question."
2. **Receive Responses**: The chatbot will provide answers based on its trained model.


---

This version includes the technologies used, like LangChain and RAG.
