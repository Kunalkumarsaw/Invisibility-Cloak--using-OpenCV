# Invisibility-Cloak--using-OpenCV
If you are a Harry Potter fan , you would know what an Invisibility Cloak is. We will make this happen with few line of python code in OpenCV Library .

Today we will be writting codes for static  Invisibility Cloak .

Follow the clock_invisivble.py for the code

Some of the QNA 's 

why do we convert BGR colour code to HSV colour code?
ans- R, G, B in RGB are all co-related to the color luminance( what we loosely call intensity),i.e., We cannot separate color information from luminance. HSV or Hue Saturation Value is used to separate image luminance from color information. This makes it easier when we are working on or need luminance of the image/frame. 
For more refrence https://stackoverflow.com/questions/17063042/why-do-we-convert-from-rgb-to-hsv/17063317#:~:text=R%2C%20G%2C%20B%20in%20RGB,luminance%20of%20the%20image%2Fframe.

why do we use  mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) code?
ans- It is useful in removing noise for more referr https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

why do we use     mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8)) ?
ans-, this maximizing operation causes bright regions within an image to “grow" for more refer https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html

Some of the HSV color codes are 

#color_identifier(np.array([0, 0, 70]), np.array([100, 255,255]) ##for red
#color_identifier(np.array([55,64,64]), np.array([94,255,255])) ##for green

IF you have diffrent color cloth you can track your own colour using the tracker and change the values of Lower red and Upper red from here
 lower_red = np.array([0, 120, 50])
 upper_red = np.array([10, 255,255])
For more details refer tracking_color.py 

You can also refer youtube for more elobaration and understanding 
https://www.youtube.com/watch?v=AkY2TpvDGUo&list=LL6u4PdXLXZkfLz6Q0Yp68Yw&index=4&t=2416s

 
