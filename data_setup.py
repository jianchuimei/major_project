import os
import shutil
import sys
print("INFO: Going to dataset folder.")
os.chdir('dataset')

if not('data' in os.listdir()):
    os.mkdir('data')
    print("INFO: data folder not found. Created data folder.")
else:
    print("INFO : data folder already exist. No new one is created.")
print("INFO: Going to 'Braille Dataset' folder.")
os.chdir("Braille Dataset")
print("INFO: Finding all files and taking all first characters.")
files = os.listdir()
ch = list(set([file[0] for file in files]))

print("INFO: Going to data folder.")
os.chdir('../data')
print('INFO: Creating folder for each characters.')
for i in ch:
    if not (i in os.listdir()):
        os.mkdir(i)
    else:
        print(f"    >> {i} folder already exist.")
print("INFO: Copying filses to its respective folder (i.e folder name with their name's first character.)")
os.chdir('../Braille Dataset')
files = os.listdir()
copy_files=0
skip_files=0
for file in files:
    folder_name = file[0]
    f=os.listdir(f'../data/{folder_name}')
    # print(f"=={f}+++++++{file}')")
    # sys.exit()
    if f'{file}' in f:
        skip_files+=1
        print(f"    >> {file} already exist.")
    else:
        shutil.copy(file, f'../data/{folder_name}')
        copy_files+=1
if copy_files:
    print(f"INFO: {copy_files} files copied and {skip_files} skipped.")
else:
    print(f"INFO: No files copied and {skip_files} skipped.")
