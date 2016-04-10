import cv2
import os

def resizeInBatch(inputImageDir, outputImageDir, newSize=(224, 224)):
	assert(len(newSize) == 2)
	inputImageNames = os.listdir(inputImageDir)
	for inputImageName in inputImageNames:
		inputImage = os.path.join(inputImageDir, inputImageName)
		outputImage = os.path.join(outputImageDir, inputImageName)
		resize(inputImage, outputImage, newSize)

def resize(inputImage, outputImage, newSize=(224, 224)):
	assert(len(newSize) == 2)
	oriImage = cv2.imread(inputImage)
	newImage = cv2.resize(oriImage, newSize)
	cv2.imwrite(outputImage, newImage)