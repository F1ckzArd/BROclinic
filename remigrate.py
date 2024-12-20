import os, shutil, sys 
 
def delete_migrations_folders(root_folder): 
    for root, dirs, files in os.walk(root_folder): 
        if not root.startswith('./venv'): 
            for dir_name in dirs: 
                if dir_name == "migrations": 
                    folder_path = os.path.join(root, dir_name) 
                    print(f"Cleaning folder: {folder_path}") 

                    for subroot, subdirs, subfiles in os.walk(folder_path): 
                        for i in subdirs: 
                            shutil.rmtree(os.path.join(subroot,i)) 
                        for i in subfiles: 
                            os.remove(os.path.join(subroot,i)) 
                         
                        with open(os.path.join(subroot,'__init__.py'),'w'): 
                            pass 
                    break 
 
root_folder = "" 
 
delete_migrations_folders("./") 
if os.path.exists(os.path.join(root_folder,'db.sqlite3')): 
    os.remove(os.path.join(root_folder,'db.sqlite3')) 
 
if '-n' in sys.argv: 
    sys.exit() 

prefix = 'py'  
os.system(prefix+' manage.py makemigrations') 
os.system(prefix+' manage.py migrate') 
os.system(prefix+' manage.py shell -c "from seeding.seed import seed;seed();"') 