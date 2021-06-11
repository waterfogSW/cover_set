import matplotlib.pyplot as plt
# 시각화
def scatter_circles(selected_point, radius, data):

    fig, ax_nstd = plt.subplots(figsize=(8, 8))

    plt.scatter(data['X'],data['Y'], s=5, alpha=0.7)
    for Cx, Cy in selected_point:
        plt.scatter(Cx, Cy, color = 'k', marker = 'x', s = 10)
        ax_nstd.add_patch(plt.Circle((Cx, Cy), radius, color='g', alpha=0.3))
    plt.show()
    plt.savefig('scatter.png')