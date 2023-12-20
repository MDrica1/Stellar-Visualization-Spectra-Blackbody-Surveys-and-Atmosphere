import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.analytic_functions import blackbody_lambda
import astropy.io.fits as pf
from matplotlib.colors import LogNorm


stars=['F4V_HD87822.fits','G1.5V_HD20619.fits','K5V_HD36003.fits','M0.5V_HD209290.fits']
l=['F4.png','G1.png','K5.png','M0.png']
idt=['HD 87822 (F4 V)', 'HD 20619 (G1.5 V)','HD 36003 (K5 V)', 'HD 209290 (M0.5 V)']
col=['navy','crimson','green','teal']
flambdall=[4.73311*10**-12, 1.92717*10**-11, 6.23593*10**-12, 5.3286*10**-13] #olhar de novo e escolher outro lambda pq esse ta dando eh problema vi
a=[10, 1, 4.75, 1]
Teff=[6586,5703,4647,3580]
lambdall=[2.01732,1.05658,1.98832,3.62321]
star_type=['F4','G1','K5','M0']

def plota_corpo_negro(indice):
    hdu = pf.open(stars[0][indice])
    head = hdu[0].header
    data = hdu[0].data
    
    x=data[0]
    X=x[np.where(np.isnan(x)==False)]
    y=data[1]
    yerr=data[2]    
    fig=plt.figure()
    fig.add_subplot(111)
    plt.xlabel(u'Wavelength ($\mathrm{\mu m}$)')
    plt.ylabel(u'Fluxo normalizado ($\mathrm{\\frac{F_\lambda}{F_{\lambda^l}}})$')
    plt.title(idt[indice])
    plt.errorbar(x,y/flambdall[indice],yerr=yerr,fmt='--',color=col[indice],linewidth=0.2)
    plt.hold('on')
    plt.loglog(x,y/flambdall[indice],ls='-',color=col[indice],linewidth=0.2)
    plt.loglog(X,blackbody_lambda(X*u.um,Teff[indice]*u.K)/blackbody_lambda(lambdall[indice]*u.um,Teff[indice]*u.K),color='k')
    plt.legend(['Espectro da estrela','Curva de corpo negro da estrela','Erro do fluxo'])
    if star_type[indice] == 'F4':
        plt.text(2.4,3.1,'$\lambda^l = 2.01732\,\mu m$', fontsize=12)
    elif star_type[indice] == 'G1':
        plt.text(2.5,0.37,'$\lambda^l = 1.05658\,\mu m$',fontsize=12)
    elif star_type[indice] == 'K5':
        plt.text(2.35,1.79,'$\lambda^l = 1.98832\,\mu m$',fontsize=12)
    elif star_type[indice] == 'M0':
        plt.text(2.7,8,'$\lambda^l = 3.62321\,\mu m$',fontsize=12)
    plt.savefig(l[indice])
    return fig
    #plt.show()
    
figs =[]
for i in range(len(stars)):
    figs.append(plota_corpo_negro(i))

j=['f4t.png','gt.png','kt.png','mt.png']
maximos=[6.2*10**-11,3.24*10**-11,3.3*10**-11,1.5*10**-11]
atm = ['atran.plt.0.85-1.5.dat','atran.plt.1.5-2.4.dat','atran.plt.2.4-4.4.dat','atran.plt.4-7.2.dat','atran.plt.7.2-12.dat','atran.plt.12-22.dat','atran.plt.22-36.dat']

def ler_txt(arquivo):
    x,y = np.genfromtxt(arquivo, usecols=(1,2))
    return x,y

for i in range(len(atm)):
    x_i,y_i = ler_txt(atm[i])

def plota_atm(indice):
    hdu = pf.open(stars[0][indice])
    head = hdu[0].header
    data = hdu[0].data
    
    x=data[0]
    #X=x[np.where(np.isnan(x)==False)]
    y=data[1]
    yerr=data[2]    
    fig=plt.figure()
    fig.add_subplot(111)
    plt.xlabel(u'Wavelength ($\mathrm{\mu m}$)')
    plt.ylabel(u'Fluxo normalizado ($\mathrm{\\frac{F_\lambda}{F_{\lambda^l}}})$')
    plt.title(idt[indice])
    plt.errorbar(x,y/(maximos[indice]),yerr=yerr,fmt='--',color=col[indice],linewidth=0.2)
    plt.hold('on')
    plt.loglog(x_0*u.um,,y_0/(maximos[indice]),ls='-',color=pink,linewidth=0.2)
    plt.loglog(x_1*u.um,,y_1/(maximos[indice]),ls='-',color=pink,linewidth=0.2)
    plt.loglog(x_2*u.um,,y_2/(maximos[indice]),ls='-',color=pink,linewidth=0.2)
    plt.loglog(x_3*u.um,,y_3/(maximos[indice]),ls='-',pink,linewidth=0.2)
    plt.xlim(xmax=6)
    plt.legend(['Espectro da estrela','Transmissao da atmosfera'], loc=1,fontsize=7)])
    plt.savefig(j[indice])
    #plt.show()
    return fig
    #plt.show()

figs_atm=[]
for i in range(4):
    figs_atm.append(plota_atm(i))

# Figura com 3 gráficos

T = [30000, 15000, 8500, 7000, 5000, 4000, 3000]
color=['orangered','green','teal','purple','brown','fuchsia','blue']
x = np.arange(0, 2100000)
ax1 = plt.subplot(311)
ax1.set_ylim(0,1)
ax1.set_xlim(300,2100000)
ax1.set_ylabel('B$_\lambda$(T) (s$^\mathrm{-1}$ cm$^\mathrm{-2}$ A$^\mathrm{-1}$ Sr$^\mathrm{-1}$)')
ax1.set_title('Radiacao de corpo negro/Curvas de transmissao')
ax1.semilogx(x,blackbody_lambda(x*u.AA,T[6])/10**6, color=color[6])

