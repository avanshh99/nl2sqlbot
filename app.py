import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-8b-8192")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

LOG_FILE = "responses.txt"

SCHEMA_CONTEXT = """
You are a helpful assistant that translates natural language into SQL queries.
Here is the database schema:

1. customers:
   - customer_id (Primary Key)
   - registration_date (DATE)
   - city (TEXT)
   - gender (TEXT)

2. orders:
   - order_id (Primary Key)
   - customer_id (Foreign Key to customers.customer_id)
   - order_date (DATE)
   - total_amount (FLOAT)
   - status (TEXT)

3. order_items:
   - item_id (Primary Key)
   - order_id (Foreign Key to orders.order_id)
   - product_name (TEXT)
   - quantity (INTEGER)
   - unit_price (FLOAT)

Return only the SQL query. Do not explain or comment. Assume the user wants the most accurate query possible.
"""

def generate_sql_query(natural_language_query):
    """
    Uses the Groq API to convert a natural language query into an SQL query.
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": SCHEMA_CONTEXT},
            {"role": "user", "content": natural_language_query}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def log_query(natural_language, sql_result):

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"Time: {datetime.now()}\n")
        log.write(f"NL Query: {natural_language.strip()}\n")
        log.write(f"SQL Response:\n{sql_result.strip()}\n")
        log.write("-" * 80 + "\n")


def main():
    print("Natural Language to SQL Translator\n")

    # Predefined test queries
    test_queries = [
        "Count new customers who joined last month.",
        "What is the male to female customer ratio?",
        "Show total sales for each month in 2023.",
        "Which products are most frequently purchased together?",
        "Find orders placed by customers in Mumbai."
    ]

    print("🔹 Running predefined test cases...\n")
    for idx, question in enumerate(test_queries, start=1):
        print(f"Q{idx}: {question}")
        sql = generate_sql_query(question)
        print(f"SQL:\n{sql}\n{'-'*50}")

    #user input
    while True:
        user_query = input("\n Enter your own natural language query (or type 'exit' to quit):\n> ")
        if user_query.lower() in ["exit", "quit"]:
            print("Thank you!")
            break
        sql = generate_sql_query(user_query)
        print(f"\n🧾Generated SQL:\n{sql}\n{'='*50}")
        log_query(user_query, sql)

if __name__ == "__main__":
    main()
