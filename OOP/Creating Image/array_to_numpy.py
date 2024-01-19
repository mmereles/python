import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtype=np.uint8)
print(data)
data[:] = (255,255,0)
print(data)



data[0:3, 0:2] = [255,0,0]
print(data)
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')