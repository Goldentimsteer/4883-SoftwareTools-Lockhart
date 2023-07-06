from wand.image import Image 




germany = Image(filename = '1.jpg')

#prints image info
print (germany.height, germany.width)
#convrts to png
germany_convert = germany.convert('PNG')
germany.save(filename = 'converted germany.png')


 #blurse the image
germany.blur(sigma = 4)
germany.save(filename ="germany blur.jpg")


#flips image

flip_germany = germany.clone()
flip_germany.flip()  
flip_germany.save(filename ='flip germany.jpg')
