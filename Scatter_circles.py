from Mkdir import createFolder 
import matplotlib.pyplot as plt

# 시각화
def scatter_circles(selected_point, radius, data, P):
    createFolder("result")
    title = './result/radius_' + str(radius) + ".png"

    fig, ax_nstd = plt.subplots(figsize=(8, 8))

    if P.size == 0:
        plt.scatter(data['X'],data['Y'], s=5, alpha=0.7)
    else:
        plt.scatter(data['X'],data['Y'], s=5, alpha=0.7, c=P)

    for Cx, Cy in selected_point:
        plt.scatter(Cx, Cy, color = 'k', marker = 'x', s = 10)
        ax_nstd.add_patch(plt.Circle((Cx, Cy), radius,fill=False, alpha = 0.7))
            
    plt.show()
    plt.savefig(title)