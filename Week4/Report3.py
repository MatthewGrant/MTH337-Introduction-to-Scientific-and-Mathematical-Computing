
# Report 4 : Mayfly Population
# MTH 337
# Matt Grant

#get_ipython().magic(u'pylab')
#%matplotlib
from pylab import *
style.use('ggplot')
import matplotlib.patches as mpatches

# In[3]:

def mayfly(x,b,t):
    ''' Function in which mayfly(x,b,tmin,tmax): 
    x, population as percent of max, 
    b, ratio of surviving offspring to females, 
    t, Generations'''
    for i in range(t):
        x = b*(1-x)*x
        # x = population (% max)
        # b = a0/2 or surviving offspring per female 
        
        #print x
        figure(num=1, figsize=(6, 5))
        plot(i,x,'c.')
        title('Mayfly Population over Time')
        xlabel('Time (Years)')
        ylabel('Population (x)')
        patch = mpatches.Patch(color='c', label='Growth Rate b: %s'%b)
        legend(handles=[patch])
    savefig('fig1.svg',  dpi=1000)

#
mayfly(.5,2.7,20)

#
def asym_plot(bmin,bmax,fig=2,markerSize=2.5):
    tmax = 500
    tmin = tmax/2

    b = linspace(bmin,bmax, 301)
    x = .5 #b = 0-3.57, Population independent
    for i in xrange(tmax):
        if i >= tmin: 
            figure(fig)
            #subplot(2,3,plot_number)
            plot(b,x,'c.',ms=markerSize)
            title('Mayfly Population over Time')
            xlabel('Growth Rate (b)')
            ylabel('Total Population Size')
        x = b*(1-x)*x   
    #savefig('fig8.svg')

#figure 2
asym_plot(0,2)

#Figure 3
asym_plot(1,3, fig=3)

#Figure 4
asym_plot(2.9,3.45, fig=4)

#Figure 5
asym_plot(3.44,3.55, fig=5)

#Figure 6
asym_plot(3.54,3.565, fig=6)

#Figure 7
asym_plot(3.60,4,fig=7,markerSize=2)

#Figure 8
asym_plot(3.846,3.860,fig=8,markerSize=2)


