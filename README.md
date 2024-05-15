# Gemini-Explorer
<h2> Overview </h2>
Gemini Flight Manager is a comprehensive backend system built using FastAPI, designed for managing and simulating flight-related operations. This system provides a robust platform for handling various aspects of flight management, including flight generation, search, and booking functionalities.

The project leverages FastAPI's efficient and easy-to-use framework to create a high-performance, scalable solution ideal for flight data management. It comes equipped with an SQLite database (<code>flights.db</code>) pre-populated with initial data, allowing for quick deployment and testing.

Key features of Gemini Flight Manager include:
<ul>
<li>Advanced search capabilities to query flights based on criteria like origin, destination, and dates.</li>
<li>Booking system that handles seat availability across different classes and calculates costs accordingly.</li>
</ul>

Designed with extensibility and scalability in mind, Gemini Flight Manager is well-suited for both educational purposes and as a foundation for more complex flight management applications.

**For the purposes of Gemini Function Calling, you will only need <code>search_flights</code> and <code> book_flight </code> functions.

<h2> Installation </h2>
<h3> Prerequisites </h3>
Before you begin, ensure you have the following installed on your system:

<ul>
  <li>Python 3.6 or higher</li>
  <li>FastAPI</li>
  <li>Uvicorn, an ASGI server for FastAPI</li>
</ul>

<h3> Step-by-Step Installation Guide </h3>
<ol>
  <li><h4> Clone the Repository </h4></li>
</ol>
Start by cloning the repository to your local machine. Use the following command:

<br>
```
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

<h2> Set Up a Virtual Environment (Optional but recommended) </h2>
It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have virtualenv installed, create a new environment with:

<br>
```
virtualenv venv
source venv/bin/activate
```
<h2> Install Dependencies </h2>
Inside the virtual environment, install all necessary dependencies by running:

<br>
```
pip install -r requirements.txt
```

<h2> Starting the FastAPI Server </h2>
After the installation, you can start the FastAPI server using Uvicorn. Navigate to the project directory and run:
<br>
```
uvicorn main:app
```
<h2> Accessing the API </h2>
With the server running, you can access the API at <code>http://127.0.0.1:8000</code>.

For interactive API documentation, visit <code>http://127.0.0.1:8000/docs</code>, where you can test the API endpoints directly from your browser.
