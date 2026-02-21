# Praxis
⸻

🚀 Praxis — AI Powered Placement Assistant

Praxis is a modular AI-powered placement preparation system built with Streamlit.
It simulates real interview environments, evaluates coding solutions, and intelligently resolves doubts using a hybrid evaluation architecture that minimizes API dependency while maintaining intelligent feedback quality.

Designed to feel like a modern SaaS product — fast, interactive, and clean.

⸻

🌟 Key Features

🧠 Interview Practice
	•	Simulates technical interview scenarios
	•	Keyword-aware deterministic scoring
	•	AI-powered improvement suggestions (only when required)
	•	Structured strengths & weaknesses feedback
	•	Context-aware session flow

💻 Coding Practice
	•	Practice DSA & technical problems
	•	Paste your code directly or upload files
	•	Heuristic time & space complexity analysis
	•	Optimization hints and improvement suggestions
	•	Clean VSCode-style dark code editor UI

📚 Doubt Solver
	•	Ask conceptual questions
	•	Upload code files (.cpp, .java, .py, etc.)
	•	Upload PDFs
	•	Upload screenshots
	•	Structured AI explanations with readable formatting

🎨 Modern UI
	•	Dark-first design
	•	Glassmorphism elements
	•	Gradient chat bubbles
	•	Animated status indicators
	•	Clean modular layout

⸻

🧠 Architecture Overview

Praxis follows a Hybrid Intelligent Evaluation Architecture:

🔹 Frontend Layer
	•	Streamlit-based UI
	•	Custom CSS styling
	•	Interactive session management

🔹 Local Evaluation Engine
	•	Keyword-based deterministic scoring
	•	Missing concept detection
	•	Structured feedback generation
	•	Heuristic complexity analysis

🔹 AI Refinement Layer
	•	Gemini API used only when needed
	•	Improvement suggestions for low scores
	•	Advanced doubt explanations

This reduces:
	•	API latency
	•	Cost
	•	Over-dependence on LLM scoring

⸻

🧩 Tech Stack
	•	Frontend: Streamlit
	•	Backend Logic: Python
	•	AI Integration: Google Gemini API
	•	File Handling: PyPDF
	•	Environment Management: python-dotenv
	•	Architecture Style: Modular design with separation of concerns

⸻

📁 Project Structure

.
├── app.py                  # Main Streamlit entry point
├── evaluator.py            # AI evaluation logic
├── prompts.py              # Prompt engineering for Gemini
├── data/
│   ├── init.py
│   └── question_bank.py    # Interview & DSA question bank
├── modes/
│   ├── interview_mode.py   # Interview Practice logic
│   ├── coding_mode.py      # Coding Practice logic
│   └── doubt_mode.py       # Doubt Solver logic
├── ui/
│   ├── chat.py             # Chat UI components
│   ├── sidebar.py          # Sidebar layout & controls
│   └── styles.py           # Custom CSS styling
├── Requirements.txt
├── README.md
└── .env (not pushed to GitHub)

⸻

⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/yourusername/praxis.git
cd praxis


⸻

2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


⸻

3️⃣ Install Dependencies

pip install -r requirements.txt


⸻

4️⃣ Configure Environment Variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here

Get your API key from:
https://aistudio.google.com/app/apikey

⸻

▶️ Run the Application

streamlit run app.py

App will launch at:

http://localhost:8501


⸻

🌟 What Makes Praxis Different?
	•	Hybrid deterministic scoring system
	•	Reduced LLM dependency
	•	Modular architecture
	•	Multi-format doubt input support
	•	Modern UI built purely in Streamlit
	•	Designed for performance & scalability
  
⸻

🎯 Future Improvements
	•	Persistent user progress tracking
	•	Analytics dashboard
	•	Adaptive difficulty system
	•	Leaderboard system
	•	Deployment-ready authentication system

⸻
