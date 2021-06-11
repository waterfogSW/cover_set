from Mkdir import createFolder 
import matplotlib.pyplot as plt

# 시각화
def scatter_circles(selected_point, radius, data, P):
    createFolder("result")
    title = './result/radius_' + str(radius) + ".png"

    fig, ax_nstd = plt.subplots(figsize=(8, 8))
    
    plt.scatter(data['X'],data['Y'], s=5, alpha=0.7)
    if (P==None):
        for Cx, Cy in selected_point:
            plt.scatter(Cx, Cy, color = 'k', marker = 'x', s = 10)
            ax_nstd.add_patch(plt.Circle((Cx, Cy), radius, color='g', alpha=0.3))
    else:
        for Cx, Cy in selected_point:
            plt.scatter(Cx, Cy, color = 'k', marker = 'x', s = 10, c=P)
            ax_nstd.add_patch(plt.Circle((Cx, Cy), radius, color='lavender', alpha=0.3))
    plt.show()
    plt.savefig(title)