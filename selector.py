import cv2
import random
import math

def getRectBoxByImage(inputImage):
	img = cv2.imread(inputImage)
	size = (img.shape[0], img.shape[1])
	boxSize = (img.shape[0] / 4, img.shape[1] / 4)
	return getRectBox(size, boxSize)

def getRectBox(imageSize, boxSize):
	# this function takes random rect box inside the center
	# of any resized image, size = 224 * 224 for example
	iw, ih = imageSize
	bw, bh = boxSize
	assert(iw / 2 > bw and ih / 2 > bh)

	x = random.choice(range(iw / 2 - bw)) + int(math.floor(0.25 * iw))
	y = random.choice(range(ih / 2 - bh)) + int(math.floor(0.25 * ih))

	# assert ( (iw / 4 <= x <= iw / 4 * 3) or (ih / 4 <= y <= ih / 4 * 3))

	return (x, x + bw, y, y + bh)
	


