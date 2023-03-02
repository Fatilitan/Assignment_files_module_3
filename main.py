__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

base_path = os.getcwd()
this_file_path = os.path.join(base_path, 'files')
cache_path = os.path.join(this_file_path, "cache")
data_zip_path = os.path.join(this_file_path, 'data.zip')

def clean_cache():
    cache_folder = "cache"
    print(base_path)
    if os.path.exists(cache_path):
        print('bestaat wel')
        for files in os.listdir(cache_path):
            os.remove(os.path.join(cache_path, files))
    else:
        print('bestaat niet')
        os.chdir(this_file_path)
        os.makedirs(cache_folder)
        os.chdir(base_path)

def cache_zip(zip_file, cache_dir):
    with ZipFile(zip_file, 'r') as zip:
        zip.extractall(path=cache_dir)

def cached_files():
    file_list = []
    for files in os.listdir(cache_path):
        file = os.path.join(cache_path, files)
        file_list.append(file)
    return file_list

#=============================================================================================================#
# find_password() werkt niet volgens wincpy, maar in de console werkt hij wel, misschien met wincpy te maken? #
#=============================================================================================================#

def find_password(file_list):
    word = 'password'
    password = ''
    for files in file_list:
        with open(files) as f:
            for line in f.readlines():
                if word in line:
                    password += line
    password = password.replace('password: ', '')
    return password


# clean_cache()
# cache_zip(data_zip_path, cache_path)
file_list = cached_files()
print(find_password(file_list))