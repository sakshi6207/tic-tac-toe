def sum(a,b,c):
    return a+b+c

def printBoard(xstate,zstate):
    z='x' if xstate[0] else ('0' if zstate[0] else 0)
    o='x' if xstate[1] else ('0' if zstate[1] else 1)
    t='x' if xstate[2] else ('0' if zstate[2] else 2)
    T='x' if xstate[3] else ('0' if zstate[3] else 3)
    f='x' if xstate[4] else ('0' if zstate[4] else 4)
    F='x' if xstate[5] else ('0' if zstate[5] else 5)
    s='x' if xstate[6] else ('0' if zstate[6] else 6)
    S='x' if xstate[7] else ('0' if zstate[7] else 7)
    e='x' if xstate[8] else ('0' if zstate[8] else 8)
    print(f"{z}|{o}|{t}")
    print(f"-| |-")
    print(f"{T}|{f}|{F}")
    print(f"-| |-")
    print(f"{s}|{S}|{e}")

def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
      if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
        print("X won the match")
        return 1
      if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
        print("0 won the match")
        return 0
    return -1


xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
turn=1  #1 for X and 0 for o
print("Welcome to Tic Tac Toe")
while(True):
    if(turn ==1):
        printBoard(xstate,zstate)
        print("X's chance")
        value= int(input("Please enter a value:"))
        xstate[value]=1
    else: 
        print("0's chance")
        value=int(input("Please enter a value:")) 
        zstate[value]=1 
    cwin=checkwin(xstate, zstate)  
    if(cwin!=-1):  
        print("Match over")
        break
    turn=1-turn

    
    
