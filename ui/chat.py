import streamlit as st

def render_chat(messages):
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div class='user-box'>{msg['content']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='assistant-box'>{msg['content']}</div>",
                unsafe_allow_html=True
            )

def add_message(role, content):
    st.session_state.messages.append({
        "role": role,
        "content": content
    })
