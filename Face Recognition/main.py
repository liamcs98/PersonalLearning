# Goals:
# Find and rip all faces from given directory + subs
# If given input directory, find same people and move to individual dirs

# Shoot the moon goals
# Try to find matching people without input
# create HTML report, with links to photos, catagorized by person,
# include image meta data
# Video support?

from PIL import Image
import face_recognition
import os


def makeNeededDirectories():
	cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd + "/Found")):
        os.makedirs(os.path.join(cwd + "/Found"))
    if not os.path.exists(os.path.join(cwd + "/Known")):
    	os.makedirs(os.path.join(cwd + "/Known"))
    if not os.path.exists(os.path.join(cwd + "/output")):
    	os.makedirs(os.path.join(cwd + "/output"))

def createImageList(path="Defualt"):
	pictureList = []
	if path == "Defualt":
		for rawImage in os.listdir("/Unknown_pictures"):
    		if rawImage.find(".jpg") > -1:
    			pictureList.append(rawImage)
    return pictureList

# Does Three things since I dont have enough ram =C
def loadImageAndDetectAndSave(imageList):
	facesFound = 0
	for image in imageList:
		#Load into Array
		imageArray = face_recognition.load_image_file(image)
		#Detect Face
		face_locations = face_recognition.face_locations(imageArray)

		#Save Found face
		if len(face_locations) > 0:
			top, right, bottom, left = face_location
            #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            #Add a little Buffer
            face_image = image[top - 20:bottom + 20, left - 20:right + 20]
            pil_image = Image.fromarray(face_image)
            pil_image.save("/Found/" + str(facesFound) + ".PNG", "PNG")

def EncodedImagesForComarison(path="Defualt"):
	compList = []
	for x in os.listdir("/Input"):
		imageArray = face_recognition.load_image_file(x)
	#If a face is found	
	if len(face_recognition.face_encodings(imageArr)) > 0:
    	face_encoding = face_recognition.face_encodings(imageArray)[0]

    	compList.append((x,face_encoding))

    return compList

def CompareFaces(imageList, compareList):
	for image in imageList:
		#Load into Array
		#imageArray = face_recognition.load_image_file(image)
		
		#Should Be only one face
		if len(face_recognition.face_encodings(imageArr)) > 0:
        	unknown_face_encoding = face_recognition.face_encodings(imageArr)[0]
		
		for name, encodedFace in compareList:
			results = face_recognition.compare_faces(encodedFace, unknown_face_encoding)
			if True in results:
            	print("Found {} in {}".format(name, image))



if __name__ == '__main__':
	makeNeededDirectories():

	imageList = createImageList():

