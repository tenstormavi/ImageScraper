#!/usr/bin/python

import os, sys
from PIL import Image
import glob
import shutil

if not os.path.exists('cropimages'):
    os.makedirs('cropimages')

def resize1(img, box, out):
    factor = 1
    while img.size[0]/factor > 2*box[0] and img.size[1]*2/factor > 2*box[1]:
        factor *=2
    if factor > 1:
        img.thumbnail((img.size[0]/factor, img.size[1]/factor), Image.NEAREST)

    if factor > 1:
        x1 = y1 = 0
        x2, y2 = img.size
        wRatio = 1.0 * x2/box[0]
        hRatio = 1.0 * y2/box[1]
        if hRatio > wRatio:
            y1 = int(y2/2-box[1]*wRatio/2)
            y2 = int(y2/2+box[1]*wRatio/2)
        else:
            x1 = int(x2/2-box[0]*hRatio/2)
            x2 = int(x2/2+box[0]*hRatio/2)
        img = img.crop((x1,y1,x2,y2))


    img.thumbnail(box, Image.ANTIALIAS)

    img.save(out, "JPEG", quality=75)

box = (200,200)
files = glob.glob('./scrapimages/*.jpg')
for filename in files:
    img = Image.open(filename)
    if img.size[0]<200 and img.size[1]<200:
        img = Image.open(filename).resize((200,200),Image.ANTIALIAS)
        out = file(os.path.splitext(filename)[0]+"_crop.jpg", "w")
        img.save(out, "JPEG")
        out.close()
    else:
        out = file(os.path.splitext(filename)[0]+"_crop.jpg", "w")
        resize1(img,box,out)

count = 0
sel = glob.glob('./scrapimages/*_crop.jpg')
for file in sel:
    m = './cropimages'
    shutil.move(file,m)
print "Done! All images are resized."
