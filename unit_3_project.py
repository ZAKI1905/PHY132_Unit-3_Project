import streamlit as st
import json
from sheets import log_assignment, get_project_statuses, update_project_status

# Load projects metadata from JSON (for objectives, thumbnails, etc.)
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
        # Use status from Google Sheet; default to "available" if not found.
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

# Update the project assignment:
# Log the assignment and update the status sheet.
def update_project_assignment(category, title, student_id):
    # Log the assignment in the log sheet
    st.write("Logging the assignment to Google Sheets")
    log_assignment(category, title, student_id)
    # Update the status sheet (set the project as taken/adopted)
    update_project_status(category, title, student_id, new_status="taken")

# Check if the student has already been assigned a project by scanning the status sheet.
def check_student_already_assigned(student_id, statuses):
    for status in statuses.values():
        if status.get("Student ID", "") == student_id:
            return True
    return False

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

    # Get the current status from the Google Sheet
    key = (category, project["title"])
    proj_status = statuses.get(key, {"Status": "available", "Student ID": ""})
    if proj_status["Status"].lower() in ["taken", "adopted"]:
        st.info(f"✅ This project has been adopted by student ID: {proj_status.get('Student ID')}")
    else:
        with st.form(key="adopt_form"):
            student_id = st.text_input("Enter your assigned student ID to adopt this project")
            submit = st.form_submit_button("📥 Adopt This Project")
            if submit and student_id.strip():
                student_id = student_id.strip()
                # Refresh statuses in case of recent changes
                statuses = get_project_statuses()
                if check_student_already_assigned(student_id, statuses):
                    st.error("⚠️ You have already adopted a project. Each student may only adopt one.")
                else:
                    update_project_assignment(category, project["title"], student_id)
                    st.success(f"✅ Project successfully adopted by ID: {student_id}")
                    st.rerun()

    if st.button("⬅️ Back to Projects"):
        st.session_state.selected_project = None

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

def main():
    st.title("PHY132 Project Showcase")
    projects_data = load_projects()
    # Get the current project statuses from Google Sheets.
    statuses = get_project_statuses()

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to:", ["🏠 Projects", "📌 Rubric"])
    if selection == "📌 Rubric":
        display_rubric()
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

if __name__ == "__main__":
    main()