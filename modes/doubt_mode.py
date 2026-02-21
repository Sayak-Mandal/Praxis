import streamlit as st
from PIL import Image
import pypdf
import io
from evaluator import solve_doubt

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = pypdf.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_code(code_file):
    try:
        return code_file.getvalue().decode("utf-8")
    except Exception as e:
        return f"Error reading code file: {str(e)}"

def run():
    st.markdown("<div class='mode-title'>Doubt Solver</div>", unsafe_allow_html=True)
    
    if 'doubt_history' not in st.session_state:
        st.session_state.doubt_history = []
        
    st.info("Ask any doubt. You can also upload a PDF, Image, or Code file for context.")
    
    upload_file = st.file_uploader("Upload Image, PDF, or Code file", type=["png", "jpg", "jpeg", "pdf", "py", "java", "cpp", "c", "js", "html", "css", "txt"])
    
    # Display chat history
    for chat in st.session_state.doubt_history:
        with st.chat_message("user"):
            st.write(chat['user'])
        with st.chat_message("assistant"):
            st.write(chat['ai'])
            
    if prompt := st.chat_input("Describe your doubt:"):
        with st.chat_message("user"):
            st.write(prompt)
            
        image_ctx = None
        text_ctx = ""
        
        if upload_file is not None:
            if upload_file.name.lower().endswith('.pdf'):
                text_ctx = extract_text_from_pdf(upload_file)
            elif upload_file.name.lower().endswith(('.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.txt')):
                text_ctx = extract_text_from_code(upload_file)
            else:
                image_ctx = Image.open(upload_file)
                
        with st.chat_message("assistant"):
            with st.spinner("Analysing doubt..."):
                answer = solve_doubt(prompt, text_context=text_ctx, image=image_ctx)
                st.write(answer)
                
        st.session_state.doubt_history.append({
            "user": prompt,
            "ai": answer
        })
