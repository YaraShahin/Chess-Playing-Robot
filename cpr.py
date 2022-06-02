import cv2
import numpy as np

#Take a picture once the button has been pressed
def snap():
    vid = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    ret, img = vid.read()
    cv2.imwrite("img.png", img)
    cv2.imshow("img", img)
    cv2.waitKey()
    return img

#function for drawing circles or numbers (if flag) for debugging
def draw(img,start, end, flag = False, n = 0):
    cv2.circle(img, (start, end), 3, (0,0,255), -1)
    if (flag):
        cv2.putText(img, str(n), (start, end), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))


#function to show an opencv img for debugging
def show(img):
    cv2.imshow("img", img)
    cv2.waitKey()

#draw numbered dots on chess board corners
def numbered(img, final):
    n = 0
    print(final)
    for i in final:
        cv2.putText(img, str(n), (i[0], i[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
        cv2.circle(img, (i[0], i[1]), 3, 255, -1)
        n = n+1
    return img

#Crop the picture taken to only include the area of interest (only once before the game starts)
#findchesscorners is almost 100% accurate, but can't show the outer corners; it can't detect shit when there are pieces
#For this function to work, the top left and bottom right squares have to be black
def crop(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    returnCode, corners = cv2.findChessboardCorners(gray, (7, 7), None)
    c = []
    for i in corners.tolist():
        c.append(i[0])
    startrows = int(c[48][0]-(c[41][0]-c[48][0])*1.3)
    startcolumns = int(c[48][1]-(c[47][1]-c[48][1])*1.30)
    endrows = int(c[0][0]+(c[0][0]-c[7][0])*1.30)
    endcolumns = int(c[0][1]+(c[0][1]-c[1][1])*1.30)
    stC = min(endcolumns, startcolumns)
    edC = max(endcolumns, startcolumns)
    stR = min(endrows, startrows)
    edR = max(endrows, startrows)
    cropped = img[stC:edC, stR:edR]
    return cropped, (stC, edC, stR, edR)

#Divide the chess board into 64 squares that each contain a chess piece or not (only once before the game starts)
#goodFeats is not accurate, but shows the corners even when there are pieces on the chess board
def goodFeats(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 81, 0.01, 10)

    corners = np.int0(corners)
    goodFeatsList = []
    for p in corners.tolist():
        goodFeatsList.append(p[0])
    return goodFeatsList

def sortIt(goodFeatsList):
    points = sorted(goodFeatsList)
    final = []
    for i in range(8, -1, -1):
        temp = []
        for j in points[9*i:9+9*i]:
            temp.append(j)
        temp.sort(key=lambda k: (-k[1], k[0]), reverse=False)
        for k in temp:
            final.append(k)
    return final

def debug():
    img = cv2.imread("img.png")
    img, cropCR = crop(img)
    goodFeatsList = goodFeats(img)
    final = sortIt(goodFeatsList)
    img = numbered(img, final)
    cv2.imshow("img",img)
    cv2.waitKey()

debug()

def once():
    #button pressed, image taken
    img = snap()
    #image cropped 
    img, cropCR = crop(img)
    #detect chess corners
    goodFeatsList = goodFeats(img)
    #get sorted chess corners list
    final = sortIt(goodFeatsList)
    return cropCR, final

def tillEnd(cropCR, final):
    #button pressed, image taken
    img = snap()
    #crop the image according to the prev detected startCols, endCols, startRows, endRows
    img = img[cropCR[0]:cropCR[1], cropCR[2]:cropCR[3]]


    

"""
if __name__ == "__main__":
    main()
"""
