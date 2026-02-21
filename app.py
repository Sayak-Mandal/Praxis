import streamlit as st
from ui.styles import load_css
from modes import interview_mode, coding_mode, doubt_mode

def main():
    st.set_page_config(page_title="Praxis", layout="centered")
    
    # Load custom CSS
    st.markdown(load_css(), unsafe_allow_html=True)
    
    st.sidebar.markdown("""
        <div class="sidebar-title-box">
            <div class="sidebar-title-text"><span class="status-dot"></span>Praxis</div>
        </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("<div style='text-align: center; opacity: 0.7; font-style: italic; margin-bottom: 20px;'>Your One Tap Placement Assistant</div>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Navigation")
    mode_selection = st.sidebar.radio("Select Mode", ["Interview Practice", "Coding Practice", "Doubt Solver"])
    
    if mode_selection == "Interview Practice":
        interview_mode.run()
    elif mode_selection == "Coding Practice":
        coding_mode.run()
    elif mode_selection == "Doubt Solver":
        doubt_mode.run()

if __name__ == "__main__":
    main()
