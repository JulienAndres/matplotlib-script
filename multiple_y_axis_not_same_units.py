def nice_plot(infos_list,infos_text,list_min,list_max):
    import matplotlib.pyplot as plt 
    import numpy as np
    #infos_list = list of value for this screen
    #list_min = list of min of all values for all infos
    #list_max = list of max of all values for all infos
    
    fig, ax = plt.subplots()
    axes = [ax.twinx() for _ in range(len(infos_list) - 1)]
    axes = [ax]+axes
    #axe location
    fig.subplots_adjust(right=0.75)
    axes[-1].spines['right'].set_position(('axes', 1.2))
    axes[-1].set_frame_on(True)
    axes[-1].patch.set_visible(False)
    
    # plot things...
    uni = np.linspace(0,100,num=len(infos_list))
    cpt=-1
    colors = [(rd.uniform(0, 1), rd.uniform(0, 1), rd.uniform(0, 1)) for _ in range(len(infos_list))]
    for ax, color in zip(axes, colors):
        cpt+=1
        ax.plot(uni[cpt],infos_list[cpt], marker='o', linestyle='none', color=color)
        ax.set_ylim(list_min[cpt],list_max[cpt])
        ax.tick_params(axis='y', colors=color)
    plt.xticks(uni,infos_text)
    axes[0].set_xlabel('X-axis')
    
    plt.show()

nice_plot([1,35,700],["info_"+str(i) for i in range(3)],[0,30,100],[10,40,1000])