import os
list = []
new_folder_path = input("enter the directory you want ot organize: ")
for file_name in os.listdir(new_folder_path):
    file_path = os.path.join(new_folder_path, file_name)
    root, extension = os.path.splitext(file_path)
    destination_folder = new_folder_path + f"\\{extension[1:]}"
    destination_file = os.path.join(destination_folder, file_name)
    if(extension != ""):
        if extension not in list:
            list.append(extension)
            os.makedirs(destination_folder, exist_ok=True)
            try:
                os.rename(file_path, destination_file)
            except PermissionError:
                print(f"permission error in this file: {file_name}")
            except Exception as e:
                print(f"an error occured with {file_path} : {e}")
        else:
            os.rename(file_path, destination_file)
     

    