# Plota a curva de corpo negro
for i in range(6):
    ax1.plot(x,blackbody_lambda(x*u.AA,T[i])/10**6,color=color[i])

ax1.annotate('3000 K', xy=(10**3.8,0.15),fontsize=8,color='blue')
ax1.text(10**3.55,0.45, '4000 K', rotation=55, fontsize=8,color='fuchsia')
ax1.text(10**3.4,0.6, '5000 K', rotation=76, fontsize=8,color='brown')
ax1.text(1390,0.7, '7000 K', rotation=85, fontsize=8,color='purple')
ax1.text(950,0.8, '8500 K', rotation=85, fontsize=8,color='teal')
ax1.text(400,0.9, '15000 K', rotation=85, fontsize=8,color='green')
ax1.text(25126,0.6, '30000 K', rotation=282, fontsize=8,color='orangered')


# Surveys astronômicos

ax2 = plt.subplot(312, sharex=ax1)
ax2.set_xlim(300,2100000)

mass = ['2MASS_2MASS.J.dat','2MASS_2MASS.H.dat','2MASS_2MASS.Ks.dat']
WISE = ['WISE_WISE.W1.dat','WISE_WISE.W2.dat','WISE_WISE.W3.dat','WISE_WISE.W4.dat']
Spitzer = ['Spitzer_IRAC.I1.dat','Spitzer_IRAC.I2.dat','Spitzer_IRAC.I3.dat','Spitzer_IRAC.I4.dat','Spitzer-MIPS.24mu.dat','Spitzer-MIPS.70mu.dat','Spitzer-MIPS.160mu.dat']
IRAS = ['IRAS_IRAS.100mu.dat','IRAS_IRAS.60mu.dat','IRAS_IRAS.25mu.dat','IRAS_IRAS.12mu.dat']
UKIDSS = ['UKIRT_UKIDSS.J.dat','UKIRT_UKIDSS.K.dat','UKIRT_UKIDSS.Y.dat','UKIRT_UKIDSS.Z.dat','UKIRT_UKIDSS.H.dat']
Hipparcos = ['Hipparcos_Hipparcos.Hp.dat','Hipparcos_Hipparcos.Hp_bes.dat','Hipparcos_Hipparcos.Hp_MvB.dat']
GAIA = ['GAIA_GAIA0.G.dat','GAIA_GAIA0.Gbp.dat','GAIA_GAIA0.Grp.dat']
IPHAS =['INT_IPHAS.gI.dat','INT_IPHAS.gR.dat','INT_IPHAS.Ha.dat']
SDSS = ['SLOAN_SDSS.g.dat','SLOAN_SDSS.i.dat','SLOAN_SDSS.r.dat','SLOAN_SDSS.u.dat','SLOAN_SDSS.z.dat']
GALEX = ['GALEX_GALEX.FUV.dat','GALEX_GALEX.NUV.dat']
Kepler = ['Kepler_Kepler.K.dat']

surveys = [mass,WISE,Spitzer,IRAS,UKIDSS,Hipparcos,GAIA,IPHAS,Kepler,SDSS,GALEX]
color = ['coral','crimson','orchid','maroon','indigo','lightgreen','gold','red','c','grey','teal']

def ler_t(arquivo):
    x = np.genfromtxt(arquivo)
    return x.T

cont = len(surveys) - 1
for j in surveys:
    it = len(j)
    if j == 'mass':
        
        for i in j:
            if it == len(j):
                f = ler_t(j[i])
                ax2.plot(f[0],f[1], color=color[cont],label='2MASS') 
                cont = cont - 1
                it = it - 1
            else:
                f = ler_t(j[i])
                ax2.plot(f[0],f[1], color=color[cont]) 
                cont = cont - 1
                it = it - 1
    else:
        for i in j:
            if it == len(j):
                f = ler_t(j[i])
                ax2.plot(f[0],f[1], color=color[cont],label=j) 
                cont = cont - 1
                it = it - 1
            else:
                f = ler_t(j[i])
                ax2.plot(f[0],f[1], color=color[cont]) 
                cont = cont - 1
                it = it - 1


ax2.legend(fontsize=6,ncol=2,loc=2,borderaxespad=0.1,frameon=False) #o 2 coloca a legenda upper left

# Curva de transmissão da atmosfera
 
ax3=plt.subplot(313)
#ax3.set_xlim()
ax3.set_xlabel('Wavelength ($\AA$)')
x=[x_0,x_1,x_2,x_3,x_4,x_5,x_6]
y=[y_0,y_1,y_2,y_3,y_4,y_5,y_6]
ax3.plot(x[6],y[6],ls='-',color='lightgreen')
ax3.hold('on')
ax3.plot(x[5],y[5],ls='-',color='lightgreen')
ax3.plot(x[4],y[4],ls='-',color='lightgreen') 
ax3.plot(x[3],y[3],ls='-',color='lightgreen')
ax3.plot(x[2],y[2],ls='-',color='lightgreen')
ax3.plot(x[1],y[1],ls='-',color='lightgreen')
ax3.plot(x[0],y[0],ls='-',color='lightgreen')
ax3.legend(['Curva de transmissao da atmosfera'],fontsize=6,loc=1)
plt.tight_layout(pad=0.3)
#plt.show()
plt.savefig('corponegro_transmissao-atmosfera.png')

