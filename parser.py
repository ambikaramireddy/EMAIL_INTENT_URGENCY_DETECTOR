from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class EmailAnalysis(BaseModel):
    """
    Structured output model for email analysis results.
    
    Attributes:
        intent (str): Detected email intent (Request, Information, Complaint, Follow-up, Greeting, Appreciation, Other)
        urgency (str): Urgency level (High, Medium, Low)
        tone (str): Tone of the email (Urgent, Neutral, Polite, Friendly, Frustrated, Formal)
    """
    intent: str = Field(
        description="Detected email intent: Request, Information, Complaint, Follow-up, Greeting, Appreciation, or Other"
    )
    urgency: str = Field(
        description="Urgency level of the email: High, Medium, or Low"
    )
    tone: str = Field(
        description="Tone of the email: Urgent, Neutral, Polite, Friendly, Frustrated, or Formal"
    )


parser = PydanticOutputParser(pydantic_object=EmailAnalysis)
