# prompts.py

def generate_question_prompt(role, difficulty):
    return f"""
You are a professional technical interviewer.

Generate ONE interview question for a {role} position.

Difficulty level: {difficulty}

Rules:
- Ask only ONE question.
- Do NOT provide the answer.
- Keep it realistic for placements.
- No HTML.
"""


def evaluation_prompt(question, answer):
    return f"""
You are a professional technical interviewer.

Evaluate the candidate's answer.

Return ONLY valid JSON in this exact format:

{{
"score": "X/10",
"strengths": "Explain what was good.",
"weaknesses": "Explain what was missing.",
"improved_answer": "Provide a better structured answer.",
"followup_question": "Ask a deeper related follow-up question."
}}

Rules:
- Score must be between 0 and 10.
- Do NOT include markdown.
- Do NOT include HTML.
- Return JSON only.

Question:
{question}

Candidate Answer:
{answer}
"""