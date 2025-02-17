import zipfile

zip_file = zipfile.ZipFile('zip_file.zip', 'w')
zip_file.write('test.txt')
zip_file.write('test2.txt')
zip_file.close()
