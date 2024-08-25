import streamlit as st
import tempfile
import os
from word import parse_docx, create_html  # Ensure the wordhtml.py file is correctly referenced

def main():
    st.title("Resume to HTML Converter")

    uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        
        # Generate HTML file
        parsed_content = parse_docx(temp_file_path)
        html_file_path = "/tmp/resume.html"  # Use a temporary file location or other appropriate path
        create_html(parsed_content, html_file_path)
        
        # Create a download button
        with open(html_file_path, "r") as f:
            html_content = f.read()
        
        st.download_button(
            label="Download HTML file",
            data=html_content,
            file_name="resume.html",
            mime="text/html"
        )
        
        # Optionally, remove the temporary files after use
        os.remove(temp_file_path)
        os.remove(html_file_path)

if __name__ == "__main__":
    main()
