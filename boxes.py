class grid:
    def __init__(self, xbox,ybox):
        self.x=1000/xbox
        self.y=1000/ybox
        self.areas=[[box((i-1)*xbox,(j-1)*ybox,i*xbox,j*ybox,i+j*self.x) for i in range(1,self.x+1)] for j in range(1,self.y+1)]
        print(len(self.areas))
        
class box:
    def __init__(self,xMin,yMin,xMax,yMax, id):
        self.cnt=0
        self.xMax=xMax
        self.yMax=yMax
        self.xMin=xMin
        self.yMin=yMin
        self.id=id
    def display(self,c=50):
        
        noFill()
        if(c==1000):
            
            stroke(c,c,80)
            rect(self.xMin,self.yMin,self.xMax-self.xMin,self.yMax-self.yMin)
                        
        else:
            stroke(50,50,80)
            rect(self.xMin,self.yMin,self.xMax-self.xMin,self.yMax-self.yMin)
        noStroke()
        if(1):
           textSize(10)
           fill(self.xMin%100-20,self.yMin%100-10,100)
           text(str(self.id),self.xMin,self.yMin)
    def pUp(self, amt=1):
        
        # if self.cnt >750 or self.cnt <-20:
        #     cnt=0
        # else:
        self.cnt+=amt
    def pDown(self):
       
        if self.cnt >75 or self.cnt <-20:
            cnt=0
        else:
             self.cnt-=1
        
