import streamlit as st
from pages import login_page, main_app

def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if not st.session_state["authenticated"]:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()