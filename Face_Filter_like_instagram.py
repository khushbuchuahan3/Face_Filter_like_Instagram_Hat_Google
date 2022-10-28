import cv2

img=cv2.imread("1.jpeg") #Image
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Greyimage
mustech=cv2.imread("ms.png") #mustech
glass=cv2.imread("glasses.png") #Glassimage
hat=cv2.imread("hat.png") #hatimage
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #facedetectionclassifier
face=classifier.detectMultiScale(grey,1.5,3)


def put_glasses(glass,fc,x,y,w,h): #userdefine function for glass position
    face_width=w
    face_height=h
    hat_width=face_width+1
    hat_height=int(0.5*face_height)+1
    glass=cv2.resize(glass,(hat_width,hat_height))
    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y+i -int(-0.20*face_height)][x+j][k]=glass[i][j][k]
    return fc


def put_hat(hat,fc,x,y,w,h): #userdefine function for hat position
    face_width=w
    face_height=h
    hat_width=face_width+1
    hat_height=int(0.5*face_height)+1
    glass=cv2.resize(hat,(hat_width,hat_height))
    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y+i -int(0.50*face_height)][x+j][k]=glass[i][j][k]
    return fc




#User define function for Facedetection
for x,y,w,h in face:
    frame=put_hat(hat,img,x,y,w,h)
    frame=put_glasses(glass,img,x,y,w,h)
    cv2.imshow("img",img)
cv2.waitKey(0)
