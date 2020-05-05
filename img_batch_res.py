import cv2
import glob
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dimensions", default=512, help="Images will be resized to 512x512 by default.")
parser.add_argument("-fn", "--filename", default="image-")
args = parser.parse_args()

start_time = time.clock()
m_path = os.path.abspath(".")
s_path = m_path+"/*"
d_path = m_path+"/resized"

is_file = os.path.isfile(d_path)

if is_file == True:
    os.mkdir(d_path)
elif is_file == False:
    pass

filename = str(args.filename)
d_width = d_height = int(args.dimensions) 
counter = 0

for image in glob.glob(s_path):
    if image.endswith(".jpg") or image.endswith(".png"):
        counter += 1
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        dim = (d_width, d_height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        img_count = str(counter).zfill(5)
        cv2.imwrite((d_path+"/"+filename+str(img_count)+".jpg"), resized)
        print(str(img_count)) 
    else:
        pass

print("\n")
print("Processing time:")
print(time.clock() - start_time, "Seconds"+"\n") 
time.sleep(1)
print("All images succesfully resized to:\n"+str(resized.shape)+"\n")
time.sleep(1)
print("Files saved to:\n"+str(d_path)+"\n")
time.sleep(1)





        
