import streamlit as st
import json

# Load simplified projects data
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

# Display project details
def display_project_details(category, project):
    st.header(project["title"])
    st.write(project["description"])
    st.markdown(f"[📄 View Rubric]({project['rubric_link']})")
    
    thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
    st.image(thumbnail_path, use_container_width=True)

    if st.button("⬅️ Back to Projects"):
        st.session_state.selected_project = None

# Main function
def main():
    st.title("PHY132 Project Showcase")
    projects_data = load_projects()

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