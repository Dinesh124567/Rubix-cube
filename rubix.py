F,U, D,L,R,B =[['G' for i in range(3)] for j in range(3)] ,[['W' for i in range(3)] for j in range(3)] ,[['Y' for i in range(3)] for j in range(3)] ,[['O' for i in range(3)] for j in range(3)] ,[['R' for i in range(3)] for j in range(3)] ,[['B' for i in range(3)] for j in range(3)] 


def f():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=F[2-j][i]
    for i in range(3):
        for j in range(3):
            F[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=U[2][i] 
    for i in range(3):
        U[2][i]=L[2-i][2] 
    for i in range(3):
        L[i][2]=D[0][i] 
    for i in range(3):
        D[0][i]=R[2-i][0] 
    for i in range(3):
        R[i][0]=t[i] 

#upper sided
def u():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=U[2-j][i]
    for i in range(3):
        for j in range(3):
            U[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=F[0][i] 
    for i in range(3):
        F[0][i]=R[0][i] 
    for i in range(3):
        R[0][i]=B[0][i] 
    for i in range(3):
        B[0][i]=L[0][i] 
    for i in range(3):
        L[0][i]=t[i] 



#down clock wise
def d():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=D[2-j][i]
    for i in range(3):
        for j in range(3):
            D[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=F[2][i] 
    for i in range(3):
        F[2][i]=L[2][i] 
    for i in range(3):
        L[2][i]=B[2][i] 
    for i in range(3):
        B[2][i]=R[2][i] 
    for i in range(3):
        R[2][i]=t[i] 


#RIGHT SIDE
def r():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=R[2-j][i]
    for i in range(3):
        for j in range(3):
            R[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=F[i][2] 
    for i in range(3):
        F[i][2]=D[i][2] 
    for i in range(3):
        D[i][2]=B[2-i][0] 
    for i in range(3):
        B[i][0]=U[2-i][2] 
    for i in range(3):
        U[i][2]=t[i] 


#LEFT SIDED
def l():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=L[2-j][i]
    for i in range(3):
        for j in range(3):
            L[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=F[i][0] 
    for i in range(3):
        F[i][0]=U[i][0] 
    for i in range(3):
        U[i][0]=B[2-i][2] 
    for i in range(3):
        B[i][2]=D[2-i][0] 
    for i in range(3):
        D[i][0]=t[i] 


# back sided
def b():
    # clock wise of F
    T=[['i' for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            T[i][j]=B[2-j][i]
    for i in range(3):
        for j in range(3):
            B[i][j]=T[i][j]

    #CHANGE THE others                
    t=['n' for i in range(3)]
    for i in range(3):
        t[i]=R[i][2] 
    for i in range(3):
        R[i][2]=D[2][2-i] 
    for i in range(3):
        D[2][i]=L[i][0] 
    for i in range(3):
        L[i][0]=U[0][2-i] 
    for i in range(3):
        U[0][i]=t[i] 

def ant_f():
    for i in range(3):
        f() 
def ant_d():
    for i in range(3):
        d() 
def ant_u():
    for i in range(3):
        u() 
def ant_l():
    for i in range(3):
        l() 
def ant_r():
    for i in range(3):
        r() 
def ant_b():
    for i in range(3):
        b()
  
def cross_solve():
    for i in range(4):
        if F[0][1]==F[1][1] and U[2][1]==U[1][1]:
            rotat_R()
            print("rotat r")
            continue
        if cross_onFace():
            Face_solve()
        if cross_onB():
            bottm_solve()
        if cross_itCont(L):
            t=0
            while not cross_onFace():
                l()
                print("l")
                t=t+1
            Face_solve()
            for i in range(t):
                ant_l(), print("ant_l")
                
        if cross_itCont(R):
            t=0
            while not cross_onFace():
                r()
                print("r")
                t=t+1
            Face_solve()
            
            for i in range(t):
                ant_r(), print("ant_r")

        if cross_itCont(B):
            t=0
            while not cross_onB():
                b()
                print("b")
                t=t+1
            bottm_solve()

            for i in range(t):
                ant_b(), print("ant_b")
                

        if cross_itCont(U):
            t=0
            while not cross_onFace():
                u()
                print("u")
                t=t+1
            Face_solve()
            if t>0:
                f(), print("f")
                for i in range(t):
                    ant_u(), print("ant_u")
                ant_f() , print("ant_f")   
        rotat_R()
        print("rotat r")
        

def Face_solve():

    if F[1][0]==U[1][1] and L[1][2]==F[1][1] :
        l(), print("l")
        d(), print("d")
        ant_l(), print("ant_l")
        f(), print("f")
        f(), print("f")
    
    elif F[1][2]==U[1][1] and R[1][0]==F[1][1] :
        ant_r(), print("ant r")
        ant_d(), print("and d")
        r(), print("r")
        f(), print("f")
        f(), print("f")
    
    elif F[2][1]==U[1][1] and D[0][1]==F[1][1]:
        ant_f(), print("ant f")
        ant_r(), print("ant r")
        ant_d(), print("ant d")
        r(), print("r")
        f(), print("f")
        f(), print("f")

    elif F[0][1]==U[1][1] and U[2][1]==F[1][1]:
        f(), print("f")
        ant_u(), print("ant u")
        r(), print("r")
        u(), print("u")
    
    else :
        while not (F[0][1]==F[1][1] and U[2][1]==U[1][1]):
            f(), print("f")


def bottm_solve():
    c=0
    while not cross_onFace() :
        d(), print("d")
        c+=1
        if c>4 :
            print("wrong")
            break
    Face_solve()

def cross_onFace():
    if F[0][1]==U[1][1] and U[2][1]==F[1][1]:
        return bool(True)
    if F[1][0]==U[1][1] and L[1][2]==F[1][1]:
        return bool(True)
    if F[1][2]==U[1][1] and R[1][0]==F[1][1]:
        return bool(True)
    if F[2][1]==U[1][1] and D[0][1]==F[1][1]:
        return bool(True)
    if U[2][1]==U[1][1] and F[0][1]==F[1][1]:
        return bool(True)
    if L[1][2]==U[1][1] and F[1][0]==F[1][1]:
        return bool(True)
    if R[1][0]==U[1][1] and F[1][2]==F[1][1]:
        return bool(True)
    if D[0][1]==U[1][1] and F[2][1]==F[1][1]:
        return bool(True)
    return bool(False)


def cross_onB():
    if D[0][1]==U[1][1] and F[2][1]==F[1][1]:
        return True
    if D[1][0]==U[1][1] and L[2][1]==F[1][1]:
        return True
    if D[2][1]==U[1][1] and B[2][1]==F[1][1]:
        return True
    if D[1][2]==U[1][1] and R[2][1]==F[1][1]:
        return True
    if L[2][1]==U[1][1] and D[1][0]==F[1][1]:
        return True
    if B[2][1]==U[1][1] and D[2][1]==F[1][1]:
        return True
    if R[2][1]==U[1][1] and D[1][2]==F[1][1]:
        return True
    if F[2][1]==U[1][1] and D[0][1]==F[1][1]:
        return True
    return False

def cross_itCont(lst):
    if lst==L:
        if L[0][1]==U[1][1] and U[1][0]==F[1][1]:
            return True
        if L[1][0]==U[1][1] and B[1][2]==F[1][1]:
            return True
        if L[1][2]==U[1][1] and F[1][0]==F[1][1]:
            return True
        if L[2][1]==U[1][1] and D[1][0]==F[1][1]:
            return True
    
    if lst==R:
        if R[0][1]==U[1][1] and U[1][2]==F[1][1]:
            return True
        if R[1][0]==U[1][1] and F[1][2]==F[1][1]:
            return True
        if R[1][2]==U[1][1] and B[1][0]==F[1][1]:
            return True
        if R[2][1]==U[1][1] and D[0][1]==F[1][1]:
            return True
        
    if lst==B:
        if B[0][1]==U[1][1] and U[0][1]==F[1][1]:
            return True
        if B[1][0]==U[1][1] and R[1][2]==F[1][1]:
            return True
        if B[1][2]==U[1][1] and L[1][0]==F[1][1]:
            return True
        if B[2][1]==U[1][1] and D[2][1]==F[1][1]:
            return True

    if lst==U:
        if U[0][1]==U[1][1] and B[0][1]==F[1][1]:
            return True
        if U[1][0]==U[1][1] and L[0][1]==F[1][1]:
            return True
        if U[2][1]==U[1][1] and F[0][1]==F[1][1]:
            return True
        if U[1][2]==U[1][1] and R[0][1]==F[1][1]:
            return True
    return False

def rotat_R():
    u()
    ant_d()
    t=[F[1][0], F[1][1], F[1][2]]
    for i in range(3):
        F[1][i]=R[1][i]
        R[1][i]=B[1][i]
        B[1][i]=L[1][i]
        L[1][i]=t[i]




def edge_solve():
    for i in range(4):
        if U[2][2]==U[1][1] and F[0][2]==F[1][1] and R[0][0]==R[1][1]:
            rotat_R(), print("rotat r")
            continue
        a=edge_onUppr()
        if bool(edge_onUppr())==True:
            if a==(0,0):
                b(), d(), ant_b(), ant_d(), print("b, d, ant_b, ant_d")
            if a==(0,2):
                r(), d(), ant_r(), ant_d(), print("r, d, ant_r, ant_d")
            if a==(2,0):
                l(), d(), ant_l(), ant_d(), print("l, d, ant_l, ant_d")
            if a==(2,2):
                f(), d(), ant_f(), ant_d(), print("f, d, ant_f, ant_d ")
        
        print(edge_onBtm())
        if bool(edge_onBtm())==True:
                while not edge_onBtm()==(0,2):
                    d(), print("d")
                edge()
        
        rotat_R(), print("rotat r")    

def edge_onBtm():
    #at 0,0
    if (D[0][0]==U[1][1] and (  (L[2][2]==F[1][1] and F[2][0]==R[1][1]) or (L[2][2]==R[1][1] and F[2][0]==F[1][1])  )):
        return 0,0
    if (L[2][2]==U[1][1] and (  (D[0][0]==F[1][1] and F[2][0]==R[1][1]) or (D[0][0]==R[1][1] and F[2][0]==F[1][1])  )):
        return 0,0
    if (F[2][0]==U[1][1] and (  (D[0][0]==F[1][1] and L[2][2]==R[1][1]) or (D[0][0]==R[1][1] and L[2][2]==F[1][1]) )):
        return 0,0
    
    #at 0,2
    if (D[0][2]==U[1][1] and (  (R[2][0]==F[1][1] and F[2][2]==R[1][1]) or (R[2][0]==R[1][1] and F[2][2]==F[1][1])  )):
        return 0,2
    if (R[2][0]==U[1][1] and (  (D[0][2]==F[1][1] and F[2][2]==R[1][1]) or (D[0][2]==R[1][1] and F[2][2]==F[1][1])  )):
        return 0,2
    if (F[2][2]==U[1][1] and (  (D[0][2]==F[1][1] and R[2][0]==R[1][1]) or (D[0][2]==R[1][1] and R[2][0]==F[1][1]) )):
        return 0,2
    
    #at 2,0
    if (D[2][0]==U[1][1] and (  (L[2][0]==F[1][1] and B[2][2]==R[1][1]) or (L[2][0]==R[1][1] and B[2][2]==F[1][1])  )):
        return 2,0
    if (L[2][0]==U[1][1] and (  (D[2][0]==F[1][1] and B[2][2]==R[1][1]) or (D[2][0]==R[1][1] and B[2][2]==F[1][1])  )):
        return 2,0
    if (B[2][2]==U[1][1] and (  (D[2][0]==F[1][1] and L[2][0]==R[1][1]) or (D[2][0]==R[1][1] and L[2][0]==F[1][1]) )):
        return 2,0
    
    #at 2,2
    if (D[2][2]==U[1][1] and (  (R[2][2]==F[1][1] and B[2][0]==R[1][1]) or (R[2][2]==R[1][1] and B[2][0]==F[1][1])  )):
        return 2,2
    if (R[2][2]==U[1][1] and (  (D[2][2]==F[1][1] and B[2][0]==R[1][1]) or (D[2][2]==R[1][1] and B[2][0]==F[1][1])  )):
        return 2,2
    if (B[2][0]==U[1][1] and (  (D[2][2]==F[1][1] and R[2][2]==R[1][1]) or (D[2][2]==R[1][1] and R[2][2]==F[1][1]) )):
        return 2,2

    return False

def edge_onUppr():
    #at 0,0
    if (U[0][0]==U[1][1] and (  (L[0][0]==F[1][1] and B[0][2]==R[1][1]) or (L[0][0]==R[1][1] and B[0][2]==F[1][1])  )):
        return 0,0
    if (L[0][0]==U[1][1] and (  (U[0][0]==F[1][1] and B[0][2]==R[1][1]) or (U[0][0]==R[1][1] and B[0][2]==F[1][1])  )):
        return 0,0
    if (B[0][2]==U[1][1] and (  (U[0][0]==F[1][1] and L[0][0]==R[1][1]) or (U[0][0]==R[1][1] and L[0][0]==F[1][1]) )):
        return 0,0
    
    #at 0,2
    if (U[0][2]==U[1][1] and (  (R[0][2]==F[1][1] and B[0][0]==R[1][1]) or (R[0][2]==R[1][1] and B[0][0]==F[1][1])  )):
        return 0,2
    if (R[0][2]==U[1][1] and (  (U[0][2]==F[1][1] and B[0][0]==R[1][1]) or (U[0][2]==R[1][1] and B[0][0]==F[1][1])  )):
        return 0,2
    if (B[0][0]==U[1][1] and (  (U[0][2]==F[1][1] and R[0][2]==R[1][1]) or (U[0][2]==R[1][1] and R[0][2]==F[1][1]) )):
        return 0,2
    
    #at 2,0
    if (U[2][0]==U[1][1] and (  (L[0][2]==F[1][1] and F[0][0]==R[1][1]) or (L[0][2]==R[1][1] and F[0][0]==F[1][1])  )):
        return 2,0
    if (L[0][2]==U[1][1] and (  (U[2][0]==F[1][1] and F[0][0]==R[1][1]) or (U[2][0]==R[1][1] and F[0][0]==F[1][1])  )):
        return 2,0
    if (F[0][0]==U[1][1] and (  (U[2][0]==F[1][1] and L[0][2]==R[1][1]) or (U[2][0]==R[1][1] and L[0][2]==F[1][1]) )):
        return 2,0
    
    #at 2,2
    if (U[2][2]==U[1][1] and (  (R[0][0]==F[1][1] and F[0][2]==R[1][1]) or (R[0][0]==R[1][1] and F[0][2]==F[1][1])  )):
        return 2,2
    if (R[0][0]==U[1][1] and (  (U[2][2]==F[1][1] and F[0][2]==R[1][1]) or (U[2][2]==R[1][1] and F[0][2]==F[1][1])  )):
        return 2,2
    if (F[0][2]==U[1][1] and (  (U[2][2]==F[1][1] and R[0][0]==R[1][1]) or (U[2][2]==R[1][1] and R[0][0]==F[1][1]) )):
        return 2,2

    return False

def edge():
    while not (U[2][2]==U[1][1] and F[0][2]==F[1][1] and R[0][0]==R[1][1]):
        ant_r(), print("ant r")
        ant_d(), print("ant d")
        r(), print("r")
        d(), print("d")


FF=["G B O", "O G R", "B R W"]
RR=["W O Y" ,"G R R" ,"G O W"]
BB=["O B O", "W B W", "R R B"]
LL=["Y Y R" ,"G O B", "Y Y W"]
UU=["G W B", "O W G" ,"Y Y B"]
DD=["R Y O", "G Y W", "R B G"]

t=0
for i in range(3):
    F[i]=FF[i].split()
    R[i]=RR[i].split()
    B[i]=BB[i].split()
    L[i]=LL[i].split()
    U[i]=UU[i].split()
    D[i]=DD[i].split()



def sec_layer():
    flip(), print("do flip, upside down")
    for i in range(4):
        leftdo()
        rightdo()
        rotat_R(), print("rotate r")

def leftdo():
    if F[1][0]==F[1][1] and L[1][2]==L[1][1]:
        return
    if isinMiddle_lyr("L"):
        MiddleSol(isinMiddle_lyr("L"))
      
    if isinUpper_lyr("L"):
        while(isinUpper_lyr("L")!=1):
            u(), print("u")
        leftA()
        if F[1][0]==L[1][1] and L[1][2]==F[1][1]:
            leftA(), u(), u(),  print("u"), print("u"), leftA()

def rightdo():
    if F[1][2]==F[1][1] and R[1][0]==R[1][1]:
        return
    if isinMiddle_lyr("R"):
        MiddleSol(isinMiddle_lyr("R"))
       
    if isinUpper_lyr("R"):
        while(isinUpper_lyr("R")!=1):
            u(), print("u")
        rightA()
        if F[1][0]==L[1][1] and L[1][2]==F[1][1]:
            rightA(), u(), u(), rightA()

def isinMiddle_lyr(a):
    if a=="L":
        if F[1][0]==L[1][1] and L[1][2]==F[1][1]:
            return 1
        if (F[1][2]==F[1][1] and R[1][0]==L[1][1]) or (F[1][2]==L[1][1] and R[1][0]==F[1][1]):
            return 2
        if (R[1][2]==F[1][1] and B[1][0]==L[1][1]) or (R[1][2]==L[1][1] and B[1][0]==F[1][1]):
            return 3
        if (B[1][2]==F[1][1] and L[1][0]==L[1][1]) or (B[1][2]==L[1][1] and L[1][0]==F[1][1]):
            return 4

    if a=="R":
        if F[1][2]==R[1][1] and R[1][0]==F[1][1]:
            return 2
        if (F[1][0]==F[1][1] and L[1][2]==R[1][1]) or (F[1][0]==R[1][1] and L[1][2]==F[1][1]):
            return 1
        if (R[1][2]==F[1][1] and B[1][0]==R[1][1]) or (R[1][2]==R[1][1] and B[1][0]==F[1][1]):
            return 3
        if (B[1][2]==F[1][1] and L[1][0]==R[1][1]) or (B[1][2]==R[1][1] and L[1][0]==F[1][1]):
            return 4 
    return False

def isinUpper_lyr(a):
    if a=="L":
        if  (U[2][1]==F[1][1] and F[0][1]==L[1][1]) or (U[2][1]==L[1][1] and F[0][1]==F[1][1]):
            return int(1)
        if (U[1][2]==F[1][1] and R[0][1]==L[1][1]) or (U[1][2]==L[1][1] and R[0][1]==F[1][1]):
            return int(2)
        if (U[0][1]==F[1][1] and B[0][1]==L[1][1]) or (U[0][1]==L[1][1] and B[0][1]==F[1][1]):
            return 3
        if (U[1][0]==F[1][1] and L[0][1]==L[1][1]) or (U[1][0]==L[1][1] and L[0][1]==F[1][1]):
            return 4

    if a=="R":
        if  (U[2][1]==R[1][1] and F[0][1]==F[1][1]) or (F[0][1]==R[1][1] and U[2][1]==F[1][1]):
            return 1
        if (U[1][2]==F[1][1] and R[0][1]==R[1][1]) or (U[1][2]==R[1][1] and R[0][1]==F[1][1]):
            return 2
        if (U[0][1]==F[1][1] and B[0][1]==R[1][1]) or (U[0][1]==R[1][1] and B[0][1]==F[1][1]):
            return 3
        if (U[1][0]==F[1][1] and L[0][1]==R[1][1]) or (U[1][0]==R[1][1] and L[0][1]==F[1][1]):
            return 4
    return False

def MiddleSol(a):
    for i in range(a-1):
        rotat_R(), print("rotate_r")
    leftA()
    if a==1:
        return
    for i in range(5-a):
        rotat_R(), print("rotate_r")

def flip():
    for i in range(2):
        ant_l()
        r()
    for i in range(2):
        tm=[F[0][1], F[1][1], F[2][1]]
        for j in range(3):
            F[j][1]=U[j][1]
        for j in range(3):
            U[j][1]=B[2-j][1]
        for j in range(3):
            B[j][1]=D[2-j][1]
        for j in range(3):
            D[j][1]=tm[j]

def leftA():
    ant_u(), ant_l(), u(), l(), u(), f(), ant_u(), ant_f()
    print("ant_u, ant_l, u, l, u, f, ant_u, ant_f")
def rightA():
    u(), r(), ant_u(), ant_r(), ant_u(), ant_f(), u(), f()
    print("u, r, ant_u, ant_r, ant_u, ant_f, u, f")


def third_layer():
    th_cross()
    th_edge()

def th_cross():
    #phase 1 ..........................................
    while not (U[0][1]==U[1][1] and U[1][0]==U[1][1] and U[1][2]==U[1][1] and U[2][1]==U[1][1]):
        
        if F[0][1]==U[1][1]:
            if (U[1][0]==U[1][1] and U[1][2]==U[1][1]) or (U[0][1]==U[1][1] and U[1][0]==U[1][1]) or (U[0][1]!=U[1][1] and U[1][0]!=U[1][1] and U[1][2]!=U[1][1] and U[2][1]!=U[1][1]):
                FRU()
            else:
                rotat_R(), print("rotate_r 1")
        else:
            rotat_R(), print("rotate r")
        
    #phase 2 ....................................
    a=0
    while not F[0][1]==F[1][1]:
        u()
        print("u")
        a=a+1
        if a>4:
            break
    for i in range(4):
        rotat_R(), print("rotate r")
        if F[0][1]!=F[1][1]:
            if L[0][1]==F[1][1]:
                p2A()
            if B[0][1]==F[1][1]:
                p2A(), rotat_R(), rotat_R(), rotat_R(), print("rotate l")
                p2A(), rotat_R(), print("rotate r"), p2A()

def th_edge():
    #phase 1......................
    while edge_st()==0:
        ep1A()
    c=0
    while edge_st()!=4:
        while not ed_right():
            rotat_R(), print("rotate r")
            c=c+1
        ep1A()
    for i in range(c):
        rotat_R(), print("rotate r")

    #phase 2..................
    for i in range(4):
        while not U[2][2]==U[1][1]:
            RD()
        u(), print("u")
    

def FRU():
    f(), r(), u(), ant_r(), ant_u(), ant_f()
    print("f, r, u, ant_r, ant_u, ant_f")
def p2A():
    r(), u(), ant_r(), u(), r(), u(), u(), ant_r(), u()
    print("r(), u(), ant_r(), u(), r(), u(), u(), ant_r(), u()")
def RD():
    ant_r(), ant_d(), r(), d()
    print("ant_r(), ant_d(), r(), d()")
def ep1A():
    u(), r(), ant_u(), ant_l(), u(), ant_r(), ant_u(), l()
    print("u(), r(), ant_u(), ant_l(), u(), ant_r(), ant_u(), l()")

def edge_st():
    a=0
    for i in range(4):
        if ed_right():
            a=a+1
        rotat_R()
    return a

def ed_right():
    if F[0][2]==F[1][1] and ((R[0][0]==R[1][1] and U[2][2]==U[1][1]) or (R[0][0]==U[1][1] and U[2][2]==R[1][1])): 
        return True
    if F[0][2]==R[1][1] and ((R[0][0]==F[1][1] and U[2][2]==U[1][1]) or (R[0][0]==U[1][1] and U[2][2]==F[1][1])):
        return True
    if F[0][2]==U[1][1] and ((R[0][0]==R[1][1] and U[2][2]==F[1][1]) or (R[0][0]==F[1][1] and U[2][2]==R[1][1])):
        return True
    return False
"""...................................................................................."""
#b(), ant_r(), l(), u(), u(), l(), b(), ant_b()

print(U)
print(F)
print(D)
print(B)


print("solving,,,,,,,,,,,,,,,,,,,")

cross_solve()
print("layer one cross solved")
 
edge_solve()

print("layer one solved")
print(U)

sec_layer()
print("layer 2 solved")

third_layer()
print("layer 3 solved")

flip()


print("u"), print(U)
print("B"), print(B)
print("D"), print(D)
print("L"), print(L) 
print("F"), print(F)
print("r"), print(R)

