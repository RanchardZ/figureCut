import os, sys
import random

from cropper import crop
from selector import getRectBoxByImage
from replacer import replace
from resizer import resizeInBatch

def generateCropperPool(cropperInputDir, cropperOutputDir, cropperPerImage):
	cropperImageNames = os.listdir(cropperInputDir)
	for cropperImageName in cropperImageNames:
		for i in range(cropperPerImage):
			inputImage = os.path.join(cropperInputDir, cropperImageName)
			temCropperImageName = cropperImageName.split('.')
			temCropperImageName.insert(-1, str(i+1))
			outputImage = os.path.join(cropperOutputDir, '.'.join(['_'.join(temCropperImageName[:-1]), temCropperImageName[-1]]))
			xstart, xend, ystart, yend = getRectBoxByImage(inputImage)
			crop(inputImage, outputImage, xstart, xend, ystart, yend)

def generateEmbeddedPool(cropperPoolDir, holderPoolDir, embeddedPoolDir, holderPerCropper):
	cropperImageNames = os.listdir(cropperPoolDir)
	holderImageNames = os.listdir(holderPoolDir)

	count = 1
	for cropperImageName in cropperImageNames:
		for i in xrange(holderPerCropper):
			holderImageName = random.choice(holderImageNames)
		
			holderImage = os.path.join(holderPoolDir, holderImageName)
			cropperImage = os.path.join(cropperPoolDir, cropperImageName)
			outputImage = os.path.join(embeddedPoolDir, '_'.join([holderImageName.split('.')[0], cropperImageName.split('.')[0], str(i)]) + '.jpg')
			xstart, xend, ystart, yend = getRectBoxByImage(holderImage)
			replace(holderImage, cropperImage, outputImage, xstart, xend, ystart, yend)
			count += 1

def process(cropperSourceDir, holderSourceDir, cropperPerImage, holderPerCropper):
	# resize cropper and holder images
	dirName = os.path.dirname(cropperSourceDir)
	cropperSourceResizedDir = os.path.join(dirName, 'cropperSourceResized')
	holderSourceResizedDir = os.path.join(dirName, 'holderSourceResized')

	os.mkdir(cropperSourceResizedDir)
	os.mkdir(holderSourceResizedDir)

	resizeInBatch(cropperSourceDir, cropperSourceResizedDir)
	resizeInBatch(holderSourceDir, holderSourceResizedDir)

	# generate cropper pool
	cropperPoolDir = os.path.join(dirName, 'cropperPoolDir')
	os.mkdir(cropperPoolDir)

	generateCropperPool(cropperSourceResizedDir, cropperPoolDir, cropperPerImage)

	embeddedPoolDir = os.path.join(dirName, 'embeddedPoolDir')
	os.mkdir(embeddedPoolDir)
	generateEmbeddedPool(cropperPoolDir, holderSourceResizedDir, embeddedPoolDir, holderPerCropper)

	