import streamlit as st
import json

# Load project data from external file
@st.cache_data
def load_projects():
    with open('data/projects.json', 'r') as file:
        data = json.load(file)
    return data

# Display project thumbnails as clickable buttons
def display_project_thumbnails(projects):
    cols = st.columns(3)  # Adjust column number for layout
    buttons = {}
    for idx, project in enumerate(projects):
        with cols[idx % 3]:
            st.image(project["thumbnail"], use_container_width=True)
            if st.button(project["title"]):
                st.session_state.selected_project = project["title"]

# Display selected project details
def display_project_details(project):
    st.header(project["title"])
    st.write(project["description"])
    st.markdown(f"[📄 View Rubric]({project['rubric_link']})", unsafe_allow_html=True)
    if st.button("⬅️ Back to Projects"):
        st.session_state.selected_project = None

# Main app logic
def main():
    st.title("PHY132 Project Showcase")

    st.image("data/img/magnetosphere/magnetosphere_thumbnail.jpg")
    
    projects_data = load_projects()

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None

    if st.session_state.selected_project is None:
        for category, projects in projects_data.items():
            st.subheader(category)
            display_project_thumbnails(projects)
            st.markdown("---")
    else:
        # Find and display the selected project
        for projects in projects_data.values():
            for project in projects:
                if project["title"] == st.session_state.selected_project:
                    display_project_details(project)
                    return

if __name__ == "__main__":
    main()
