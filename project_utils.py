import json
import streamlit as st
from sheets import get_project_statuses, log_assignment, update_project_status

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

# def display_project_details(category, project, statuses):
#     st.header(project["title"])
#     thumbnail_path = get_thumbnail_path(category, project["directory"], project["thumbnail"])
#     st.image(thumbnail_path, use_container_width=True)

#     st.subheader("📌 Objectives")
#     for obj in project.get("objectives", []):
#         st.write(f"- {obj}")

#     st.subheader("📝 Tasks")
#     for task in project.get("tasks", []):
#         st.write(f"- {task}")

#     st.subheader("🧲 Relevant Physics Concepts and Formulas (PHY132)")
#     for concept in project.get("physics_concepts", []):
#         st.write(f"- {concept}")

def check_student_already_assigned(username, statuses):
    for status in statuses.values():
        if status.get("Student ID", "") == username:
            return True
    return False

# Log a project adoption event and update its status as taken.
def update_project_assignment(category, title, username):
	st.write("Logging the assignment to Google Sheets")
	log_assignment(category, title, username, action="adopted")
	update_project_status(category, title, username, new_status="taken")
    
def display_project_details(category, project, statuses):
	st.header(project["title"])
    # Use the project["directory"] field for file paths.
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
    
    # Use the project title as the unique key for status.
	key = (category, project["title"])
    # Debugging output: Check the key and the current status.
	# st.write("DEBUG: Project Key:", key, "Status from Sheet:", statuses.get(key))
    
	# Get status from the Google Sheet, default to available.
	proj_status = statuses.get(key, {"Status": "available", "Student ID": ""})
	if proj_status["Status"].lower() in ["taken", "adopted"]:
		# st.info(f"✅ This project has been adopted by: {proj_status.get('Student ID')}")
		st.info(f"✅ This project has been adopted.")
	else:
		username = st.session_state.get("username")
		if username:
			if st.button("Adopt This Project"):
				# Refresh statuses to catch any recent changes.
				statuses = get_project_statuses()
				if check_student_already_assigned(username, statuses):
					st.error("⚠️ You have already adopted a project. Each student may only adopt one.")
				else:
					update_project_assignment(category, project["title"], username)
					st.success(f"✅ Project successfully adopted by {username}")
					st.rerun()
		else:
			st.error("You must be logged in to adopt a project.")
    
    # Add a Back button so the user can return to the projects list.
	if st.button("⬅️ Back to Projects"):
		st.session_state.selected_project = None
		st.rerun()