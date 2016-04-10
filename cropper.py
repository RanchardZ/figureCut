import cv2

def crop(inputImage, outputImage, xstart, xend, ystart, yend):
	assert(0 < xstart < xend and 0 < ystart < yend)
	oriImage = cv2.imread(inputImage)
	assert(xend < oriImage.shape[1] and yend < oriImage.shape[0])
	cropImage = oriImage[xstart: xend, ystart: yend]
	cv2.imwrite(outputImage, cropImage)