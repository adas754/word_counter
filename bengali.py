import re
import streamlit as st

def count_words(text):
    bengali_pattern = r'[\u0980-\u09FF]+'  # Matches Bengali words
    english_pattern = r'[A-Za-z]+'         # Matches English words

   
    bengali_words = re.findall(bengali_pattern, text)
    english_words = re.findall(english_pattern, text)
    
    bengali_count = len(bengali_words)
    english_count = len(english_words)
    
    return bengali_count, english_count

def main():
    st.title("Bengali and English Word Counter")
    st.subheader("Upload a text file to count the number of Bengali and English words.")
    
   
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    
    if uploaded_file is not None:
        
        text = uploaded_file.read().decode('utf-8')

       
        bengali_count, english_count = count_words(text)

        
        st.write(f"Number of Bengali words: {bengali_count}")
        st.write(f"Number of English words: {english_count}")

if __name__ == "__main__":
    main()
