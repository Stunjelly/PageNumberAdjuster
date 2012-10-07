import os

folder = "C:\wamp\www\parker\working\plus1"
os.chdir(folder)
for image in os.listdir(folder):
	base = image[:-4]
	num = base[4:]
	os.rename(image, '_page'+str(int(num)+1)+'.jpg')
	#os.rename(image, image[1:])