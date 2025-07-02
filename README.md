# 🧠 Natural Language to SQL Translator 

This Python tool converts natural language queries into SQL queries using the GROQ API and an example retail database schema. Simply describe your question in plain English and instantly get the corresponding SQL statement!

---

## 🚀 Features

- **Natural Language to SQL:** Converts human language into accurate SQL queries based on your schema.
- **GROQ LLM Integration:** Uses advanced LLMs (e.g., Llama 3) via the GROQ API for reliable translation.
- **Predefined Test Cases:** Includes useful sample queries to get started right away.
- **Interactive CLI:** Enter your own questions, get SQL, and see results instantly in your terminal.
- **Automatic Logging:** All queries and responses are logged to `responses.txt` for your records and debugging.
- **Customizable Schema:** Easily adapt the schema context to your own database structure.

---

## ⚙️ Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Install dependencies:**

   ```bash
   pip install requests python-dotenv
   ```

3. **Set up environment variables:**

   - Copy `.env.example` to `.env`:

     ```bash
     cp .env.example .env
     ```

   - Add your [GROQ API Key](https://console.groq.com/) and (optionally) model name to the `.env` file:

     ```
     GROQ_API_KEY=your_api_key_here
     GROQ_MODEL=llama3-8b-8192  # Or another supported model
     ```

---

## 🛠️ Usage

Run the translator:

```bash
python main.py
```

- The program will run predefined test cases.
- You can then enter your own natural language queries (or type `exit` to quit).

---

## 📝 API and Logging

- **API:** The tool interacts with the [GROQ OpenAI-compatible API](https://console.groq.com/).
- **Schema:** The schema context can be modified in the script for your use case.
- **Logging:** Every query and its SQL response are appended to `responses.txt` with a timestamp for auditing or debugging.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## Built by Avan ❤️

````
