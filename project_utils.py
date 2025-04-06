import json
import streamlit as st

def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)

def get_thumbnail_path(category, directory, thumbnail_file):
    category_dir = category.replace(" ", "_")
    return f"data/{category_dir}/{directory}/img/{thumbnail_file}"

def display_project_thumbnails(category, projects, statuses):
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        thumbnail_path = get_thumbnail_path(category, project["directory"], project["thumbnail"])
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

def display_project_details(category, project, statuses):
    st.header(project["title"])
    thumbnail_path = get_thumbnail_path(category, project["directory"], project["thumbnail"])
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