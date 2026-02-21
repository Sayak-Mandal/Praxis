import streamlit as st
from data.question_bank import QUESTION_BANK
from evaluator import evaluate_coding_answer

import random

def run():
    st.markdown("<div class='mode-title'>Coding Practice</div>", unsafe_allow_html=True)
    
    track = st.sidebar.selectbox("Select Track", list(QUESTION_BANK["Coding Practice"].keys()), key="cod_track")
    difficulty = st.sidebar.selectbox("Select Difficulty", list(QUESTION_BANK["Coding Practice"][track].keys()), key="cod_diff")
    
    if 'coding_questions' not in st.session_state:
        st.session_state.coding_questions = []
    if 'coding_current_index' not in st.session_state:
        st.session_state.coding_current_index = 0
    if 'coding_history' not in st.session_state:
        st.session_state.coding_history = []
        
    start_btn = st.sidebar.button("Start / Reset Coding", key="start_cod")
    
    if start_btn:
        all_q = QUESTION_BANK["Coding Practice"][track][difficulty]
        # Shuffle and pick up to 3 questions
        st.session_state.coding_questions = random.sample(all_q, min(len(all_q), 3))
        st.session_state.coding_current_index = 0
        st.session_state.coding_history = []
        
    if not st.session_state.coding_questions:
        st.info("Please select Track and Difficulty, then click Start in the sidebar.")
        return
        
    current_q_index = st.session_state.coding_current_index
    total_q = min(len(st.session_state.coding_questions), 3)
    
    # Display previous chat history
    for chat in st.session_state.coding_history:
        if chat["type"] == "question":
            with st.chat_message("assistant"):
                st.markdown(f"**Problem {chat['q_num']}:**\n{chat['text']}")
        elif chat["type"] == "answer":
            with st.chat_message("user"):
                st.code(chat["text"], language="python")
        elif chat["type"] == "evaluation":
            with st.chat_message("assistant"):
                st.markdown(chat["text"], unsafe_allow_html=True)
                
    # If done with all questions
    if current_q_index >= total_q:
        st.success("You have completed all problems in this set!")
        if st.button("Restart"):
            st.session_state.coding_current_index = 0
            st.session_state.coding_history = []
            st.rerun()
        return

    # Check if we need to show the next question
    question = st.session_state.coding_questions[current_q_index]
    
    # If the last item in history is NOT the current question, add and show it
    if not st.session_state.coding_history or st.session_state.coding_history[-1]["type"] == "evaluation":
        st.session_state.coding_history.append({
            "type": "question", 
            "text": question,
            "q_num": current_q_index + 1
        })
        with st.chat_message("assistant"):
             st.markdown(f"**Problem {current_q_index + 1}:**\n{question}")
    
    # Process Chat Input
    if prompt := st.chat_input("Your Code:"):
        # Add user answer to history
        st.session_state.coding_history.append({
            "type": "answer",
            "text": prompt
        })
        
        # Display user answer temporarily
        with st.chat_message("user"):
            st.code(prompt, language="python")
            
        with st.spinner("Executing and Evaluating..."):
            eval_text, score = evaluate_coding_answer(question, prompt)
            
        # Add evaluation to history
        st.session_state.coding_history.append({
             "type": "evaluation",
             "text": eval_text,
             "score": score
        })
        
        # Auto advance
        st.session_state.coding_current_index += 1
        st.rerun()
