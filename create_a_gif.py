#I already used pip3 install imageio
import imageio.v3 as iio

filenames = ['elmo-1.png','elmo-2.png','elmo-3.png','elmo-4.png','elmo-5.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('elmo.gif',images,duration = 200,loop =0)
