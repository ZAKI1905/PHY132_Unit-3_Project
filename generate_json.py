import os
import json

root_dir = "data"
json_data = {}

# Walk through the directories
for category in os.listdir(root_dir):
    cat_path = os.path.join(root_dir, category)
    if os.path.isdir(cat_path):
        projects = []
        for project in os.listdir(cat_path):
            proj_path = os.path.join(cat_path, project)
            if os.path.isdir(proj_path):
                img_dir = os.path.join(proj_path, "img")
                thumbnails = [f for f in os.listdir(img_dir) if "thumbnail" in f.lower()]
                thumbnail_path = os.path.join(img_dir, thumbnails[0]) if thumbnails else ""
                
                # Construct project description (you'll replace this manually later)
                projects.append({
                    "title": project.replace("_", " "),
                    "thumbnail": thumbnail_path.replace("\\", "/"),
                    "description": "Replace with your description.",
                    "rubric_link": "Replace with rubric link."
                })
        json_data[category.replace("_", " ")] = projects

# Save JSON
with open("projects.json", "w") as f:
    json.dump(json_data, f, indent=4)