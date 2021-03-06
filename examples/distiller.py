from equipment import *
from .inputs import *


#region INPUTS
bd = Distiller(0.01, boilup_rate=10)
bd.Mixture = n
p1 = Pipe(0.1,1)
t1 = Tank(0.01)
t1.Mixture = m
t1.X = bd.Width*4
p1.FromTop = bd
p1.ToTop = t1
#endregion

#region PLOTS:
def plot():
    t_list = []
    # x1_list = []
    # x2_list = []
    x_list = []
    y_list = []
    t = 0
    for i in np.arange(0,10000,1):
        t += bd.dt
        t_list.append(t)
        # x1_list.append(bd.NextMixture.MolarFractions[0])
        # x2_list.append(bd.NextMixture.MolarFractions[1])
        x_list.append(bd.xi[0])
        y_list.append(bd.yi[0])
    plt.plot(t_list,x_list,t_list,y_list)
    plt.xlim(0,1000)
    plt.ylim(0,1)
    plt.show()
#endregion

#region ANIMATION:

# Canvas
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8,8)
ax = plt.axes(xlim=(-0.5, 5.5), ylim=(-0.5, 4.5))

# Animation Function
def init():
    ax.add_patch(bd.DrawContour)
    ax.add_patch(p1.DrawContour)
    ax.add_patch(t1.DrawContour)
    return bd.DrawContour, p1.DrawContour, t1.DrawContour

def draw(DrawObjects):
    for o in DrawObjects:
        ax.add_patch(o)

def animate(i):
    # Inlets and Outlets
    p1.Inlet = bd.Outlet
    t1.Inlets = [p1.Outlet]
    
    # NextTime function
    bd.NextTime
    t1.NextTime
    
    # Drawings
    patches = []
    patches.append(bd.DrawLiquid)
    patches.append(bd.DrawTopArrow)
    patches.append(p1.DrawContour)
    patches.append(t1.DrawContour)
    patches.append(t1.DrawLiquid)
    # print(bd.Mixture.Mass, t1.Mixture.Mass)
    # print(bd.Mixture.Moles, t1.Mixture.Moles)
    # print(bd.Mixture.MolarFractions, t1.Mixture.MolarFractions)
    for patch in patches:
        ax.add_patch(patch)
    return patches

#endregion

# Function Call
def show_animation():
    anim = animation.FuncAnimation(fig,animate,init_func=init,frames=1000,interval=30,blit=True)
    plt.show()
