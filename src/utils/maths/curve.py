speedStep = 100

class bezeirCurve:

    def __init__(self, pt1, pt2, pt3, pt4, step=speedStep):
        self.x1,self.y1 = pt1[0], pt1[1]
        self.x2,self.y2 = pt2[0], pt2[1]
        self.x3,self.y3 = pt3[0], pt3[1]
        self.x4,self.y4 = pt4[0], pt4[1]
        self.step = step

    def getPoint(self):
        output=[]
        for i in range(self.step,1,-1):
            x = self.point4curve(i/self.step,self.x1,self.x2,self.x3,self.x4)
            y = self.point4curve(i/self.step,self.y1,self.y2,self.y3,self.y4)
            val = tuple((x,y))
            output.append(val)
        return output

    def point4curve(self, step, val1, val2, val3, val4):
        p1 = (1-step)**3 * val1
        p2 = 3 * (1-step)**2 * step * val2
        p3 = 3 * (1-step)* step**2 * val3
        p4 = step**3 * val4
        position = p1+p2+p3+p4
        return position