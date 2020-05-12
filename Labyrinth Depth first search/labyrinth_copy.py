def sanity(x,y,lab):
    x-=1
    if len(lab)==0:
        print('Empty labyrinth. You made it out of there!')
        return False
    else:
        try:
            pos = lab[y][x]
            if pos==0:
                return True
            else:
                print('You are standing on the wall. Nice view!\n')
                print('Please try other coordinates.\n')
                return False
        except Exception as e:
            print("Your coordinates are ({},{}).\n".format(x,y))
            print('While labyrinth size is ({},{}).\n'.format(len(lab[0]),len(lab)))
            print('You are outside of the labyrinth. You made it out of there!\n')
            return False


def read_lab(file = 'testlab.txt'):
    lab=[]
    with open(file,'r') as labfile:
        lab = labfile.readlines()
    lab = [[int(y) for y in list(x.strip())] for x in lab]    
    return lab    


def print_lab(lab):
    s = len(str(len(lab)))+1
    print(' '*s,'Y, V')
    print(' '*s,'^')
    print(' '*s,'|')

    for line,k in zip(lab,range(1,len(lab)+1)):
        lineS = [str(x) for x in line]
        s = len(str(len(lab)))-len(str(k))
        for j in range(len(line)):
            if len(str(lineS[j]))>=2:
                #print('here',lineS[j])
                pass
            else:
                lineS[j]= str(lineS[j])+' '
        lineS = str(lineS).replace(',','').replace("'",' ').replace('[','').replace(']','')#.replace(' 1 ',chr(9608)+chr(9608)+chr(9608))#12/8       
        print(' '*s,k,'|',lineS)
        
    ST = str(k)+' '*s+'|'+str(line)
    s = list(ST).index('[')
    print(' '*s,'-----'*(len(line)+2),'> X, U')
    print('\n\n')

    

