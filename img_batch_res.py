import cv2
import glob
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dimensions", default=512, help="")
parser.add_argument("-fn", "--filename", default="image-", help="")
args = parser.parse_args()

start_time = time.clock()
m_path = os.path.abspath(".")
s_path = m_path+"/source_folder/*"
d_path = m_path+"/destination_folder/"
filename = str(args.filename)
d_width = d_height = int(args.dimensions) 
counter = 0

for image in glob.glob(s_path):
    counter += 1
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    dim = (d_width, d_height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    img_count = str(counter).zfill(4)
    cv2.imwrite((d_path+filename+str(img_count)+".jpg"), resized)
    print(str(img_count)) 

print("\n")
print("Processing time:")
print(time.clock() - start_time, "Seconds"+"\n") 
time.sleep(1)
print("All images succesfully resized to:\n"+str(resized.shape)+"\n")
time.sleep(1)
print("Files saved to:\n"+str(d_path)+"\n")
time.sleep(1)





        
