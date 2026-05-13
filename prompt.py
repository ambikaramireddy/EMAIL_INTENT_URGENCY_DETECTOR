
from langchain_core.prompts import PromptTemplate

template = """
You are an email analysis assistant.

Your task is to analyze the given email text strictly based on the content provided.
Do not assume any external context.

You must classify the email into:

1. intent
2. urgency
3. tone

Allowed Values:

Intent:
- Request
- Information
- Complaint
- Follow-up
- Greeting
- Appreciation
- Other

Urgency:
- High
- Medium
- Low

Tone:
- Urgent
- Neutral
- Polite
- Friendly
- Frustrated
- Formal

Classification Rules:

INTENT:
- Request → asks for help, action, support, or response
- Information → provides updates or information
- Complaint → expresses dissatisfaction or frustration
- Follow-up → checks status of previous communication
- Greeting → greeting or casual salutation
- Appreciation → gratitude or thanking
- Other → anything else

URGENCY:
- High → contains words like immediately, urgent, ASAP, critical, emergency, now
- Medium → action required soon but not immediate
- Low → informational or no urgency

TONE:
- Urgent → pressure or time-sensitive
- Neutral → plain communication
- Polite → respectful or courteous
- Friendly → warm or conversational
- Frustrated → angry or dissatisfied
- Formal → professional style

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT add explanations.
3. Do NOT add markdown formatting.
4. Do NOT write extra words like "Output", "Email Text", or notes.
5. Your response must start with {{
   and end with }}.
6. Use double quotes for all JSON keys and values.

Email Text:
{text}

Return JSON in this exact format:

{{
    "intent": "string",
    "urgency": "string",
    "tone": "string"
}}
"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)