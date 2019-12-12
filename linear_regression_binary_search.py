import xml.etree.cElementTree as et
import matplotlib.pyplot as plt
import numpy as np


def creation(x):
    empty=[]
    tree=et.ElementTree(file=x)
    root = tree.getroot()
    for rows in root:
        for year in rows:
            if (year.tag=='YEAR'):
                x=int(year.text)
            elif(year.tag=='ANNUAL'):
                y=float(year.text)
        temp=[x-1900,y]
        empty.append(temp)
    return empty



def dis(a,b,m,c):
        return (m*a+c-b)/(((m**2)+1)**0.5)
    
    
    
def sumdis(p,m,c):
    dissum=0
    for i in range(0,len(p)):
        dissum+=(dis(p[i][0],p[i][1],m,c))**2
    return dissum


if(__name__=='__main__'):
    m=0
    csum=0
    count=0
    #p=[[1,3],[-2,1],[-3,-2],[4,5],[5,-6],[-7,6],[-8,-7],[10,4]]
    p=creation("datafile.xml")
    x = np.linspace(0,len(p),100)
    for i in range(0,len(p)):
        for j in range(i+1,len(p)):
            m1=(p[j][1]-p[i][1])/(p[j][0]-p[i][0])
            c1=(-m1*p[i][0])+p[i][1]
            m+=m1
            csum+=c1
            count+=1
        plt.plot(p[i][0],p[i][1],'bo')
    d=0
    m/=count
    c=csum/count
    k=100
    r=c+k
    l=c-k
    while d<1000:
        if (sumdis(p,m,c)>sumdis(p,m,r)):
            l=c
            c=(c+r)/2
        elif (sumdis(p,m,c)>sumdis(p,m,l)):
            r=c
            c=(c+l)/2
        else:
            if (abs(sumdis(p,m,c)-sumdis(p,m,r))<abs(sumdis(p,m,c)-sumdis(p,m,l))):
                l=c
                c=(c+r)/2
            elif(abs(sumdis(p,m,c)-sumdis(p,m,r))>abs(sumdis(p,m,c)-sumdis(p,m,l))):
                r=c
                c=(c+l)/2
            else:
                if(r-l>-0.1 and r-l<0.1):
                    break
        d+=1
    y=m*x+c
    plt.plot(x, y, '-k')
    plt.show()
    while(True):
        print(m*(int(input())-1900)+c)
