import cv2

def replace(holderImage, cropperImage, outputImage, xstart, xend, ystart, yend):
	holder = cv2.imread(holderImage)
	cropper = cv2.imread(cropperImage)
	holder[xstart: xend, ystart: yend] = cropper[:, :]
	cv2.imwrite(outputImage, holder)
