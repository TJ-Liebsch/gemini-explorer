# Gemini-Explorer
<h2> Overview </h2>
Gemini Flight Manager is a comprehensive backend system built using FastAPI, designed for managing and simulating flight-related operations. This system provides a robust platform for handling various aspects of flight management, including flight generation, search, and booking functionalities.

The project leverages FastAPI's efficient and easy-to-use framework to create a high-performance, scalable solution ideal for flight data management. It comes equipped with an SQLite database (<code>flights.db</code>) pre-populated with initial data, allowing for quick deployment and testing.

Key features of Gemini Flight Manager include:

Advanced search capabilities to query flights based on criteria like origin, destination, and dates.
Booking system that handles seat availability across different classes and calculates costs accordingly.
Designed with extensibility and scalability in mind, Gemini Flight Manager is well-suited for both educational purposes and as a foundation for more complex flight management applications.

**For the purposes of Gemini Function Calling, you will only need search_flights and book_flight functions.

<h2> Installation </h2>
<h3> Prerequisites </h3>
Before you begin, ensure you have the following installed on your system:

Python 3.6 or higher
FastAPI
Uvicorn, an ASGI server for FastAPI
<h3> Step-by-Step Installation Guide </h3>
<h4> Clone the Repository </h4>

Start by cloning the repository to your local machine. Use the following command:

git clone https://github.com/your-username/your-repository.git
cd your-repository

<h3> Set Up a Virtual Environment (Optional but recommended) </h3>
It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have virtualenv installed, create a new environment with:

virtualenv venv
source venv/bin/activate
<h3> Install Dependencies </h3>
Inside the virtual environment, install all necessary dependencies by running:

pip install -r requirements.txt

<h3> Starting the FastAPI Server </h3>
After the installation, you can start the FastAPI server using Uvicorn. Navigate to the project directory and run:

uvicorn main:app
<h3> Accessing the API </h3>
With the server running, you can access the API at http://127.0.0.1:8000.

For interactive API documentation, visit http://127.0.0.1:8000/docs, where you can test the API endpoints directly from your browser.
