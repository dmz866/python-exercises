import os
import shutil
import send2trash
'''
file = open('test_file.txt', 'w')
file.write('Shi')
file.close()
'''
#list all files
#print(os.listdir())

#move files
#shutil.move('test_file.txt', 'C:\\Users\\dmz86\\Documents')

#delete and send to trash
#send2trash.send2trash('C:\\Users\\dmz86\\Documents\\test_file.txt')

# Directory tree generator
route = 'C:\\Users\\dmz86\\Documents\\Estudios\\python'

for folder, subfolders, files in os.walk(route):
    print(f'Folder: {folder}')

    for subfolder in subfolders:
        print(f'Subfolder: {subfolder}')

    for file in files:
        print(f'File: {file}')

    print('\n')

#os.unlink() deletes file
#os.rmdir() deletes empty folder


