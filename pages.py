import streamlit as st
# from project_utils import load_projects, display_project_thumbnails, display_project_details
from sheets import get_project_statuses, log_assignment, update_project_status, log_sign_event
from data.Magnetic_Fields_and_Forces.Analyz_Earths_Magnetos.project_texts import project_steps_texts

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        credentials = st.secrets["login"]
        if username in credentials and credentials[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            # Log sign-in event
            log_sign_event(username, action="login")
            st.rerun()
        else:
            st.error("Invalid username or password.")

def display_profile(statuses):
    st.header("Your Profile")
    username = st.session_state.get("username", "Unknown")
    st.write(f"**Username:** {username}")
    adopted_project = None
    for key, status in statuses.items():
        if status.get("Student ID", "") == username:
            adopted_project = key
            break
    if adopted_project:
        category, title = adopted_project
        st.write(f"**Adopted Project:** {title} in {category}")
    else:
        st.write("You have not adopted any project yet.")
    
    if st.button("Sign Out"):
        log_sign_event(username, action="logout")
        st.session_state["authenticated"] = False
        if "username" in st.session_state:
            del st.session_state["username"]
        st.rerun()

def display_my_project(statuses):
    st.header("My Project")
    username = st.session_state.get("username", "")
    adopted_project = None
    for key, status in statuses.items():
        if status.get("Student ID", "") == username:
            adopted_project = key
            break
    if adopted_project:
        category, title = adopted_project
        st.write(f"**Project:** {title} in {category}")
        # For the specific project, show a button to view detailed multi‑step info.
        if title == "Analyzing Earth’s Magnetosphere and the Physics of Solar Wind Interactions":
            if st.button("View Project Details"):
                st.session_state["project_step_index"] = 0  # initialize steps
                display_project_steps()
                return
        if st.button("Abandon Project"):
            log_assignment(category, title, username, action="abandoned")
            update_project_status(category, title, "", new_status="available")
            st.success("You have abandoned the project. It is now available for adoption.")
            st.rerun()
    else:
        st.write("You have not adopted any project.")

def display_project_steps():
    # Use the pages defined in project_texts.py
    pages = project_steps_texts
    if "project_step_index" not in st.session_state:
        st.session_state["project_step_index"] = 0

    index = st.session_state["project_step_index"]
    current_page = pages[index]

    st.header(current_page["title"])
    st.markdown(current_page["content"])

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if index > 0:
            if st.button("Back"):
                st.session_state["project_step_index"] = index - 1
                st.rerun()
    with col3:
        if index < len(pages) - 1:
            btn_label = "Start" if index == 0 else "Next"
            if st.button(btn_label):
                st.session_state["project_step_index"] = index + 1
                st.rerun()
        else:
            st.write("End of project details.")

    st.markdown("---")
    st.info("Use the Next and Back buttons to navigate through the project steps.")

def display_rubric():
    st.header("📌 Project Grading Rubric")
    rubric_markdown = """
    <style>
    table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        font-family: sans-serif;
    }
    th, td {
        padding: 10px;
        text-align: center;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #4CAF50;
        color: white;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #ddd;
    }
    </style>

    | Criteria | Weight |
    |:--------:|:------:|
    | Conceptual Understanding & Clarity | 25% |
    | Quantitative Analysis & Accuracy | 30% |
    | Quality and Clarity of Diagrams | 20% |
    | Analytical Depth & Real-world Connections | 15% |
    | Overall Presentation & Organization | 10% |
    """
    st.markdown(rubric_markdown, unsafe_allow_html=True)

def main_app():
    st.title("PHY132 Project Showcase")
    from project_utils import load_projects, display_project_thumbnails, display_project_details
    projects_data = load_projects()
    statuses = get_project_statuses()

    # Build navigation options dynamically.
    nav_options = ["🏠 Projects", "📌 Rubric", "👤 Profile"]
    username = st.session_state.get("username")
    if username:
        for status in statuses.values():
            if status.get("Student ID", "") == username:
                if "📁 My Project" not in nav_options:
                    nav_options.insert(1, "📁 My Project")
                break

    selection = st.sidebar.radio("Go to:", nav_options)
    if selection == "📌 Rubric":
        display_rubric()
        return
    elif selection == "👤 Profile":
        display_profile(statuses)
        return
    elif selection == "📁 My Project":
        display_my_project(statuses)
        return

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None

    if st.session_state.selected_project is None:
        for category, projects in projects_data.items():
            st.subheader(category)
            display_project_thumbnails(category, projects, statuses)
            st.markdown("---")
    else:
        category, title = st.session_state.selected_project
        for project in projects_data[category]:
            if project["title"] == title:
                display_project_details(category, project, statuses)
                break

    footer = '''
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            This tool was developed for <b>PHY 132 - College Physics II</b> at Eastern Kentucky University.<br>
            For questions, contact: <b>Professor Zakeri</b> (m.zakeri@eku.edu)
        </div>
        <div>
            <img src="https://raw.githubusercontent.com/ZAKI1905/phy132-kirchhoff-checker/main/img/PrimaryLogo_Maroon.png" width="150">
        </div>
    </div>
    '''
    st.markdown(footer, unsafe_allow_html=True)