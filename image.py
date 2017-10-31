### This program convert Image to text and also write them into text file
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

## Capture image and convert to text and return variable
def getimage(img_path):
im = Image.open(img_path) # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp.jpg')
text = pytesseract.image_to_string(Image.open('vinRead2.jpg'))
return text
#print getimage("vinRead5.jpg");

### remove the blank lines
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line
			


print ('***********************writing into text file**********************************')
## Writing into text file 
file = open('temp.txt','w') 

file.write(text.encode("utf-8"))
file.close()
print ('********************************************************************************')


print ('***********Reading from Text file**************************************')
## Reading from file
with open('temp.txt') as f:
    #for line in f:
        
    for line in nonblank_lines(f):    
        print line

print ('********************************************************************************')
			


