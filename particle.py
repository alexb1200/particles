class particle:
    def __init__(self,x,y,col=0,row=0, v=PVector(0,0)):
        self.x=x
        self.y=y
        self.v=v
        self.col=col
        self.row=row
        self.prevC=col
        self.prevR=row
        self.flag=1
        self.a=PVector()
        self.m=random(.1,5)
    
    def push(self,force):
        self.a=force/self.m
        self.v+=self.a
        self.a=0
    def collide(self):
        f=self.m*PVector(self.v.x*self.v.x,self.v.y*self.v.y)*-1/20
        print("bounce")
        self.push(f)
    
    def tick(self,row=0,col=0):
        self.x+=self.v.x
        self.y+=self.v.y
        #print(self.v.x,self.v.y)
        self.prevC=self.col
        self.prevR=self.row
        self.col=col
        self.row=row
        if(self.v.x>3 or self.v.y >3):
            self.v=PVector(4,4)
        if(self.v.x<-3 or self.v.y <-3):
            self.v=PVector(-1,-1)
        
        if(self.x<0):
            self.x=width
            self.v=PVector(random(-5,5),random(-5,5))
        if(self.x>width):
            self.x=0
            self.v=PVector(random(-5,5),random(-5,5))
        if(self.y<0):
             self.y=height
             self.v=PVector(random(-5,5),random(-5,5))
        if(self.y>height):
            self.y=0
            self.v=PVector(random(-5,5),random(-5,5))
        if(self.prevR == self.row and self.prevC==self.col):
            self.flag=1
            return 1
        else:
            self.flag=0
            return 0
