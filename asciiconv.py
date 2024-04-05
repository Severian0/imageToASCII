from PIL import Image
def imgToASCII(image,filetype,savepath,scale):
    scale = int(scale)

    # open and get image size
    img = Image.open(image)
    width,height = img.size

    # resize image (downscale)
    img.resize((width//scale, height//scale)).save("resized.%s" % filetype)

    # open new image
    img = Image.open("resized.%s" % filetype)
    width, height = img.size # get new width and height 


    # list with correct length and height (same as resized image)
    array = []
    for i in range(height):
        array.append(["X"] * width)
       

    pixelimg = img.load()

    for i in range(height):
        for j in range(width):
            if sum(pixelimg[j,i]) == 0:
                array[i][j] = '#'
            elif sum(pixelimg[j,i]) in range(1,100):
                array[i][j] = 'X'
            elif sum(pixelimg[j,i]) in range(100,200):
                array[i][j] = '%'
            elif sum(pixelimg[j,i]) in range(200,300):
                array[i][j] = '&'
            elif sum(pixelimg[j,i]) in range(300,400):
                array[i][j] = '*'
            elif sum(pixelimg[j,i]) in range(400,500):
                array[i][j] = '+'
            elif sum(pixelimg[j,i]) in range(500,600):
                array[i][j] = '/'
            elif sum(pixelimg[j,i]) in range(600,700):
                array[i][j] = '('
            elif sum(pixelimg[j,i]) in range(700,750):
                array[i][j] = '\''
            else: array[i][j] = ' '


    final = open(savepath, "w")
    for i in array:
        final.write("".join(i)+'\n')

    final.close()

imaaj = input()
filetyp = input()
saveas = input()
scale = int(input())

imgToASCII(imaaj,filetyp,saveas,scale)
