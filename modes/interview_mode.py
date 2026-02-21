import streamlit as st
from data.question_bank import QUESTION_BANK
from evaluator import evaluate_interview_answer

import random

def run():
    st.markdown("<div class='mode-title'>Interview Practice</div>", unsafe_allow_html=True)
    
    # Selection from sidebar
    track = st.sidebar.selectbox("Select Track", list(QUESTION_BANK["Interview Practice"].keys()), key="int_track")
    difficulty = st.sidebar.selectbox("Select Difficulty", list(QUESTION_BANK["Interview Practice"][track].keys()), key="int_diff")
    
    # Initialize session state for this mode
    if 'interview_questions' not in st.session_state:
        st.session_state.interview_questions = []
    if 'interview_current_index' not in st.session_state:
        st.session_state.interview_current_index = 0
    if 'interview_history' not in st.session_state:
        st.session_state.interview_history = []
        
    start_btn = st.sidebar.button("Start / Reset Interview", key="start_int")
    
    if start_btn:
        all_q = QUESTION_BANK["Interview Practice"][track][difficulty]
        # Shuffle and pick up to 3 questions
        st.session_state.interview_questions = random.sample(all_q, min(len(all_q), 3))
        st.session_state.interview_current_index = 0
        st.session_state.interview_history = []
        
    if not st.session_state.interview_questions:
        st.info("Please select Track and Difficulty, then click Start in the sidebar.")
        return
        
    current_q_index = st.session_state.interview_current_index
    total_q = min(len(st.session_state.interview_questions), 3)
    
    # Initialize report state
    if 'interview_report' not in st.session_state:
        st.session_state.interview_report = None
    
    # Display previous chat history
    for chat in st.session_state.interview_history:
        if chat["type"] == "question":
            with st.chat_message("assistant"):
                st.markdown(f"**Question {chat['q_num']}:** {chat['text']}")
        elif chat["type"] == "answer":
            with st.chat_message("user"):
                st.write(chat["text"])
        elif chat["type"] == "evaluation":
            with st.chat_message("assistant"):
                st.markdown(chat["text"], unsafe_allow_html=True)
                
    # Check if we need to show the next question
    if current_q_index < total_q:
        question = st.session_state.interview_questions[current_q_index]
        
        # If the last item in history is NOT the current question, add and show it
        if not st.session_state.interview_history or st.session_state.interview_history[-1]["type"] == "evaluation":
            st.session_state.interview_history.append({
                "type": "question", 
                "text": question,
                "q_num": current_q_index + 1
            })
            with st.chat_message("assistant"):
                 st.markdown(f"**Question {current_q_index + 1}:** {question}")
        
        # Process Chat Input
        if prompt := st.chat_input("Your Answer:"):
            # Add user answer to history
            st.session_state.interview_history.append({
                "type": "answer",
                "text": prompt
            })
            
            # Display user answer temporarily
            with st.chat_message("user"):
                st.write(prompt)
                
            with st.spinner("Evaluating..."):
                from evaluator import evaluate_interview_answer
                eval_text, score = evaluate_interview_answer(st.session_state.interview_questions[current_q_index], prompt)
                
            # Add evaluation to history
            st.session_state.interview_history.append({
                 "type": "evaluation",
                 "text": eval_text,
                 "score": score
            })
            
            # Auto advance
            st.session_state.interview_current_index += 1
            st.rerun()

    # If done with all questions
    if st.session_state.interview_current_index >= total_q:
        st.success("You have completed the interview session!")
        
        # Generate the report if it hasn't been generated yet
        if not st.session_state.interview_report:
            with st.spinner("Generating Performance Report..."):
                from evaluator import generate_interview_report
                report = generate_interview_report(st.session_state.interview_history)
                st.session_state.interview_report = report
                
        # Display the report
        st.markdown("---")
        st.markdown("## 📊 Interview Performance Report")
        st.markdown(st.session_state.interview_report)
        st.markdown("---")
        
        if st.button("Restart Interview"):
            st.session_state.interview_current_index = 0
            st.session_state.interview_history = []
            st.session_state.interview_report = None
            st.rerun()

        # Add disabled chat input to anchor the scroll
        st.chat_input("Interview completed.", disabled=True)
