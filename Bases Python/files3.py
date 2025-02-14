from pathlib import Path, PureWindowsPath
# Use Path for any OS. No double backslashes for windows
'''

folderRoute = Path('C:/Users/dmz86/OneDrive/Desktop')
fileName = folderRoute / 'test33.txt'

print(folderRoute, fileName)

a = open(fileName)
print(a.read())



'''
#################################################################
file = Path('C:/Users/dmz86/OneDrive/Desktop/test33.txt')
# Content, name, extension
print(file.read_text(), file.name, file.suffix)

# Convert to Windows path
print(PureWindowsPath(file))

