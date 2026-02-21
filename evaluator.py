import os
import google.generativeai as genai
import re

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def extract_score(text):
    """
    Parses scores like "8", "8/10", "Score: 8/10", "**Score: 8/10**", etc.
    Returns float or None.
    """
    match = re.search(r'(?:score|rating)[^\d]*(\d+(?:\.\d+)?)(?:\s*/\s*10)?', text, re.IGNORECASE)
    if match:
        return float(match.group(1))
        
    # fallback searching for x/10
    match = re.search(r'(\d+(?:\.\d+)?)\s*/\s*10', text)
    if match:
        return float(match.group(1))
        
    # fallback searching for a single number if text is very short
    if len(text.split()) < 5:
        match = re.search(r'\b(\d+(?:\.\d+)?)\b', text)
        if match:
            return float(match.group(1))
            
    return None

def format_score_color(text, score):
    """
    Wraps the score output from the AI text in a colored span based on the value.
    >= 8 is green, >= 5 is yellow, < 5 is red.
    """
    if score is None:
        return text
        
    color_class = "text-green"
    if score < 5:
        color_class = "text-red"
    elif score < 8:
        color_class = "text-yellow"
        
    # Check if the text actually contains the score formatting
    score_int = int(score) if score.is_integer() else score
    
    # Find the line containing the score and format it
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Strip asterisks for checking
        clean_line = line.replace('**', '')
        if f"{score_int}/10" in clean_line or f"{score}/10" in clean_line or ('Score' in clean_line and (str(score_int) in clean_line or str(score) in clean_line)):
            # Wrap the whole line in the color span
            lines[i] = f"<span class='{color_class}'>{line}</span>"
            break
            
    return '\n'.join(lines)

def evaluate_interview_answer(question, user_answer):
    """
    Evaluates the user's interview answer.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""
        You are an expert technical interviewer.
        Question: {question}
        User's Answer: {user_answer}
        
        Please evaluate the answer. 
        1. Provide a Score out of 10. Format it exactly as "Score: X/10" on its own line.
        2. Provide brief feedback.
        3. If the score is less than 10, provide an improved version of the answer.
        Limit your response to a concise review.
        """
        response = model.generate_content(prompt)
        text = response.text
        
        score = extract_score(text)
        text = format_score_color(text, score)
        return text, score
    except Exception as e:
        return f"API Error: {str(e)}", None

def evaluate_coding_answer(problem, code_answer):
    """
    Evaluates the user's coding answer.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""
        You are an expert software engineer reviewing code.
        Problem: {problem}
        User's Code:
        {code_answer}
        
        Please evaluate the code.
        1. Provide a Score out of 10. Format it exactly as "Score: X/10" on its own line.
        2. Comment on Time Complexity.
        3. Comment on Space Complexity.
        4. Provide feedback on code quality and correctness.
        5. If the score is less than 10, suggest an improvement or optimized code.
        """
        response = model.generate_content(prompt)
        text = response.text
        
        score = extract_score(text)
        text = format_score_color(text, score)
        return text, score
    except Exception as e:
        return f"API Error: {str(e)}", None

def solve_doubt(prompt_text, text_context="", image=None):
    """
    Solves a user's doubt, optionally with image or pdf text.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        contents = []
        if text_context:
            contents.append(f"Context from document: {text_context}")
        contents.append(f"User Doubt: {prompt_text}")
        if image:
            contents.append(image)
            
        response = model.generate_content(contents)
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"

def generate_interview_report(history):
    """
    Generates a final report summarizing the user's performance across 5 questions.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Prepare the conversation log
        conversation_log = ""
        for item in history:
            if item["type"] == "question":
                conversation_log += f"Q: {item['text']}\n"
            elif item["type"] == "answer":
                conversation_log += f"A: {item['text']}\n"
            elif item["type"] == "evaluation":
                conversation_log += f"Evaluation: {item['text']}\n"
                conversation_log += "-" * 40 + "\n"
                
        prompt = f"""
        You are an expert technical interviewer and career coach.
        Review the following transcript of an interview session:
        
        {conversation_log}
        
        Please generate a comprehensive performance report for the candidate.
        Include the following sections clearly formatted using Markdown:
        - **Overall Summary**: A brief paragraph summarizing their performance.
        - **Strengths**: What the candidate did well.
        - **Weaknesses/Areas of Improvement**: Where the candidate struggled or provided incomplete answers.
        - **Topics to Focus On**: Specific technical concepts or topics they should study further before their real interview.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating report: {str(e)}"
