def nice_plot(to_plot, text_x_label):
    import matplotlib.pyplot as plt 
    import numpy as np
    plt.figure()
    plt.plot(np.linspace(0, 100, num=len(to_plot)), to_plot)
    plt.xticks(np.linspace(0, 100, num=len(to_plot)),text_x_label)
    plt.ylabel("Y label")
    plt.xlabel("X label")
    plt.title("Title")
#    plt.savefig(path_graph)
    plt.show()
    plt.close()

nice_plot([[1,2,3],[2,3,0],[6,9,3]],["jhgg", "jgjhg", "ookok"])
nice_plot([3,10,1],["jhgg", "jgjhg", "ookok"])