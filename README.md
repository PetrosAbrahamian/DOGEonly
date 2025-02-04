Federal Spending Data Viewer

📌 Project Overview

Federal Spending Data Viewer is an interactive web application designed to make government spending data accessible and easy to explore. By integrating with the USAspending.gov API, this project allows users to analyze federal spending trends dynamically over selected time ranges.

🔧 Features

Year-Based Filtering: Retrieve federal spending data by selecting a custom range of years.

Search Functionality: Quickly search for recipients, award IDs, or spending amounts.

Pagination: Smooth navigation through large datasets.

Dynamic Data Retrieval: Backend dynamically fetches data from the USAspending.gov API.

Responsive UI: Built using Bootstrap for a clean and accessible interface.

🛠️ Technologies Used

Frontend: HTML, CSS (Bootstrap), JavaScript

Backend: Python (Flask, Flask-CORS, Flask-Caching)

API: USAspending.gov

🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/PetrosAbrahamian/DOGEonly.git
cd DOGEonly

2️⃣ Install Dependencies

Ensure you have Python installed, then run:

pip install flask flask-cors flask-caching requests

3️⃣ Run the Flask Backend

python project7.py

The server will start at http://127.0.0.1:5000.

4️⃣ Open the Frontend

Simply open index.html in your browser or use a local development server.

📊 How It Works

Select a start year and end year using dropdown menus.

Click Fetch Data to retrieve government spending data for the specified range.

Use the search bar to filter results based on keywords.

Navigate through results with pagination controls.

📌 API Usage

The project fetches spending data from the following endpoint:

https://api.usaspending.gov/api/v2/search/spending_by_award/

📎 Future Improvements

Add advanced filtering options (e.g., by agency or spending category).

Enhance UI/UX with interactive charts and graphs.

Store previously queried data in a database for faster access.

🏆 Contributing

This project is open to contributions! Feel free to submit pull requests or report issues.

📬 Contact

For questions or feedback, reach out via GitHub or email.

Note: This project does not include a license and is therefore proprietary. Please contact the repository owner for permission before using or distributing this code.

