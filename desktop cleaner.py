'''
import os
import shutil


def desktop_cleaner():
#Organizes the files based on the extention.

    desk_path= os.path.join(os.path.expanduser("~"), "Desktop")
    path_perm= 0o755
    fill_types={
        "images":[".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
        "videos" : [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
        "archives": [".zip", ".rar", ".7z"],
        "others" : []
    }
    
    for file_name in os.listdir(desk_path):
        file_path = os.path.join(desk_path, file_name)
        os.chmod(file_path, path_perm)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()

            for folder_name, extensions in fill_types.items():
                if extension in extensions:
                    target_folder = os.path.join(desk_path, folder_name) 
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(file_path, target_folder)
                    break
                else:
                    target_folder =os.path.join(desk_path, "others")
                    os.makedirs(target_folder, exist_ok= True) 
                    shutil.move(file_path, target_folder)

desktop_cleaner()
'''
'''
import os
import shutil

def desktop_cleaner():
    # Organizes the files based on the extension.
    
    desk_path = os.path.join(os.path.expanduser("~"), "Desktop")
    path_perm = 0o755
    fill_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
        "videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
        "archives": [".zip", ".rar", ".7z"],
        "others": []
    }
    
    for file_name in os.listdir(desk_path):
        file_path = os.path.join(desk_path, file_name)
        os.chmod(file_path, path_perm)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            moved = False
            
            for folder_name, extensions in fill_types.items():
                if extension in extensions:
                    target_folder = os.path.join(desk_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)
                    moved = True
                    break
            
            if not moved:
                target_folder = os.path.join(desk_path, "others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)

desktop_cleaner()
'''

import os
import shutil

def desktop_cleaner():
    # Organizes the files based on the extension.
    
    desk_path = os.path.join(os.path.expanduser("~"), "OneDrive")
    print(f"Desktop path: {desk_path}")  # Debugging line
    path_perm = 0o755
    fill_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
        "videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
        "archives": [".zip", ".rar", ".7z"],
        "others": []
    }
    
    for file_name in os.listdir(desk_path):
        file_path = os.path.join(desk_path, file_name)
        
        # Skip if the file path does not exist
        if not os.path.exists(file_path):
            print(f"File does not exist: {file_path}")  # Debugging line
            continue
        
        os.chmod(file_path, path_perm)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            moved = False
            
            for folder_name, extensions in fill_types.items():
                if extension in extensions:
                    target_folder = os.path.join(desk_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    
                    print(f"Moving file: {file_path} to {target_folder}")  # Debugging line
                    try:
                        shutil.move(file_path, target_folder)
                    except Exception as e:
                        print(f"Error moving file: {e}")  # Debugging line
                    moved = True
                    break
            
            if not moved:
                target_folder = os.path.join(desk_path, "others")
                os.makedirs(target_folder, exist_ok=True)
                print(f"Moving file to others: {file_path}")  # Debugging line
                try:
                    shutil.move(file_path, target_folder)
                except Exception as e:
                    print(f"Error moving file to others: {e}")  # Debugging line

desktop_cleaner()
