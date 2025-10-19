import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    # Define file type categories
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"],
        "Executables": [".exe", ".msi"],
        "Others": []
    }

    print(f"\nOrganizing files in: {folder_path}\n")

    # Scan the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        # Match file type and move
        for category, extensions in categories.items():
            if file_ext in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} → {category}")
                moved = True
                break

        # If extension not found, move to "Others"
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} → Others")

    print("\nFolder organized successfully!")

def main():
    print("Smart File Organizer")
    print("--------------------")
    folder_path = input("Enter the folder path to organize: ").strip()
    organize_folder(folder_path)

if __name__ == "__main__":
    main()
