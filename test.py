"""
Test module for Email Intent & Urgency Detector
Run tests to validate model outputs
"""

from prompt import prompt
from parser import parser
from model import get_model
from config import TEST_CASES
import json


def run_single_test(email_text):
    """
    Run analysis on a single email
    
    Args:
        email_text (str): Email text to analyze
        
    Returns:
        EmailAnalysis: Parsed analysis result
    """
    try:
        model = get_model()
        chain = prompt | model | parser
        result = chain.invoke({"text": email_text})
        return result
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return None


def run_all_tests():
    """
    Run all test cases and display results
    """
    print("=" * 80)
    print("EMAIL INTENT & URGENCY DETECTOR - TEST SUITE")
    print("=" * 80)
    print()
    
    passed = 0
    failed = 0
    
    for test_name, test_data in TEST_CASES.items():
        print(f"Test Case: {test_name}")
        print("-" * 80)
        print(f"Input Email: {test_data['email']}")
        print()
        
        result = run_single_test(test_data['email'])
        
        if result:
            print(f"Output:")
            print(f"  Intent:  {result.intent}")
            print(f"  Urgency: {result.urgency}")
            print(f"  Tone:    {result.tone}")
            print()
            
            # Check if output matches expected values
            intent_match = result.intent == test_data['expected_intent']
            urgency_match = result.urgency == test_data['expected_urgency']
            tone_match = result.tone == test_data['expected_tone']
            
            print(f"Expected:")
            print(f"  Intent:  {test_data['expected_intent']} {'✓' if intent_match else '✗'}")
            print(f"  Urgency: {test_data['expected_urgency']} {'✓' if urgency_match else '✗'}")
            print(f"  Tone:    {test_data['expected_tone']} {'✓' if tone_match else '✗'}")
            print()
            
            if intent_match and urgency_match and tone_match:
                print("Status: ✓ PASSED")
                passed += 1
            else:
                print("Status: ✗ FAILED")
                failed += 1
        else:
            print("Status: ✗ ERROR")
            failed += 1
        
        print()
    
    print("=" * 80)
    print(f"TEST RESULTS: {passed} Passed, {failed} Failed out of {len(TEST_CASES)} tests")
    print("=" * 80)
    
    return passed, failed


if __name__ == "__main__":
    run_all_tests()