"""Main entrypoint for the Streamlit app."""

import streamlit as st
from demo_inputs.example_transcripts import example_transcripts
from helper_functions.keyword_search import keyword_search

class KeywordSearchApp:
    def __init__(self):
        self.example_transcripts = example_transcripts  # Load the transcripts
    
    def run(self):
        # Streamlit title and description
        st.title("Keyword Search in Call Transcripts")
        st.write("Enter a keyword to search for in the call transcripts.")

        # User input field to enter the search keyword
        search_term = st.text_input("Enter keyword:")

        # Check if the user has entered a keyword
        if search_term:
            self.check_and_display_results(search_term)
    
    def check_and_display_results(self, search_term):
        # Use the function to find matching calls
        matching_calls = find_calls_with_keyword(self.example_transcripts, search_term)

        # Display results
        if matching_calls:
            st.success(f"The keyword '{search_term}' is found in the following calls: {', '.join(matching_calls)}")
        else:
            st.error(f"No calls found with the keyword '{search_term}'.")

# Instantiate and run the Streamlit app
if __name__ == "__main__":
    app = KeywordSearchApp()
    app.run()