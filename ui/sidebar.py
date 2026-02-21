import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.header("🚀 PlacementSense AI")

        # -----------------------------
        # MODE SELECTION
        # -----------------------------
        mode = st.radio(
            "Select Mode",
            [
                "🎤 Interview Practice",
                "📚 Doubt Solver",
                "💻 Coding Practice"
            ]
        )

        st.divider()

        # Default values
        role = None
        difficulty = None
        start = False

        # -----------------------------
        # INTERVIEW SETTINGS
        # -----------------------------
        if mode == "🎤 Interview Practice":

            role = st.selectbox(
                "Select Track",
                [
                    "Java Developer",
                    "DSA"
                ]
            )

            difficulty = st.selectbox(
                "Select Difficulty",
                [
                    "Easy",
                    "Medium",
                    "Hard"
                ]
            )

            start = st.button("Start Interview")

        return mode, role, difficulty, start
