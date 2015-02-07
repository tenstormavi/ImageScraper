Detailed Working
================

imgscrapper.py
--------------
A web-scraper in python to scrape google image results for a given search term.
And save them in a folder with names like 1.jpg, 2.jpg, 3.jpg, etc. where 1, 2,
3 are there
search result ranking.

imgprocess.py
-------------
An image processing script to iterate over all the scrap images and reduce
every image to 200x200 pixels.
This reduction is satisfying the following conditions:

1. The images is not stretched on the axes, i.e. the aspect ration is maintained.

2. For images which do not have the aspect ratio of 1:1, the extra length or width is be cropped.

3. If cropped, the resulting image is from the center of the original image.

4. The cropped image should be saved in a separate directory, with _crop suffix to the file name e.g. 1.jpg becomes 1_crop.jpg
