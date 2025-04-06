import streamlit as st
import json
from sheets import log_assignment, get_project_statuses, update_project_status

# Load project metadata from JSON
def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)

def get_thumbnail_path(category, title, thumbnail_file):
    category_dir = category.replace(" ", "_")
    title_dir = title.replace(" ", "_")
    return f"data/{category_dir}/{title_dir}/img/{thumbnail_file}"

# Display project thumbnails using status from Google Sheets
def display_project_thumbnails(category, projects, statuses):
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
        # Get current status from the Google Sheet (default to "available")
        key = (category, project["title"])
        proj_status = statuses.get(key, {"Status": "available"})
        is_taken = proj_status["Status"].lower() in ["taken", "adopted"]
        with cols[idx % 3]:
            if is_taken:
                st.image(thumbnail_path, use_container_width=True, caption="❌ Project Taken")
            else:
                st.image(thumbnail_path, use_container_width=True)
            if st.button(project["title"]):
                st.session_state.selected_project = (category, project["title"])

# Log the assignment and update the status sheet using the logged-in username
def update_project_assignment(category, title, username):
    st.write("Logging the assignment to Google Sheets")
    log_assignment(category, title, username)
    update_project_status(category, title, username, new_status="taken")

# Check if the student has already adopted a project by scanning the status sheet.
def check_student_already_assigned(username, statuses):
    for status in statuses.values():
        if status.get("Student ID", "") == username:
            return True
    return False

# Show detailed project information with an adopt button that uses the logged-in username.
def display_project_details(category, project, statuses):
    st.header(project["title"])
    thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
    st.image(thumbnail_path, use_container_width=True)

    st.subheader("📌 Objectives")
    for obj in project.get("objectives", []):
        st.write(f"- {obj}")

    st.subheader("📝 Tasks")
    for task in project.get("tasks", []):
        st.write(f"- {task}")

    st.subheader("🧲 Relevant Physics Concepts and Formulas (PHY132)")
    for concept in project.get("physics_concepts", []):
        st.write(f"- {concept}")

    key = (category, project["title"])
    proj_status = statuses.get(key, {"Status": "available", "Student ID": ""})
    if proj_status["Status"].lower() in ["taken", "adopted"]:
        st.info(f"✅ This project has been adopted by: {proj_status.get('Student ID')}")
    else:
        username = st.session_state.get("username")
        if username:
            if st.button("Adopt This Project"):
                # Refresh statuses to capture any recent changes
                statuses = get_project_statuses()
                if check_student_already_assigned(username, statuses):
                    st.error("⚠️ You have already adopted a project. Each student may only adopt one.")
                else:
                    update_project_assignment(category, project["title"], username)
                    st.success(f"✅ Project successfully adopted by {username}")
                    st.experimental_rerun()  # Or st.rerun if that’s what you're using.
        else:
            st.error("You must be logged in to adopt a project.")

    if st.button("⬅️ Back to Projects"):
        st.session_state.selected_project = None

# Display the project grading rubric.
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

# Display the logged-in student's profile
def display_profile(statuses):
    st.header("Your Profile")
    username = st.session_state.get("username", "Unknown")
    st.write(f"**Username:** {username}")
    adopted_project = None
    # Look for the project adopted by this student in the status sheet.
    for key, status in statuses.items():
        if status.get("Student ID", "") == username:
            adopted_project = key  # key is (category, title)
            break
    if adopted_project:
        category, title = adopted_project
        st.write(f"**Adopted Project:** {title} in {category}")
    else:
        st.write("You have not adopted any project yet.")

# The main application that combines everything together.
def main_app():
    st.title("PHY132 Project Showcase")
    projects_data = load_projects()
    statuses = get_project_statuses()

    # Sidebar Navigation now includes a Profile option.
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to:", ["🏠 Projects", "📌 Rubric", "👤 Profile"])
    if selection == "📌 Rubric":
        display_rubric()
        return
    elif selection == "👤 Profile":
        display_profile(statuses)
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

# The login page: once credentials are validated, we save the username in session state.
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        credentials = st.secrets["login"]
        if username in credentials and credentials[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.experimental_rerun()  # Refresh to load the main page
        else:
            st.error("Invalid username or password.")

# Main entry point
def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if not st.session_state["authenticated"]:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()