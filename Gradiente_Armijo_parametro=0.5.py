from math import *
from time import sleep
from Tkinter import *
from numpy import *
def dimKL(n):#ANALIZA la dimension del espacio de Krylov
    m=input('m = dim(K) = dim(L) = ')
    print ''
    if m<=n:
        return m
    else:
        print 'm no puede ser mayor que n. Ingrese de nuevo:'
        dimKL(n)
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
print 'f(x1,x2)=2.x1^2 + x1.x2 + 4.x2^2 '#funcion
print 'gradiente de f(x1,x2): (4.x1 + x2 , x1 + 8.x2)'
x=matriz(1,2)
d=matriz(1,2)
print 'parametro=0.5'
print 'ingrese los puntos del vector inicial'#x0
for i in range(2):
    x[0][i]=input('')
print 'x0=',x[0]
print 'f(x_0)=',(2*x[0][0]**2 + x[0][0]*x[0][1]+ 4*x[0][1]**2)

alpha=0.5
d=matriz(1,2)
def gradiente(x,d,it):
    g=vector(2)
    g[0]=4*x[it][0]+x[it][1]
    g[1]=x[it][0]+8*x[it][1]
    d[it][0]=-g[0]
    d[it][1]=-g[1]
    t=1
    while t<=1:
        a=2*(x[it][0]+t*d[it][0])**2+(x[it][0]+t*d[it][0])*(x[it][1]+t*d[it][1])+4*(x[it][1]+t*d[it][1])**2
        b=2*(x[it][0])**2+(x[it][0])*(x[it][1])+4*(x[it][1])**2+alpha*t*(g[0]*d[it][0]+g[1]*d[it][1])
        if a<=b:
            break
        else:
            t=t*0.5
    print 't_%d'%it,t
    print 'd_%d'%(it),d[it]
    print ''
    x.append([0]*2)
    x[it+1][0]=x[it][0]+t*d[it][0]
    x[it+1][1]=x[it][1]+t*d[it][1]
it=0
while it <6:
    gradiente(x,d,it)
    print 'x_%d'%(it+1),x[it+1]
    print 'f(x_%d)='%(it+1),(2*x[it][0]**2 + x[it][0]*x[it][1]+ 4*x[it][1]**2)
    d.append([0]*2)
    it+=1
sleep(40)
