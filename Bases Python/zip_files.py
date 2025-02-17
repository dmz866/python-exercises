import zipfile
import shutil

'''
#Create zip file
zip_file = zipfile.ZipFile('zip_file.zip', 'w')
zip_file.write('test.txt')
zip_file.write('test2.txt')
zip_file.close()

#Unzip file
zp = zipfile.ZipFile('zip_file.zip', 'r')
zp.extractall()

'''
#Unzip file
shutil.unpack_archive('zip_file.zip', 'new folder unzip name')


