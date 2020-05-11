import os

def createIfNotExist(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def move(folderName, files):
	for file in files:
		os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove('DesktopCleaner.py')
#print(files)

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Others')

imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
#print(images)

docExts = [".pdf", ".doc", ".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
#print(docs)

mediaExts = [".mkv", ".mp3", ".mp4"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
#print(media)

others = []
for file in files:
	ext = os.path.splitext(file)[1].lower()
	if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
		others.append(file)
print(others)
move("Images", images)
move("Docs", docs)
move("Media", media)
move("Others", others)
