# 🌐 Live Demo

🚀 Hugging Face Deployment:

[Email Intent & Urgency Detector](https://huggingface.co/spaces/ambika6/EMAIL_INTENT_URGENCY_DETECTOR)

````markdown
# 📧 Email Intent & Urgency Detector

An AI-powered Email Classification App built using:

- Streamlit
- LangChain
- Groq LLM
- Pydantic Output Parser

This application analyzes emails and predicts:

✅ Intent  
✅ Urgency  
✅ Tone  

---

# 🚀 Features

- Email Intent Detection
- Urgency Classification
- Tone Analysis
- Beautiful Streamlit UI
- Multiple Test Cases
- Batch Testing Support
- Structured JSON Output using Pydantic
- Groq LLM Integration

---

# 🧠 Intent Categories

- Greeting
- Appreciation
- Complaint
- Request
- Follow-up
- Information

---

# ⚡ Urgency Levels

- Low
- Medium
- High

---

# 🎭 Tone Types

- Friendly
- Polite
- Neutral
- Frustrated
- Urgent

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── model.py
├── parser.py
├── prompt.py
├── config.py
├── requirements.txt
└── README.md
````

---

# 🔧 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ambikaramireddy/EMAIL_INTENT_URGENCY_DETECTOR
```

```bash
cd email-intent-detector
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🌐 Hugging Face Deployment

Upload these files to your Hugging Face Space:

* app.py
* model.py
* parser.py
* prompt.py
* config.py
* requirements.txt

Then add your:

```text
GROQ_API_KEY
```

inside:

## Settings → Repository Secrets

---

# 📦 requirements.txt

```txt
streamlit
langchain
langchain-core
langchain-groq
pydantic
python-dotenv
```

---

# 🧪 Sample Input

```text
Please resolve this issue immediately. The system is down for all users.
```

# ✅ Output



<p align="center">
  <img src="https://github.com/ambikaramireddy/EMAIL_INTENT_URGENCY_DETECTOR/blob/main/Screenshot%202026-05-14%20084108.png?raw=true" width="900">
</p>
```



# 🛠 Technologies Used

* Python
* Streamlit
* LangChain
* Groq API
* Pydantic

---

# 👨‍💻 Author

Made with  by Ambika Ramireddy

---

# ⭐ Future Improvements

* Email Spam Detection
* Sentiment Analysis
* Multi-language Support
* Email Reply Generator
* Dashboard Analytics
* Database Integration

---

# 📜 License

This project is open-source and available under the MIT License.

```
```
