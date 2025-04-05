import streamlit as st
import json

# Load projects data
def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)

# Generate thumbnail path automatically
def get_thumbnail_path(category, title, thumbnail_file):
    category_dir = category.replace(" ", "_")
    title_dir = title.replace(" ", "_")
    return f"data/{category_dir}/{title_dir}/img/{thumbnail_file}"

# Display project thumbnails
def display_project_thumbnails(category, projects):
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
        with cols[idx % 3]:
            st.image(thumbnail_path, use_container_width=True)
            if st.button(project["title"]):
                st.session_state.selected_project = (category, project["title"])

# Display detailed project information
def display_project_thumbnails(category, projects):
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
        assigned = project.get("assigned_to", "") != ""

        with cols[idx % 3]:
            if assigned:
                st.image(thumbnail_path, use_container_width=True, caption="❌ Project Taken")
            else:
                st.image(thumbnail_path, use_container_width=True)
            if st.button(project["title"]):
                st.session_state.selected_project = (category, project["title"])
                
def update_project_assignment(category, title, student_id):
    with open("data/projects.json", "r") as f:
        data = json.load(f)

    for project in data[category]:
        if project["title"] == title:
            project["assigned_to"] = student_id
            break

    with open("data/projects.json", "w") as f:
        json.dump(data, f, indent=2)

def check_student_already_assigned(student_id):
    with open("data/projects.json", "r") as f:
        data = json.load(f)

    for category_projects in data.values():
        for proj in category_projects:
            if proj.get("assigned_to", "") == student_id:
                return True
    return False

def display_project_details(category, project):
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

    assigned_id = project.get("assigned_to", "")
    if assigned_id:
        st.info(f"✅ This project has been adopted by student ID: {assigned_id}")
    else:
        with st.form(key="adopt_form"):
            student_id = st.text_input("Enter your assigned student ID to adopt this project")
            submit = st.form_submit_button("📥 Adopt This Project")
            if submit and student_id.strip():
                student_id = student_id.strip()
                if check_student_already_assigned(student_id):
                    st.error("⚠️ You have already adopted a project. Each student may only adopt one.")
                else:
                    update_project_assignment(category, project["title"], student_id)
                    st.success(f"✅ Project successfully adopted by ID: {student_id}")
                    st.rerun()

    if st.button("⬅️ Back to Projects"):
        st.session_state.selected_project = None

# Display Rubric
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

# Main function
def main():
    st.title("PHY132 Project Showcase")
    projects_data = load_projects()

    # Sidebar Navigation
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
            display_project_thumbnails(category, projects)
            st.markdown("---")
    else:
        category, title = st.session_state.selected_project
        for project in projects_data[category]:
            if project["title"] == title:
                display_project_details(category, project)
                break

if __name__ == "__main__":
    main()