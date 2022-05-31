import streamlit as st

from bbquote883.lib import get_quote

author, quote = get_quote()  # assuming the function returns an author and a quote

st.title('Welcome to my Breaking Bad quote generator ! Made with ❤️ - Bali 883 Le Wagon')
f"Quote : {quote}, \n> {author}"
