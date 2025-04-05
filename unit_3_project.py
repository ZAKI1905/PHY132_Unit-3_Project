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

# Display project details
def display_project_details(category, project):
    st.header(project["title"])
    st.write(project["description"])
    thumbnail_path = get_thumbnail_path(category, project["title"], project["thumbnail"])
    st.image(thumbnail_path, use_container_width=True)

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

    # Footer with contact info and EKU logo
    footer = '''
    ---
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