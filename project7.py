from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_caching import Cache
import requests

app = Flask(__name__)

# ✅ Allow CORS for local frontend
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

# Configure caching
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300})

@app.route('/')
def home():
    return "<h1>Federal Spending API</h1><p>Try accessing <a href='/api/spending'>/api/spending</a></p>"

@app.route('/api/spending', methods=['GET'])
@cache.cached(query_string=True)
def get_spending():
    try:
        # Extract parameters from the request
        start_year = request.args.get('start_year', '2022')
        end_year = request.args.get('end_year', '2022')
        query = request.args.get('query', '').lower()  # For search functionality
        page = request.args.get('page', 1, type=int)

        print(f"Fetching data for {start_year}-{end_year}, page {page}, query: {query}")  # Debugging

        url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
        payload = {
            "filters": {
                "award_type_codes": ["A", "B", "C", "D"],
                "time_period": [
                    {"start_date": f"{start_year}-01-01", "end_date": f"{end_year}-12-31"}
                ]
            },
            "fields": ["Award ID", "Recipient Name", "Award Amount"],
            "limit": 100,
            "page": page,
            "sort": "Award Amount",
            "order": "desc"
        }

        print("📌 Payload Sent to API:", payload)  # Debugging

        # Send request to the external API
        response = requests.post(url, json=payload)
        print("📌 Raw API Response Status:", response.status_code)

        if response.status_code != 200:
            print("API Error:", response.text)
            return jsonify({"error": f"API returned status {response.status_code}"}), response.status_code

        # Get raw data
        data = response.json()
        print("📌 Raw Data from API:", data)  # Debugging API response

        # Apply query filtering if query is provided
        if query:
            filtered_results = [
                item for item in data.get('results', [])
                if query in item["Recipient Name"].lower()
                or query in item["Award ID"].lower()
                or query in str(item["Award Amount"]).lower()
            ]
            data['results'] = filtered_results

        # Return filtered or original data to the frontend
        return jsonify(data)

    except Exception as e:
        print("Error:", str(e))  # Debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
