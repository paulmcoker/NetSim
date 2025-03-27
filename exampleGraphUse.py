from makeGraph import *


def main():
    xlist = []
    ylist = []
    maxMakeNumber = 9000
    doCycles = 600
    goDown = 2
    for x in range(doCycles):
        rx = x
        xlist.append(rx)
        ry = random.randint(1000, (maxMakeNumber - (x * goDown)))
        ylist.append(ry)

    totalYY = 0
    for i in range(len(ylist)):
        totalYY += ylist[i]
    averageYY = int(totalYY / doCycles)
    print("Ave = ", averageYY)

    xlist2 = []
    ylist2 = []
    for x in range(doCycles):
        rx = x
        xlist2.append(rx)
        ry = random.randint(1, 1000)
        ylist2.append(ry)

    messagex = "X = Cycles"
    messagey = "Y = Packets"

    maxX = 1200
    maxY = 600

    graphing = makeGraph(maxX, maxY)
    xMultiply = 1

    # graphing.makeHistogram(xlist, ylist,messagex,messagey,xMultiply,"black")
    graphing.makeScatterGraph(xlist, ylist, messagex, messagey, xMultiply, "black")
    # graphing.makeLineGraph(xlist, ylist,messagex,messagey,xMultiply,"black")
    graphing.makeLineGraphOver(xlist2, ylist2, messagex, messagey, xMultiply, "red")

    graphing.makeRectangleFilled(410, 5, 590, 35, "lightblue")
    graphing.addComment("Packets delivered", 500, 20, "blue")

    graphing.markPoint(300, 300, 8, "red")  # mark with circle x,y,size,colour
    graphing.markLabel(1100, 50, 8, "red", 1150, "marked")  # mark with circle x,y,size,colour + place-label message
    graphing.makeRectangleLines(1080, 30, 1190, 150, 3, "red")
    graphing.makeLine(100, 300, 1100, 300, 2, "blue")
    graphing.addComment("Ave Pkts", 1150, 300, "black")
    graphing.markPointAtXY(xlist, 100, 100, 8, "blue")


if __name__ == "__main__":
    main()

