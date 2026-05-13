"""
Email Intent & Urgency Detector - Configuration Module
This file contains configuration and helper functions for the application.
"""

# Email Intent Categories
INTENT_CATEGORIES = {
    "Request": "Email asks for action, help, or response",
    "Information": "Email provides information or updates",
    "Complaint": "Email expresses dissatisfaction or issues",
    "Follow-up": "Email checks status or follows up on previous communication",
    "Greeting": "Email is a greeting or salutation",
    "Appreciation": "Email thanks or appreciates someone",
    "Other": "Any other intent not listed above"
}

# Urgency Levels
URGENCY_LEVELS = {
    "High": "Contains urgent language like 'immediately', 'ASAP', 'critical'",
    "Medium": "Contains action required but not immediately, mentions deadlines",
    "Low": "No urgency indicators, informational, can wait"
}

# Tone Types
TONE_TYPES = {
    "Urgent": "Shows pressure, time-sensitive language",
    "Neutral": "Neither positive nor negative",
    "Polite": "Courteous, respectful language",
    "Friendly": "Warm, conversational tone",
    "Frustrated": "Shows frustration, dissatisfaction, anger",
    "Formal": "Professional, official language"
}

# Test Cases for Validation
TEST_CASES = {
    "Urgent Request": {
        "email": "Please fix this issue immediately. The system is down and affecting all users!",
        "expected_intent": "Request",
        "expected_urgency": "High",
        "expected_tone": "Urgent"
    },
    
   
    "Follow-up": {
        "email": "Just checking in on the status of your proposal from last week. Looking forward to your thoughts.",
        "expected_intent": "Follow-up",
        "expected_urgency": "Low",
        "expected_tone": "Polite"
    },
    "Greeting": {
        "email": "Hi there! Hope you're having a great day!",
        "expected_intent": "Greeting",
        "expected_urgency": "Low",
        "expected_tone": "Friendly"
    },
    "Appreciation": {
        "email": "Thank you so much for your help with the project. You did an amazing job!",
        "expected_intent": "Appreciation",
        "expected_urgency": "Low",
        "expected_tone": "Polite"
    },
    
"Informational Email": {
    "email": "The weekly team meeting is scheduled for Friday at 2 PM in Conference Room B.",
    "expected_intent": "Information",
    "expected_urgency": "Low",
    "expected_tone": "Neutral"
},




"Complaint": {
    "email": "I'm extremely frustrated with the service quality. This is completely unacceptable!",
    "expected_intent": "Complaint",
    "expected_urgency": "High",
    "expected_tone": "Frustrated"
},




}