import os
import shutil

# Folder to organize
folder = os.getcwd()

# Define categories & extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
}

# Make folders if they don't exist
for category in categories.keys():
    if not os.path.exists(os.path.join(folder, category)):
        os.makedirs(os.path.join(folder, category))

if not os.path.exists(os.path.join(folder, "Others")):
    os.makedirs(os.path.join(folder, "Others"))

# Organize files
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        moved = False
        for category, extensions in categories.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(filepath, os.path.join(folder, category, filename))
                print(f"✅ Moved: {filename} → {category}")
                moved = True
                break
        if not moved:
            shutil.move(filepath, os.path.join(folder, "Others", filename))
            print(f"✅ Moved: {filename} → Others")

print("\n🎉 Folder organized!")
