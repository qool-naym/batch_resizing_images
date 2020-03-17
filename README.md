# Batch Resizing Images

Short Python script for batch resizing images. Intentionally to be used for preparing lots of images for dataset compiling.

### What you need to do:

Just put the folder containing your images and your destination folder in the same directory as ```img_batch_res.py``` . 

Within ````img_batch_res.py```` replace ```"/source_folder/*"``` and ```"/destination_folder/" ``` with the names of your folders.
Make sure NOT to remove ```*``` on ```/source_folder/*```.
By default your images will be resized to 512x512, you can adjust the dimensions by changing ```d_width, d_height``` to any tuple of positive integers.
 
Output files will be named ```image-0001``` , ```image-0002``` , etc. If you want to use a different name, change the value of ```filename``` to any name you prefer (must be a string). If you need more than 4 digits added after the name, just fill in more zeros by changing ```str(counter).zfill(4)``` to ```str(counter).zfill(5)``` or to any other positive integer.

The script will convert any images to and output ```.jpg``` files.
