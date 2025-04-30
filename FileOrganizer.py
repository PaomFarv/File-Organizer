import os
import shutil

def clear_terminal():
    
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

clear_terminal()

file_extensions = {
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".tif",".webp",".heic",".ico"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".tgz"],
    "Executables_Scripts": [".exe", ".bat", ".sh", ".py", ".java", ".js"],
    "Others": [".html", ".htm", ".css", ".json", ".xml", ".md"]
}

# Get the current working directory
while True:
    try:
        desired_directory = str(input("\nEnter the directory path to organize: "))
    except ValueError:
        print("Invalid input. Please enter a valid directory path.")
        continue
    
    if not os.path.exists(desired_directory):
        print("The specified directory does not exist.")
        continue

    break

files_in_desired_dir = os.listdir(desired_directory)

for file in files_in_desired_dir:
    file_extension = os.path.splitext(file)[1]

    for folder_name, extensions in file_extensions.items():
        if file_extension.lower() in extensions:  # Match extensions
            folder_dir = os.path.join(desired_directory, folder_name)

            # Create folder if it doesn't exist
            if not os.path.exists(folder_dir):
                os.mkdir(folder_dir)

            # Move the file into the appropriate folder
            shutil.move(os.path.join(desired_directory, file), os.path.join(folder_dir, file))
            print(f"Moved '{file}' to '{folder_name}' folder.")
            print("ALL FILES MOVED SUCCESSFULLY! If all the files are not moved to the correct folder, please check the file extension and try again. " \
            "You might need to add more extensions in script's dictionary.")
            print("\n<A PaomFarv Creation>\n")
            break
else:
    print("No files to move.")
    print("\n Coded by PaomFArv.\n")