import cv2
import glob
import os

images = glob.glob("sample/*.jpg")

target_width = 500

for image in images:
     #Read the image
     img = cv2.imread(image, 1)

     #Get the Original Dimention
     original_width, original_height = img.shape[:2]

     # Calculate the target height while maintaining the aspect ratio
     aspect_ratio = original_width / original_height
     target_height = int(target_width * aspect_ratio)

     #Resize the image
     resize = cv2.resize(img, (target_width, target_height))

     #Display the resized image
     cv2.imshow("New size image", resize)
     cv2.waitKey(500)
     cv2.destroyAllWindows()

     filename = os.path.basename(image)
     cv2.imwrite(f"sample/500_{filename}",resize)