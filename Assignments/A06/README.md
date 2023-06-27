A06 - Imagemagick
Imagemagick is a tool that is able to manipulate images
One of the things you can do with ImageMagick is get information about an image
```
 identify (filename)
```
this will not pull alot of information if you want some more info type 
```
 identify - verbose (filename)
```
This will bring up alot more info like the image type the size and much more

If you want to change the type of image the file 
Ex: a jpg into a png 
```
convert (filename) (filename).png
```
for making the image having a diffrent size you would use the same convert but would have -resize then the ratio yo would want it

```
 convert (filename) -resize AxB (new filename)
```
now if you look at the image info the image did not actually make it the exact size you asked it.
it kept the same ratio but just increased it to the lenght yo set
to make it exactly what you asked all you have to do is type
```
convert (filename) -resize AxB\! (new filename)
```

for changing the contrast of the image you would do the same thing of using convert but you will put -paint (number)
```
convert  thumbnail_IMG_8355.jpg -paint 20  (filename)
```
for making a image swirled instead of paint you use swirl

```
convert  thumbnail_IMG_8355.jpg -swirl 180  (filename)
```
This is just the begining of imagemagick for more info go to https://imagemagick.org/
