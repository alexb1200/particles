import particle as p
import boxes as b



def setup():
    size(1000,1000,P2D)
    colorMode(HSB,255)

boxSize=50
g=b.grid(boxSize,boxSize).areas

   
z= [p.particle(random(0,1000),random(0,1000),0,0)for i in range(700)]#p.particle(499,250,0,0,PVector(10,10))
acc=0
t=p.particle(1000/2,0)

writting=[]
writting.append(PVector(500,500))
def gravity(ball):
    ball.push(PVector(0,0.8))

    
def draw():
    
    
    global acc
    background(0)
    #stroke(255)
    #stroke(50,100,50)
    #print(get(255,244))
    
    # for m in g:
    #     for v in m:
    #         v.display()
            
    for i,y in enumerate(z):
        row=ceil(y.y/boxSize)-1
        col=ceil(y.x/boxSize)-1
        curr=g[row][col]
        if(y.tick(row,col) and y.flag==0):
            curr.pUp()
        else:
            if y.flag==1: #check to make sure the flag logic is good
                g[y.prevR][y.prevC].pDown()
        
        
        y.push((-1*PVector(curr.xMin+boxSize/2,curr.yMin+boxSize/2)+PVector(y.x,y.y))*.001*(.5+3*curr.cnt))
        #gravity(y)
        #print(curr.cnt)
        
        #curr.display(1000)
        #stroke(y.v.x*y.v.y/1000+curr.cnt,50,y.v.x*y.v.y%100+10)
        #bit=writting[floor(random(0,len(writting)-1))]
        bit=writting[i%len(writting)]
        
        w=(bit-PVector(y.x,y.y))
        w=w/(w.x*w.x+w.y*w.y)+.1*w
        y.push( w)
        fill(y.v.x*y.v.y%255,y.v.x*y.v.y%155+100,255)#y.v.x*y.v.y%100+10)
        
        circle(y.x,y.y,3)
    #g[1][2].display(1000)

        
        
   
    
            #acc+=50
    # gravity(t)
    # if(t.y>height-20):
    #     t.collide()
    # circle(t.x,t.y,10)
    # t.tick()
  
    
    # for x in z:
    #     x.push(PVector(random(-1,1),random(-1,1)))
    #     circle(x.x,x.y,2)
    #     x.tick()


def mouseDragged():
    # row=ceil(mouseY/boxSize)
    # col=ceil(mouseX/boxSize)
    # curr=g[row][col]
    # curr.pUp(100000)
    # curr.display(1000)
    #if(millis()%2==0):
        writting.append(PVector(mouseX,mouseY))

def keyPressed():
    if key== 'c':
        del writting[:]
        writting.append(PVector(500,500))
        
def mouseClicked():
    for y in z:
        w=(PVector(mouseX,mouseY))-PVector(y.x,y.y)
           
        #y.push( w*.1)
        y.v=PVector(0,0)
        
       
        
        
