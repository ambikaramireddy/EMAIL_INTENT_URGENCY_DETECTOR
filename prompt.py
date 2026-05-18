import warnings
warnings.filterwarnings("ignore")
from langchain_core.prompts import PromptTemplate

template = """
You are an advanced AI email analysis system.

Your task is to analyze the provided email text carefully and classify it into:

1. intent
2. urgency
3. tone

You must ONLY use the allowed labels.

--------------------------------------------------
ALLOWED LABELS
--------------------------------------------------

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

--------------------------------------------------
CLASSIFICATION DEFINITIONS
--------------------------------------------------

INTENT DEFINITIONS:

Request:
- Asking for help
- Asking for action
- Asking for support
- Asking for response
- Asking for approval
- Asking for completion of a task

Information:
- Sharing updates
- Sharing announcements
- Sharing schedules
- Sharing status information
- General informational communication

Complaint:
- Expressing dissatisfaction
- Reporting issues/problems
- Angry customer/user feedback
- Negative experience reporting

Follow-up:
- Checking status of previous communication
- Reminder emails
- Asking for updates on earlier discussions

Greeting:
- Greetings or casual salutations
- Introductory friendly messages

Appreciation:
- Thanking someone
- Expressing gratitude
- Appreciating support/help/work

Other:
- Anything not matching above categories

--------------------------------------------------
URGENCY RULES
--------------------------------------------------

High:
- Immediate action required
- Contains words like:
  urgent, immediately, ASAP, critical,
  emergency, now, as soon as possible
- Production/system failure situations
- Serious customer escalation

Medium:
- Action needed soon
- Mentions deadlines
- Time-sensitive but not emergency

Low:
- Informational communication
- No urgency indicators
- Casual or routine messages

--------------------------------------------------
TONE RULES
--------------------------------------------------

Urgent:
- Pressure or time-sensitive language
- Demanding immediate response

Neutral:
- Plain factual communication
- Emotionally balanced

Polite:
- Respectful and courteous
- Professional kindness

Friendly:
- Warm conversational language
- Casual positive communication

Frustrated:
- Angry, dissatisfied, irritated tone
- Complaints or negative emotions

Formal:
- Highly professional or official style

--------------------------------------------------
IMPORTANT PRIORITY RULES
--------------------------------------------------

1. Base classification ONLY on the provided email text.
2. Do NOT assume external context.
3. Do NOT hallucinate missing information.
4. Choose the MOST dominant intent.
5. Choose the MOST dominant tone.
6. If multiple tones exist, select the strongest tone.
7. If urgency indicators are absent, use Low.
8. Complaint emails with anger/frustration should usually have Frustrated tone.
9. Greetings and appreciation emails usually have Low urgency.
10. Use Other only if no category clearly matches.

--------------------------------------------------
OUTPUT RULES
--------------------------------------------------

1. Return ONLY valid JSON.
2. Do NOT include explanations.
3. Do NOT include markdown.
4. Do NOT include extra text.
5. Response must start with {{
6. Response must end with }}
7. Use double quotes for all keys and values.
8. Output must contain ONLY these keys:
   - intent
   - urgency
   - tone

--------------------------------------------------
EMAIL TEXT
--------------------------------------------------

{text}

--------------------------------------------------
OUTPUT FORMAT
--------------------------------------------------

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
