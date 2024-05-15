# Gemini Explorer

## Overview

Gemini Explorer is a AI chatbot built using vertexai, streamlit, and google cloud platform. This chatbot is capable of learning from the users and is able to answer various complex questions. The project utilizes streamlit's UI capablities to easily present the chatbox for the user to interact with.

Key features of Gemini Explorer include:
- An AI that can learn from the user.
- A UI to interact with this AI.

The API key I have expires with-in 90 days of 5/13/2024, so if you couldn't run it on your own here is a short video of me running it when I still had the API key:

## Installation

### Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.6 or higher

### Step-by-Step Installation Guide

1. **Clone the Repository**
   
   Start by cloning the repository to your local machine. Use the following command:
   ```bash
   git clone https://github.com/TJ-Liebsch/gemini-explorer.git
   cd gemini-explorer

## Set Up a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have `virtualenv` installed, create a new environment with:

```bash
virtualenv venv
source venv/bin/activate
```

## Install Dependencies
Inside the virtual environment, install all necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## Accessing the Chatbot
Inside the virtual environment, run the program with this command
```bash
streamlit run geminiExplorer.py
```
