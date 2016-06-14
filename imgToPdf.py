#imToPdf - program that exports a list of images and converts them to a pdf.
from __future__ import division
import os

from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from StringIO import StringIO


def main():
    images = image_search()
    output = PdfFileWriter()
    for image in images:
        Image_file = Image.open(image)     # need to convert the image to the specific size first.
        width, height = Image_file.size
##        Image_file.resize = ((200, 200))   # Change the size using tuple assignments
##        resized_image = "resized" + image
##        Image_file.save(resized_image)

        im_width = 1 * cm

        # Using ReportLab to insert image into PDF
        ##imgTemp = StringIO()
        watermark_str = "watermark" + str(images.index(image)) + '.pdf'
        imgDoc = canvas.Canvas(watermark_str)

        # Draw image on Canvas and save PDF in buffer
        ##imgPath = r"C:\Users\Ope O\Pictures\cat.png"
        aspect = height / float(width)
        print aspect
        imgDoc.drawImage(image, 0,0, width = im_width, height = (im_width * aspect))    ## at (399,760) with size 160x160

        imgDoc.showPage()
        imgDoc.save()
        # Get the watermark file just created
        watermark = PdfFileReader(open(watermark_str, "rb"))

        #Get our files ready
        pdf1File = open('sample.pdf', 'rb')
        page = PdfFileReader(pdf1File).getPage(0)
        page.mergePage(watermark.getPage(0))


        #Save the result

        output.addPage(page)
    
    #write the output to the pdf file    
    output.write(file("output.pdf","wb"))


#Create a function to search the current user directory for images to aggregate.
def image_search():
    found_images = []                   #initialize a list to store the file names of images found.
    for doc in os.listdir(os.curdir):         #get all the files in current directory. the path specified as argument is the current directory
        image_ext = ['.jpg', '.png', '.PNG', '.jpeg', '.JPG']             #check for files that end with these
        for ext in image_ext:
            if doc.endswith(ext):
                found_images.append(doc)
    return found_images

main()



