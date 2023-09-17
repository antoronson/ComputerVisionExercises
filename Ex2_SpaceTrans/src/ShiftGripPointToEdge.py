import mmap
import numpy

class ShiftGripPosToPartEdge:
    labelLength = 100   #In mm
    labelWidth  = 50    #In mm
    labelOff_X  = 10    #In mm
    labelOff_y  = 5     #In mm
    labelTheta  = 0
    
    #------------------------
    # Cam Params
    #------------------------
    thetaUF = 0
    thetaActPart = 0
    def __init__(self, labelL, labelW, labelOffX, labelOffY, labelTheta):
        self.labelLength = labelL
        self.labelWidth = labelW
        self.labelOff_X = labelOffX
        self.labelOff_Y = labelOffY
        self.labelTheta = labelTheta


    def RotateCamFrameToUserFrame(self, _Angle):
        self.thetaUF = -360-_Angle

        if self.thetaUF <-360:
            self.thetaUF+=360

        else:
            #Do Notning
            #TODO: Catch Error here
            return 0
            
    

    def setActPartRotation(self, _Angle):
        self.thetaActPart = self.thetaActPart + self.labelTheta
    
   def  


