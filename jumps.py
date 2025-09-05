
import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import random
import matplotlib as mpl
import matplotlib.ticker as ticker



t1=2000
t2=25000
p=0.9
T=0.475
avibr=0.017
  

@njit
def vibr(avibr):
    return -avibr*np.log(1-np.random.random())
    
@njit      
def sign():
    if np.random.uniform(0,1) <0.5:
        return 1
    else:
        return -1
    
@njit
def tjump():
    x=np.random.random()
    
    if x<=p:
        return -t1*np.log(1-np.random.random())
    else:
        return -t2*np.log(1-np.random.random())

@njit
def hitime(x, xh):
    
    for l in range(x):
        xh=np.append(xh, int(tjump()))
    return xh

@njit
def rawalk(N, avibr):
    
    
    xi=np.zeros(N+1)
    xi[0]=0.


    jt=2
    jr=0.4
    ctjump=True
    tj=int(tjump())
    #tj=1000
    sjr=sign()*jr/jt
    print(tj)
    ns=0
    ti=np.arange(0,N+1)
    for k in range(1,N+1):
        
        vib=sign()*vibr(avibr)
        #vib=sign()*avibr
        #vib=np.random.normal(0.,np.sqrt(T))
        
        if ctjump==False:
            tj=int(tjump()) + k
            #tj=1000 + k
            ctjump=True
            sjr=sign()*jr/jt
            print('salto en: ' + str(tj))
        
        if k in np.arange(tj, tj+jt):
            f=1
            
            if k==tj+jt-1:
                ctjump=False
                ns= ns + 1
        else:
            f=0
        
        xi[k]=xi[k-1] + vib + sjr*f
        
    
    return xi,ti, ns

@njit
def counter(xf, dr, dt, Pwait):
    
    
    to=0
    n=0
    
    for k in range(0, len(xf)-dt, dt):
        
        d=abs(xf[k+dt]-xf[k])
        if d>=dr:
            Pwait=np.append(Pwait, k+dt-to)
            to=k+dt
            n=n+1
    
    if len(Pwait)!=0:

        tav= np.average(Pwait)
        var= np.var(Pwait)

        alpha=0.5*(1+var/(tav**2))

    else:
        alpha=0
    
    return n, alpha
        

def grafica(avibr):        

    cmap = plt.cm.viridis  # Choose a colormap
    norm = mpl.colors.Normalize(vmin=2, vmax=16)  # Normalize dt range
    sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm) 

    fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=False, figsize=(12, 6))

    xf, tf, salt= rawalk(23000000, avibr)
    print(salt)

    for dt in range(2,17, 2):
    
        alpha=np.array([])
        r=np.array([])
        obs=np.array([])
        dr=0.16
        while dr<0.51:
        
            Pwait=np.array([])
            sob, alph= counter(xf, dr, dt, Pwait)
        
            alpha=np.append(alpha, alph)
            r=np.append(r, dr)
            obs=np.append(obs, sob/salt)
        
            print('Saltos observados: ' + str(sob))
            print('alpha: ' + str(alph))
        
            dr=dr+0.02
        
        ax0.plot(r, alpha,marker='o', label=f'dt={dt}', color=cmap(norm(dt)))
        ax1.plot(r, obs, marker='o', label=f'dt={dt}', color=cmap(norm(dt)))


    # colorbar
    cbar = plt.colorbar(sm, ax=ax1, pad=0.02)
    cbar.set_label(r"$\Delta t$", fontsize=12)

    # Subplot 1 (Alpha vs Delta r)
    ax0.set_title(r'', fontsize=12)
    ax0.set_xlabel(r'$\Delta r$', fontsize=20)
    ax0.set_ylabel(r'$\alpha$', fontsize=20)
    

    # Subplot 2 (No/Nr vs Delta r)
    ax1.set_title(r'', fontsize=12)
    ax1.set_yscale('log')
    ax1.set_xlabel(r'$\Delta r$', fontsize=20)
    ax1.set_ylabel(r'$N/ N_r$', fontsize=20)
    x=np.arange(0.14, 0.52, 0.01)
    const=np.zeros(len(x))
    const[:]=1.
    ax1.plot(x, const, linestyle='--', color='b', alpha=0.5)
    #ax1.grid(visible=True, which="both", axis="y", linestyle="--", linewidth=0.5)



    # Adjust spacing
    plt.subplots_adjust(wspace=0.3)


    plt.figure(dpi=600)


    plt.show()

    return

grafica(avibr)

#N=30000
#n=5 #number of simulations

#plt.ylim([-3, 3])

#colors=np.array(['b', 'r', 'y', 'g', 'black'])

#for j in range(n):
    
  #  xi,ti, ns=rawalk(N, 0.017)    

   # plt.plot(ti, xi, color=colors[j], linewidth=0.75)

#plt.xlabel(r't',fontsize=10)
#plt.ylabel(r'x',fontsize=10)
#plt.title('Velocidad de vibraciones media: ' + str(avibr))
#plt.show()      
