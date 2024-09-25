import cv2

img = cv2.imread("sample/galaxy.jpg", 1)

print(img)
print(img.shape)

resize_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxi", resize_image)

cv2.imwrite("sample/Resized_galaxy.jpg", resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()