def LAB(x,y,lab,marker = -1):
    '''

    x,y -- initial position
    lab -- labyrinth array
    marker -- visited cell marker 0/-1, where 0 - empty cell, -1 visited cell
    
    '''
    y-=1
    

    #4production rules
    RX = [-1,0,1,0]
    RY = [0,1,0,-1]
    #RX = [-1,0,1,0]
    #RY = [0,1,0,-1]

    trace = [[x,y,-2]]

    PATH = [-1]
    FLAGBACK = []
    #for backtrak1 marker == 0
    MEMORYLIST = []
    def TRY(Xs,Ys,FIND = True,BACK = False):
        #print(PATH,'!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        if PATH[0]>0:
            return True
        #print('here')
        else:
            while FIND and PATH[0]<0:
                #print('f_loop')
                #for 4 production rules
                for k in range(4):
                    #print('k_loop')
                    #if on the border
                    if (Xs==0) or (Ys==0) or (Xs==W-1) or (Ys==H-1):
                        #TRY(Xs,Ys,False)
                        #path is found
                        if PATH[0]<0:
                            print('\n\n---Path is found.---\n\n')
                            FIND = False
                            PATH[0] = 1
                            TRY(Xs,Ys,False,False)
                        
                    else:
                        #step
                        #print(1,'X =' ,Xs,'Y = ',Ys)
                        Xs,Ys = Xs+RX[k],Ys+RY[k]
                        #print(1,'X =' ,Xs,'Y = ',Ys, 'R = ',k)
                        #print(k!= trace[-1][2])
                        #print((int(lab[Ys][Xs]) == 0))
                        #print(lab[Ys][Xs])
                    #if marker ==0:
                        #if (Ys,Xs) in MEMORYLIST:
                            #
                            #continue
                        
                        if (int(lab[Ys][Xs]) == 0):
                            #print('lab[Ys][Xs]',lab[Ys][Xs],Ys,Xs)
                            if BACK:
                                if  (k!= int(trace[-1][2])):
                                    if PATH[0]<0:
                                        #print('a2')
                                        trace.append([Xs,Ys,k])
                                        CNT[0]+=1
                                        if k == 1:
                                            Yss = 7-Ys
                                        elif k==3:
                                            Yss = 7-Ys
                                        else:
                                            Yss = 7-Ys
                                        print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.','L:=L+1='+str(len(trace)+1)+'.','LAB[{},{}]:={}.'.format(Xs+1,Yss,len(trace)),'Free.')
                                        lab[Ys][Xs] = len(trace)#-1
                                        #print(trace)
                                        #print_lab(lab)
                                        TRY(Xs,Ys,True,False)
                                        BACK = False
                                    #continue
                            else:
                                    if PATH[0]<0:
                                        #print('a1')
                                        trace.append([Xs,Ys,k])
                                        CNT[0]+=1
                                        if k == 1:
                                            Yss = 7-Ys
                                        elif k==3:
                                            Yss = 7-Ys
                                        else:
                                            Yss = 7-Ys
                                        print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.','L:=L+1='+str(len(trace)+1)+'.','LAB[{},{}]:={}.'.format(Xs+1,Yss,len(trace)),'Free.')
                                        lab[Ys][Xs] = len(trace)#-1
                                        #print(trace)
                                        #print_lab(lab)
                                        TRY(Xs,Ys,True,False)
                                        #continue


                        elif (int(lab[Ys][Xs])==1):
                            #print(BACK)
                            if (PATH[0]<0 and (not BACK)):
                                CNT[0]+=1
                                print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.','Wall.')
                                Xs,Ys = Xs-RX[k],Ys-RY[k]
                            #continue
                            else:
                                Xs,Ys = Xs-RX[k],Ys-RY[k]
                                FLAGBACK.append('Wall')
                                
                            
                        else:
                            if (int(lab[Ys][Xs])==-1):
                                if (PATH[0]<0 and (not BACK)):
                                    CNT[0]+=1
                                    print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.','Thread')#.ALredy.Visited')
                                    Xs,Ys = Xs-RX[k],Ys-RY[k]
                                #continue
                                else:
                                    Xs,Ys = Xs-RX[k],Ys-RY[k]
                                    FLAGBACK.append('Thread')
                            else:
                                 #print('HOW',int(lab[Ys][Xs]))
                                 #if visited
                                if (PATH[0]<0 and  (not BACK)):
                                    CNT[0]+=1
                                    print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.','Thread')
                                    Xs,Ys = Xs-RX[k],Ys-RY[k]
                                else:
                                    Xs,Ys = Xs-RX[k],Ys-RY[k]
                                    #FLAGBACK.append('Thread')

                if PATH[0]<0:
                    #if all production rules were tried            
                    try:
                        if PATH[0]<0:
                            #print(trace)
                            
                            if k == 1:
                                Yss = 7-Ys
                            elif k==3:
                                Yss = 7-Ys
                            else:
                                Yss = 7-Ys
                            
                            print('-'*len(trace),'Backtrack ','L:=L+1='+str(len(trace)+1)+'.','LAB[{},{}]:={}.'.format(Xs+1,Yss,-1))
                            XY = trace.pop()
                            lab[XY[1]][XY[0]] = int(marker)
                            if marker == 0:
                                MEMORYLIST.append((XY[0],XY[1]))
                                print(MEMORYLIST)
                                
                            try:
                                del FLAGBACK[0]
                            except:
                                pass
                            for name in FLAGBACK:
                                CNT[0]+=1
                                print(str(CNT[0])+').','-'*len(trace),'R'+str(k+1)+'.',FLAGBACK.pop())
                            

                            TRY(trace[-1][0],trace[-1][1],True,True)
                    except Exception as e:
                        if PATH[0]<0:
                            print('No path.')
                            FIND = False
                            return False
        #FIND=False
        #return True
            
    
                  
    if (sanity(x,y,lab)):
        print('sanity check passed')
        
        #widh and hight of the labirinth
        W,H = len(lab[0]),len(lab)
        #trials counter / steps counter
        CNT = [0]
        
        print_lab(lab)

        TRY(x,y,True)
        
    else:
        pass    

    print_lab(lab)
   



                

                  
    





#LAB(x=8,y=9,lab=read_lab('testlab.txt'))   
LAB(x=5,y=4,lab=read_lab('lab1.txt'),marker=-1)
#LAB(x=5,y=4,lab=read_lab('lab1.txt'),marker=0)
#LAB(x=14,y=15,lab=read_lab('20x15.txt')) 
#LAB(x=5,y=5,lab=read_lab('another.txt'))
#LAB(x=3,y=32,lab=read_lab('another1.txt'),marker=-1)






