🏛️ Federal Spending Explorer

📌 Project Overview

Federal Spending Explorer is an interactive web application that allows users to explore U.S. government spending data. Users can filter spending data by year, search for specific recipients, and navigate through paginated results. The project utilizes data from USAspending.gov and is fully deployed on Render.


🌐 Live Demo

Frontend (User Interface): https://dogeonly-1.onrender.com
(Data may initially take some time to load)

Backend API: https://dogeonly.onrender.com


🚀 Features

✅ Search federal spending by award ID, recipient name, or amount✅ Filter spending by year range✅ Paginated results for easy navigation✅ Fast API response with caching enabled✅ Fully deployed frontend and backend on Render✅ Calculates total amounts awarded to recipients (even across multiple years)


🛠️ Tech Stack


Frontend:

HTML, CSS, Bootstrap

JavaScript (Fetch API for API requests)

Hosted on Render (Static Site)


Backend:

Python, Flask

Flask-CORS (Cross-Origin Resource Sharing)

Flask-Caching (Performance optimization)

Hosted on Render (Web Service)

Data Source:

USAspending.gov API (Official U.S. government spending data)


⚡ How to Run Locally


If you want to run this project on your local machine:


1️⃣ Clone the Repository

git clone https://github.com/PetrosAbrahamian/DOGEonly.git
cd DOGEonly


2️⃣ Set Up the Backend


Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate  # (Mac/Linux)
.venv\Scripts\activate    # (Windows)

Install Dependencies

pip install -r requirements.txt

Run Flask Backend

python project7.py

Your backend should now be running at http://127.0.0.1:10000


3️⃣ Set Up the Frontend


Simply open index.html in a browser or use Live Server (VS Code Extension).


📡 API Endpoints


1️⃣ Get Federal Spending Data


Endpoint: /api/spending

Method: GET

Query Parameters:

start_year → (Default: 2022)

end_year → (Default: 2022)

query → (Optional: Search by award ID, recipient, or amount)

page → (Pagination, default: 1)

Example Request:

https://dogeonly.onrender.com/api/spending?start_year=2022&end_year=2022&page=1&query=Lockheed

Example Response:

{
  "results": [
    {
      "Award ID": "HT940216C0001",
      "Recipient Name": "HUMANA GOVERNMENT BUSINESS INC",
      "Award Amount": 49773209628.4
    }
  ]
}

Note About Totals:

The total award amount displayed for each recipient represents the cumulative funding they have received for the specific award ID.

Changing the year range does not alter the total amount shown if the recipient received funds across those years. For example, HUMANA GOVERNMENT BUSINESS INC shows the same total amount for 2022 and 2017 if the award spans multiple years.


🚀 How This Can Be Useful for DOGE

This project provides a structured way to explore and analyze federal spending data, which can be useful for organizations like DOGE in several ways:

Government Contract & Grant Analysis

DOGE (or similar organizations) can track which companies are receiving large government contracts.

This helps in identifying key players in specific industries and who controls major federal funding.

Financial Transparency & Accountability

By making government spending more accessible and user-friendly, this tool helps in identifying patterns in where taxpayer money is going.

If DOGE is involved in policy discussions or government analysis, this tool provides a quick way to pull spending trends.

Customizable for Future Use

Since this is an open-source project, DOGE can modify or extend it to add deeper analytics, generate reports, or visualize spending patterns with charts.

It could be upgraded with AI-powered insights to predict future spending trends based on historical data.


💡 Future Improvements

While this project demonstrates key concepts and skills, it is not a polished production-level application. Some of its limitations include:

User Interface (UI):

The UI is functional but not visually appealing or modern. It lacks advanced styling and user-friendly animations often found in polished applications.

Performance:

The app may not handle large datasets or high user traffic efficiently. Optimizations for speed and scalability could be added.

Limited Features:

The tool is limited to basic search and filter functionality. Advanced analytics or visualizations (e.g., charts, graphs) are not yet implemented.

Design:

The frontend design is simplistic and could benefit from improvements in layout, responsiveness, and overall aesthetic appeal.

Error Handling:

The app could have more robust error messages and handling for edge cases, such as invalid API responses or user input.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Petros Abrahamian🚀 GitHub: @PetrosAbrahamian

🤖 AI Assistance

This project was developed with AI assistance for debugging, deployment guidance, and documentation improvements.

