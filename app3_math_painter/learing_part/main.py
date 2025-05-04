import numpy as np
from PIL import Image
data=np.zeros((5,4,3),dtype=np.uint8)
data[:]=[255,255,0]
print(data)

data[0:2,0:2]=[255,0,0]
data[2:4,1:3]=[40,40,0]
print(data)

img=Image.fromarray(data,'RGB')
img.save("canva.png")