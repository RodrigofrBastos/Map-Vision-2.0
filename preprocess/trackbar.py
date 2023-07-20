# import the opencv library
import cv2
import numpy as np

# uma função de callback vazia
def nothing(x):
    pass

def start_trackers(vDefaults = None):
    # Create a window
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('HMin','image',0,179,nothing) # Hue is from 0-179 for Opencv
    cv2.createTrackbar('SMin','image',0,255,nothing)
    cv2.createTrackbar('VMin','image',0,255,nothing)
    cv2.createTrackbar('HMax','image',0,179,nothing)
    cv2.createTrackbar('SMax','image',0,255,nothing)
    cv2.createTrackbar('VMax','image',0,255,nothing)

    if(isinstance(vDefaults, list)):
        # Set default value for MAX HSV trackbars.
        cv2.setTrackbarPos('HMin', 'image', vDefaults[0])
        cv2.setTrackbarPos('HMax', 'image', vDefaults[1])

        cv2.setTrackbarPos('SMin', 'image', vDefaults[2])
        cv2.setTrackbarPos('SMax', 'image', vDefaults[3])

        cv2.setTrackbarPos('VMin', 'image', vDefaults[4])
        cv2.setTrackbarPos('VMax', 'image', vDefaults[5])

    else:
        # Set default value for MAX HSV trackbars.
        cv2.setTrackbarPos('HMax', 'image', 179)
        cv2.setTrackbarPos('SMax', 'image', 255)
        cv2.setTrackbarPos('VMax', 'image', 255)

def get_trackers():
    hMin = cv2.getTrackbarPos('HMin','image')
    sMin = cv2.getTrackbarPos('SMin','image')
    vMin = cv2.getTrackbarPos('VMin','image')

    hMax = cv2.getTrackbarPos('HMax','image')
    sMax = cv2.getTrackbarPos('SMax','image')
    vMax = cv2.getTrackbarPos('VMax','image')
    return hMin, hMax, sMin, sMax, vMin, vMax
  
# define a video capture object
print('inicializando webcam ...')
#               hMin, hMax, sMin, sMax, vMin, vMax
list_default = [104, 110, 150, 199, 127, 184]

start_trackers(list_default)
vid = cv2.VideoCapture(0)
print('configuração concluída')

while(True):
    # Capture the video frame by frame
    ret, frame = vid.read()
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    h_min, h_max, s_min, s_max, v_min, v_max = get_trackers()

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # Criação de máscara com base nos limites estabelecidos
    mask = cv2.inRange(imgHSV,lower,upper)
    #cv2_imshow(mask)

    #Recorte da região delimitada pela máscara
    imgResult = cv2.bitwise_and(frame,frame,mask=mask)
    # Display the resulting frame
    cv2.imshow('image', imgResult)
    


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()