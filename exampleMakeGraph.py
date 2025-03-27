# graphics.py
import time, math, random
from graphics import *

class makeGraph:
    def __init__(self, xSize, ySize):
        self.maxX = xSize # size of window
        self.maxY = ySize
        self.xSize = xSize - 100 # plotable area in graph after 100 gap
        self.ySize = ySize - 100
        self.win = GraphWin('Graph', xSize, ySize)
        self.highestY = 5000
        self.yConvert = 1
        self.addComment("ZaiPaul",(xSize-50),20, "red")
    #-----------------------------------------------
    def calcHighest(self,ylist):
        highestY = 0
        for y in range(len(ylist)):
            if ylist[y] > highestY:
                highestY = ylist[y]
        if highestY < 5000:
            highestY = 5000 # round up
        elif highestY < 10000:
            highestY = 10000 # round up
        elif highestY < 20000:
            highestY = 20000 # round up
        elif highestY < 50000:
            highestY = 50000 # round up
        elif highestY < 100000:
            highestY = 100000 # round up
        elif highestY < 500000:
            highestY = 500000 # round up
        elif highestY < 1000000:
            highestY = 1000000 # round up
        else:
            highestY = 10000000

        return highestY
    #---------------------------------------------------------------------------------------------
    def makeBackground(self,xlist, ylist, xMultiply):
        maxX = self.maxX - 200
        maxY = self.maxY
        if xMultiply < 1:
            xMultiply = 1 # stop / zero
        highestY = self.highestY
        
        l = len(xlist)
        maximumX = l
        maximumY = 0
        for y in range(len(ylist)):
            if ylist[y] > maximumY:
                maximumY = ylist[y]
        #print("X ",maximumX, " Y " , maximumY)
            
        bottom = self.ySize

        win = self.win

        xJump = 100
        xStep = 20
        if maximumX == maxX:
            xStep = maximumX / 10
            if xStep < 100:
                xStep = 100
        if maximumX > maxX: # divide down
            xStep = maximumX / 10
            xJump = int(maxX  / 10)
            print("Big step = ", xStep)

        if maximumX < maxX: # multiply up
            xStep = int(maximumX/10)
            xJump = maxX / 10

        print("x stepping" ,xStep, xMultiply)

        theRange = 10 # print 10 numbers at bottom -- int((self.xSize-100)/xStep/xMultiply) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        for x in range(theRange+1):
            if (x*xJump) < (maxX+50):
                data10 = Text(Point(((x*xJump))+100, bottom+25), str(int(x*xStep)))
                data10.draw(win)
            
        yStep = 50
        if maximumY > self.ySize: # divide down
            yStep = ( highestY /self.ySize)
        print("highest ", highestY, "max y ", maximumY, "  Stepping",yStep)
            
        for y in range(10):
            data10 = Text(Point(40, (self.ySize - (y*50))), str(y*int(highestY/10)))
            data10.draw(win)

        l = Line(Point(100,bottom), Point(self.xSize,bottom))
        l.draw(win)
        l2 = Line(Point(100,bottom), Point(100,10))
        l2.draw(win)
    #---------------------------------------------------------------------------------------------------
    def makeScatterGraph(self, xlist,ylist,messageX,messageY,xMultiply,colour):
        xSpread = ((self.xSize-100) / len(xlist)) ##### Check calc - maximum x value into screen width
        print("xspread ", xSpread)
        
        win = self.win
        highestY = self.calcHighest(ylist)
        print("Highest ",highestY)
        
        bottom = self.ySize
        self.highestY = highestY
            
        yConvert = (highestY / (self.ySize))
        self.yConvert = yConvert
        
        self.makeBackground(xlist, ylist, xSpread)
        
        #---------------------------------Plot data
        if len(xlist) > 0 and len(ylist) > 0:
            for x in range(len(xlist)):
                b1 = Rectangle(Point(int(xlist[x]*xSpread)+100,498-(ylist[x]/yConvert)), Point(int(xlist[x]*xSpread)+101,498-(ylist[x]/yConvert)))
                b1.setFill(colour)
                b1.draw(win)


        data14 = Text(Point(int(self.maxX/2), bottom+50), messageX)
        data14.draw(win)
        overY = (len(messageY)*5)+20
        data15 = Text(Point(overY, 15),messageY )
        data15.draw(win)

    #---------------------------------------------------------------------------------------------------
    def makeHistogram(self, xlist,ylist,messageX,messageY,xMultiply,colour):
        xSpread = ((self.xSize-100) / len(xlist)) ##### Check calc - maximum x value into screen width
        print("xspread ", xSpread)
        
        win = self.win
        highestY = self.calcHighest(ylist)
        bottom = self.ySize
        self.highestY = highestY

        xSeperate = int(self.xSize / len(xlist))
            
        yConvert = (highestY / (self.ySize))
        self.yConvert = yConvert
        
        self.makeBackground(xlist, ylist, xSpread)

        colour = "red"
        
        #---------------------------------Plot data
        if len(xlist) > 0 and len(ylist) > 0:
            for x in range(len(xlist)):
                b1 = Line(Point(int(xlist[x]*xSpread)+100,498-(ylist[x]/yConvert)), Point(int(xlist[x]*xSpread)+100,498-(0)))
                b1.setFill(colour)
                b1.draw(win)
                if colour == "red":
                    colour = "blue"
                elif colour == "blue":
                    colour = "green"
                else:
                    colour = "red"


        data14 = Text(Point(int(self.maxX/2), bottom+50), messageX)
        data14.draw(win)
        overY = (len(messageY)*5)+20
        data15 = Text(Point(overY, 15),messageY )
        data15.draw(win)
        
    #-------------------------------------------------------------------------------------------------------
    def makeLineGraph(self, xlist,ylist,messageX,messageY,xMultiply,colour):
        xSpread = ((self.xSize-100) / len(xlist)) ##### Check calc - maximum x value into screen width
        print("xspread ", xSpread)
        
        win = self.win
        bottom = self.ySize
        highestY = self.calcHighest(ylist)
        self.highestY = highestY
            
        yConvert = int(highestY / (self.ySize))
        self.yConvert = yConvert

        self.makeBackground(xlist, ylist, xSpread)
        #---------------------------------Plot data
        ystart = 0
        if len(ylist) > 0:
            ystart = ylist[0]

        if len(ylist) > 0 and len(ylist) > 0:
            start_lineX = int(xlist[0]*xSpread)+100
            start_lineY = 498-(ystart/yConvert)
            
            for x in range(1,len(ylist)):
                b1 = Line(Point(start_lineX,start_lineY), Point(int(xlist[x]*xSpread)+102,498-(ylist[x]/yConvert)))
                b1.setFill(colour)
                b1.draw(win)
                start_lineX = int(xlist[x]*xSpread)+100
                start_lineY = 498 - (ylist[x]/yConvert)


        data14 = Text(Point(int(self.maxX/2), bottom+50), messageX)
        data14.draw(win)
        overY = (len(messageY)*5)+20
        data15 = Text(Point(overY, 15),messageY )
        data15.draw(win)
    #---------------------------------------------------------------------------------------------

    def makeLineGraphOver(self, xlist,ylist,messageX,messageY,xMultiply,colour):
        xSpread = ((self.xSize-100) / len(xlist)) ##### Check calc - maximum x value into screen width
        print("xspread ", xSpread)
        highestY = self.highestY
            
        yConvert = self.yConvert
            
        bottom = self.ySize-100
        win = self.win

        ystart = 0
        if len(ylist) > 0 and len(xlist) > 0:
            ystart = ylist[0]

            start_lineX = int(xlist[0]*xSpread) +100
            start_lineY = 498-(ystart/yConvert)

            for x in range(1,len(ylist)):
                b1 = Line(Point(start_lineX,start_lineY), Point(int(xlist[x]*xSpread)+102,498-(ylist[x]/yConvert)))
                b1.setFill(colour)
                b1.draw(win)
                start_lineX = int(xlist[x]*xSpread)+102
                start_lineY = 498-(ylist[x]/yConvert)
        
    #-------------------------------------------------------------------------------------
    def addComment(self,comment,atX,atY, colour):
        win = self.win
        data1 = Text(Point(atX, atY),comment )
        data1.setFill(colour)
        data1.draw(win)
    def addImage(self,filename,x,y):
        win = self.win
        d1 = Image(Point(x,y), filename)
        d1.draw(win) 
    def markPoint(self,atX,atY, size, colour):
        win = self.win
        cir1 = Circle(Point(atX,atY), size)
        cir1.setFill(colour)
        cir1.setOutline("black")
        cir1.draw(win)
    def markPointAtXY(self,xlist, atX,atY, size, colour):
        xSpread = int((self.xSize-100) / len(xlist)) ##### Check calc - maximum x value into screen width
        print("xspread ", xSpread)
        win = self.win
        cir1 = Circle(Point((atX*xSpread)+100,(self.ySize -100 - atY)), size)
        cir1.setFill(colour)
        cir1.setOutline("black")
        cir1.draw(win)
    def markLabel(self,atX,atY, size, colour, plusX, message):
        win = self.win
        cir1 = Circle(Point(atX,atY), size)
        cir1.setFill(colour)
        cir1.setOutline("black")
        cir1.draw(win)
        data1 = Text(Point(plusX, atY),message )
        data1.draw(win)
    def makeLine(self,x,y,x2,y2,w,colour):
        win = self.win
        l = Line(Point(x,y), Point(x2,y2))
        l.setWidth(w)
        l.setFill(colour)
        l.draw(win)
    def makeRectangleFilled(self,x,y,x2,y2,colour):
        win = self.win
        b1 = Rectangle(Point(x,y), Point(x2, y2))
        b1.setFill(colour)
        b1.draw(win)
    def makeRectangleLines(self,x,y,x2,y2,w,colour):
        win = self.win
        l1 = Line(Point(x,y), Point(x2,y))
        l1.setWidth(w)
        l1.setFill(colour)
        l1.draw(win)
        l2 = Line(Point(x,y2), Point(x2,y2))
        l2.setWidth(w)
        l2.setFill(colour)
        l2.draw(win)
        l3 = Line(Point(x,y), Point(x,y2))
        l3.setWidth(w)
        l3.setFill(colour)
        l3.draw(win)
        l4 = Line(Point(x2,y), Point(x2,y2))
        l4.setWidth(w)
        l4.setFill(colour)
        l4.draw(win)

    

#------------------------------------------------
    ########### >>>>>>>>>>> Other shapes that can be added

    #b1 = Rectangle(Point(230,130), Point(270, 170))
    #b1.setFill("lightblue")
    #b1.draw(win)
    
    ######### >>>>> circles
    #cir2 = Circle(Point(500,150), 30)
    #cir2.setFill("red")
    #cir2.draw(win)

    ######### >>>>> Polygon = multiple points
    #p1 = Polygon(Point(725,125), Point(800,150), Point(750,170))
    #p1.setFill("yellow")
    #p1.draw(win)
   
    #e1 = Oval(Point(230,270), Point(270,330)) # set corners of bounding box
    #e1.setFill("blue")
    #e1.setOutline("red")
    #e1.draw(win)

    #--------------------------------------------
        #--------------------------------------------------
        #data16 = Text(Point(500, bottom+70),"Click to leave" )
        #data16.draw(win)
        #------------------------------------------------------------

        #pointM1 = win.getMouse() #Get mouse click & button coordinates
                
        #xx = int(pointM1.x)
        #yy = int(pointM1.y)
        #win.close()
