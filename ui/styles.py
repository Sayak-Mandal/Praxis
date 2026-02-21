def load_css():
    return """
    <style>
    /* Dark Mode First Design */
    :root {
        --bg-color: #0e1117;
        --text-color: #fafafa;
        --box-bg: rgba(255, 255, 255, 0.05);
        --user-bubble: linear-gradient(135deg, #0f9b0f, #00c853);
        --ai-bubble: linear-gradient(135deg, #1e3c72, #2a5298);
        --border-radius: 12px;
    }

    /* Sidebar Title Box */
    .sidebar-title-box {
        padding: 15px 10px;
        text-align: center;
        margin-bottom: 5px;
    }
    .sidebar-title-text {
        font-size: 2.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #4CAF50, #81C784);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    /* Breathing Green Dot */
    .status-dot {
        width: 12px;
        height: 12px;
        background-color: #00e676;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 8px #00e676;
        animation: breathe 2s infinite ease-in-out;
    }

    @keyframes breathe {
        0% { opacity: 0.3; transform: scale(0.8); box-shadow: 0 0 4px #00e676; }
        50% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 12px #00e676, 0 0 20px #00e676; }
        100% { opacity: 0.3; transform: scale(0.8); box-shadow: 0 0 4px #00e676; }
    }

    body {
        color: var(--text-color);
        background-color: var(--bg-color);
    }

    /* App layout & Title */
    .app-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .mode-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #4CAF50, #81C784);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    }

    /* Text Colors */
    .text-green { color: #4CAF50 !important; font-weight: bold; }
    .text-yellow { color: #FFC107 !important; font-weight: bold; }
    .text-red { color: #f44336 !important; font-weight: bold; }

    /* Question box */
    .question-box {
        background: var(--box-bg);
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: var(--border-radius);
        margin-bottom: 20px;
        font-size: 1.1rem;
        color: var(--text-color);
    }
    </style>
    """