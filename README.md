# 🌐 Live Demo

🚀 Hugging Face Deployment:

[Email Intent & Urgency Detector](https://huggingface.co/spaces/ambika6/EMAIL_INTENT_URGENCY_DETECTOR)
## 🚀 Live Demo

Email Intent & Urgency Detector is live here:

https://emailintenturgencydetector-mawt8fdnynmnqrbpvtxduz.streamlit.app/

# 📧 AI Email Intent & Urgency Detector

## 📌 Project Overview

The AI Email Intent & Urgency Detector is a Large Language Model (LLM)-powered application that analyzes email text and classifies it into:

* Intent
* Urgency Level
* Tone

The system is built using:

* Streamlit
* LangChain
* Groq LLM
* Pydantic
* Python

This project demonstrates practical usage of:

* Prompt Engineering
* Structured Output Parsing
* LLM Pipelines
* AI-based Text Classification
* Streamlit Web Application Development

------

# 🧠 Problem Statement

Organizations receive thousands of emails daily.

Manually identifying:

* customer complaints
* urgent issues
* requests
* follow-ups
* appreciation emails

is time-consuming.

This project automates email understanding using Artificial Intelligence and Large Language Models.

---

# 🚀 Features

## ✅ Email Classification

The application classifies emails into:

### Intent Categories

* Request
* Information
* Complaint
* Follow-up
* Greeting
* Appreciation
* Other

### Urgency Levels

* High
* Medium
* Low

### Tone Types

* Urgent
* Neutral
* Polite
* Friendly
* Frustrated
* Formal

---


## ✅ Structured JSON Output

The model returns structured JSON output using Pydantic validation.

---

## ✅ Streamlit User Interface

Provides an interactive web application for users to:

* Enter email text
* Analyze emails
* View results instantly
* Run test cases

---

## ✅ Prompt Engineering

Uses carefully designed prompts to improve:

* Classification accuracy
* Output consistency
* JSON formatting reliability

---

## ✅ Automated Test Cases

Includes predefined test cases to validate model predictions.

---


# 🎯 Objectives

The main objectives of this project are:

* Automate email classification
* Detect urgency level of emails
* Identify email tone
* Build a structured AI pipeline
* Demonstrate prompt engineering concepts
* Create a user-friendly AI application

---

# 🛠️ Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Core programming language           |
| Streamlit  | Frontend web application            |
| LangChain  | LLM pipeline orchestration          |
| Groq       | Fast LLM inference                  |
| Pydantic   | Structured output validation        |
| dotenv     | Secure environment variable loading |

---
![System Architecture](https://raw.githubusercontent.com/ambikaramireddy/EMAIL_INTENT_URGENCY_DETECTOR/main/Screenshot%202026-05-13%20232328.png)

# 📂 Project Structure

```text
email-intent-detector/
│
├── app.py
├── config.py
├── model.py
├── parser.py
├── prompt.py
├── test.py
├── requirements.txt
├── .env
└── README.md
```

---

# 📄 File Explanation

# 1️⃣ app.py

## Purpose

`app.py` is the main frontend application file.

It handles:

* User Interface
* User Input
* Button Actions
* AI Model Invocation
* Result Display
* Test Case Execution

---

## Main Components

### Streamlit UI

Used to create:

* text area
* buttons
* headers
* result sections
* test case display

---

### Email Input

```python
email_input = st.text_area()
```

Allows users to enter email text.

---

### Analyze Button

```python
if st.button("Analyze Email")
```

Triggers the AI analysis pipeline.

---

### LangChain Pipeline

```python
chain = prompt | model | parser
```

This creates the AI workflow:

```text
Prompt → LLM Model → Output Parser
```

---

### Chain Invocation

```python
result = chain.invoke({"text": email_input})
```

Sends the user email to the AI model.

---

### Result Display

Displays:

* Intent
* Urgency
* Tone

---

# 2️⃣ config.py

## Purpose

Stores reusable configuration data.

This improves:

* modularity
* maintainability
* code readability

---

## Contents

### INTENT_CATEGORIES

Stores intent labels and descriptions.

---

### URGENCY_LEVELS

Stores urgency definitions.

---

### TONE_TYPES

Stores tone categories.

---

### TEST_CASES

Contains sample emails and expected outputs.

Used for:

* validation
* testing
* performance checking

---

# 3️⃣ model.py

## Purpose

Responsible for loading the Large Language Model.

---

## Main Components

### load_dotenv()

Loads environment variables securely.

---

### GROQ_API_KEY

API key used to access Groq-hosted models.

---

### ChatGroq

Initializes the Llama 3.1 model.

```python
ChatGroq(
    model="llama-3.1-8b-instant"
)
```

---

## Why Groq?

Groq provides:

* fast inference
* low latency
* efficient LLM execution

---

## temperature=0

```python
temperature=0
```

Used for deterministic outputs.

Important for:

* classification tasks
* consistent results
* reliable JSON generation

---

# 4️⃣ parser.py

## Purpose

Defines structured output validation using Pydantic.

---

## EmailAnalysis Class

Defines output fields:

```python
intent
urgency
tone
```

---

## Why Pydantic?

Pydantic:

* validates model output
* ensures proper JSON structure
* prevents parsing errors
* converts outputs into Python objects

---

## PydanticOutputParser

Automatically parses LLM output into structured format.

---

# 5️⃣ prompt.py

## Purpose

Contains prompt engineering instructions.

This is the most important AI logic file.

---

## Responsibilities

The prompt controls:

* classification logic
* model behavior
* output formatting
* response constraints

---

## Prompt Engineering

The prompt includes:

* classification definitions
* urgency rules
* tone rules
* formatting instructions
* output restrictions
* examples

---

## Why Prompt Engineering is Important?

LLMs depend heavily on instructions.

A better prompt improves:

* accuracy
* consistency
* reliability
* structured output quality

---

## Output Rules

The model is forced to:

* return valid JSON
* avoid explanations
* avoid markdown
* follow strict formatting

---

# 6️⃣ test.py

## Purpose

Used to validate model performance.

---

## Responsibilities

* Runs predefined test cases
* Compares expected outputs
* Displays pass/fail results

---

## Why Testing is Important?

Testing ensures:

* model reliability
* consistency
* classification correctness

---

# 🔄 Application Workflow

```text
User Enters Email
        ↓
Streamlit Receives Input
        ↓
Prompt Template Created
        ↓
LangChain Pipeline Executes
        ↓
Groq LLM Analyzes Email
        ↓
Pydantic Parses Output
        ↓
Results Displayed to User
```

---

# 📊 Sample Input and Output

## Input Email

```text
Please resolve this issue immediately. The server is down.
```

---

## Output

```json
{
    "intent": "Request",
    "urgency": "High",
    "tone": "Urgent"
}
```

---

# 🧪 Example Test Cases

| Email Type         | Expected Intent |
| ------------------ | --------------- |
| Complaint Email    | Complaint       |
| Greeting Email     | Greeting        |
| Thank You Email    | Appreciation    |
| Recruitment Update | Information     |
| Follow-up Email    | Follow-up       |

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2: Navigate to Project Folder

```bash
cd email-intent-detector
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Add:

```env
GROQ_API_KEY=your_api_key
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

---

# 🧪 Running Tests

```bash
python test.py
```

---

# 📌 Advantages of the Project

* Automates email understanding
* Reduces manual effort
* Demonstrates practical AI usage
* Shows prompt engineering concepts
* Uses structured LLM outputs
* Beginner-friendly architecture

---

# 🚧 Future Improvements

Future enhancements may include:

* Spam Detection
* Email Summarization
* Sentiment Analysis
* Confidence Scores
* Multi-language Support
* CSV Bulk Email Analysis
* Dashboard Analytics
* Database Integration

---

# 🎓 Learning Outcomes

This project helped in understanding:

* Large Language Models
* Prompt Engineering
* LangChain Pipelines
* Streamlit Development
* Structured Output Parsing
* AI Workflow Design
* API Integration
* Automated Testing

---

# 📷 Screenshots

Add screenshots of:

* Main UI
* Email Analysis Result
* Test Case Execution
* Streamlit Dashboard

---

# 👨‍💻 Author

Ambika Ramireddy

---

# 📜 License

This project is developed for educational and learning purposes.

---

# ⭐ Conclusion

The AI Email Intent & Urgency Detector demonstrates how Large Language Models can be used to automate email understanding tasks.

The project combines:

* Prompt Engineering
* LLM Integration
* Structured Output Parsing
* Web Application Development

into a complete AI-powered application.
