# MES Chatbot

This repository contains code for a MES (Manufacturing Execution System) chatbot application built using Flask API and Streamlit.

## Overview

The MES Chatbot is a web-based application that allows users to interact with a chatbot interface to ask questions related to manufacturing processes, production data, and other relevant information. The chatbot utilizes a pre-trained language model to understand user queries and provide informative responses.

The application consists of two main components:

1. **Flask API (flask_api_2.py):**
   - This component serves as the backend API for the chatbot.
   - It provides endpoints for receiving user queries, processing them, and returning appropriate responses.
   - The Flask API integrates with a pre-trained language model and invokes it to generate responses to user queries.

2. **Streamlit Client (mes_client_2.py):**
   - This component serves as the frontend interface for the chatbot.
   - It is built using Streamlit, a Python library for building interactive web applications.
   - The Streamlit client provides a text input field where users can enter their questions and receive responses from the chatbot in real-time.
   - It communicates with the Flask API to send user queries and receive responses asynchronously.

## Setup Instructions

To run the MES Chatbot application, follow these steps:

1. **Clone the Repository:**
git clone https://github.com/your-username/mes-chatbot.git
cd mes-chatbot

2. **Install Dependencies:**
   pip install -r requirements.txt
   
3. **Run the Flask API:**
   python flask_api_2.py

4. **Run the Streamlit Client:**
- Open a new terminal window.
- run the following command: streamlit run mes_client_2.py
  5. **Interact with the Chatbot:**
- Once both the Flask API and Streamlit client are running, you can interact with the MES Chatbot by entering your questions in the text input field provided by the Streamlit client.

## Directory Structure

- **flask_api_2.py:** Flask application script containing the backend API logic.
- **mes_client_2.py:** Streamlit application script containing the frontend client interface.
- **Config.env:** Environment configuration file containing environment variables used by the application.
- **requirements.txt:** File containing the Python dependencies required by the application.
- **README.md:** This file providing an overview of the MES Chatbot application and setup instructions.


