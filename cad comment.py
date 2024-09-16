import streamlit as st
from PIL import Image
import os

# File paths
COMMENT_FILE = "comments.txt"

# Function to save comments
def save_comment(comment):
    with open(COMMENT_FILE, "a") as f:
        f.write(comment + "\n")

# Function to load comments
def load_comments():
    if os.path.exists(COMMENT_FILE):
        with open(COMMENT_FILE, "r") as f:
            return f.readlines()
    return []

# Title of the app
st.title('CAD Drawing Commenting Tool')

# Ensure unique key for file uploader
uploaded_file = st.file_uploader("Upload CAD Drawing", type=["png", "jpg", "jpeg", "svg"], key="unique_file_uploader_key")

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded CAD Drawing', use_column_width=True)
    
    # Input for comments with a unique key
    comment = st.text_area("Add your comment here:", key="unique_text_area_key")
    
    # Button to submit the comment with a unique key
    if st.button('Submit Comment', key="unique_button_key"):
        if comment:
            save_comment(comment)
            st.success('Comment submitted!')
        else:
            st.warning('Please enter a comment.')
    
    # Display comments
    st.subheader('Previous Comments:')
    comments = load_comments()
    if comments:
        for c in comments:
            st.write(c.strip())
    else:
        st.write('No comments yet.')
