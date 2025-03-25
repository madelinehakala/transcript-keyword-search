"""Main entrypoint for the Streamlit app."""

import streamlit as st
from helper_functions.keyword_search import keyword_search
from demo_inputs.example_transcripts import example_transcripts

class KeywordSearchApp:
    def __init__(self):
        self.example_transcripts = example_transcripts  # Load the transcripts
    
    def run(self) -> None:
        # Streamlit title and description with improved styling
        st.markdown(
            """
            <style>
            .title {
                font-size: 2.5rem;
                font-weight: bold;
                color: #5A9; /* Muted blue color */
                text-align: center;
                margin-bottom: 20px;
            }
            .description {
                font-size: 1.2rem;
                text-align: center;
                margin-bottom: 30px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="title">Keyword Search for Call Transcripts</div>', unsafe_allow_html=True)
        st.markdown('<div class="description">Enter a keyword to search for in the call transcripts.</div>', unsafe_allow_html=True)

        # User input field to enter the search keyword
        search_term = st.text_input("🔍 Enter keyword:")

        # Check if the user has entered a keyword
        if search_term:
            self.check_and_display_results(search_term)
    
    def check_and_display_results(self, search_term: str) -> None:
        # Use the function to find matching calls
        matching_calls = keyword_search(self.example_transcripts, search_term)

        # Display results
        if matching_calls:
            st.success(f"✅ The keyword '{search_term}' is found in the following calls:")
            for call_id, transcript in matching_calls.items():
                with st.expander(f"📞 Call ID: {call_id}", expanded=False):
                    st.markdown(f"**Transcript:** \n\n{transcript}")
                st.markdown("---")
        else:
            st.error(f"❌ No calls found with the keyword '{search_term}'.")

# Instantiate and run the Streamlit app
if __name__ == "__main__":
    app = KeywordSearchApp()
    app.run()