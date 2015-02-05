#!/usr/bin/python

import sys
from lxml import html
import requests
import os
import glob

def checking(links):
    arr=[]
    for m in links:
        if(m[-3:]=="jpg" or m[-3:]=="png" or m[-3:]=="gif"):
            arr.append(m)
    return arr

name = raw_input("Enter the name of the picture: ")
URL = "https://www.google.com/search?site=&tbm=isch&q=%s"%name
page = requests.get(URL)

c = html.fromstring(page.text)
img = c.xpath('//img/@src')
links = c.xpath('//a/@href')
img_links =  checking(links)
img.extend(img_links)

if len(img)==0:
    sys.exit( "Sorry, no images found!")

print "%s images of %s are available for download: "%(len(img),name)

imgdownload = int(raw_input('How many images you want to download? : '))

for x  in range(0,len(img)):
    if  img[x][:4]!="http":
        img[x]="https:"+img[x]

if not os.path.exists('scrapimages'):
    os.makedirs('scrapimages')

count=0
failed=0

for img_url in img :
    try:
    	store = requests.request('get',img_url)
    	z = open('scrapimages/%s' % img_url.split('/')[-1], 'w')
    	z.write( store.content)
    	z.close()
	count+=1
    except:
        failed +=1
    if count==imgdownload:
        	break

rem = 0
files = glob.glob('./scrapimages/images*')
for file in files:
    rem+=1
    new_name = './scrapimages/'+(str(rem) +'.jpg')
    os.rename(file, new_name)


print
print "Done. %s images downloaded!"%count
print "%s images failed to download!"%failed

