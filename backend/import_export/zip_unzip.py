from zipfile import ZipFile
import os
from create_app import app

def zip_files(user_id,file_path_list):
    zip_file_name = None
    flag = True
    try:
        zip_file_name = str(user_id)+"_exported_as_zip.zip"
        
        with ZipFile(zip_file_name,'w') as zip:
            for file in file_path_list:
                zip.write(file)
            zip.write('Instructions.pdf')
    except Exception as e:
        flag = False
        for each in file_path_list:
            os.remove(each)
    finally :
        if flag:
            for each in file_path_list:
                os.remove(each)
        return zip_file_name
