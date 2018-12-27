from math import *
from time import sleep
from Tkinter import *
from numpy import *
def matriz(n,m):#DEFINA LA MATRIZ
    M=[]
    for i in range(n):
        M.append([0]*m)
    return M
def vector(n): #DEFINE EL VECTOR
    v=[]
    for i in range(n):
        v.append(0)
    return v
print 'f(x1,x2)=x1^2+e^{x2^2}'#funcion
print 'gradiente de f(x1,x2)= [2.x1 ,  2.x2.e^{x2^2}]'
print 'gradiente^2 f(x1,x2)=[[2 , 0] , [0 , e^{x2^2}.(2+4.x2^2)]]'
x=matriz(1,2)
d=matriz(1,2)
print 'ingrese los puntos del vector inicial'#x0
for i in range(2):
    x[0][i]=input('')
print 'x_0=',x[0]
print '   f(x_0)=',(x[0][0]**2+e**(x[0][1]**2))
d=matriz(1,2)
def newton(x,d,it):
    g=vector(2)
    g[0]=2*x[it][0]
    g[1]=2*x[it][1]*exp(x[it][1]**2)
    g2=matriz(2,2)
    g2[0][0]=-2
    g2[0][1]=0
    g2[1][0]=0
    g2[1][1]=-(2+4*x[it][1]**2)*exp(x[it][1]**2)
    ig2=linalg.inv(g2)
    print 'gradiente f(x_%d)='%it,g
    print '-(gradiente^2 f(x_%d))^{-1}='%it,g2
    d[it][0]=ig2[0][0]*g[0]+ig2[0][1]*g[1]
    d[it][1]=ig2[1][0]*g[0]+ig2[1][1]*g[1]
    print 'd_%d='%(it),d[it]
    print ''
    x.append([0]*2)
    x[it+1][0]=x[it][0]+d[it][0]
    x[it+1][1]=x[it][1]+d[it][1]
it=0
while it <10:
    newton(x,d,it)
    print 'x_%d='%(it+1),x[it+1]
    print '   f(x_%d)='%(it+1),(x[it][0]**2+exp(x[it][1]**2))
    d.append([0]*2)
    it+=1
sleep(40)
