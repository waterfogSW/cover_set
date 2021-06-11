from Mkdir import createFolder 
import matplotlib.pyplot as plt

# 시각화
def scatter_circles(selected_point, radius, data, P):
    createFolder("result")
    title = './result/radius_' + str(radius) + ".png"

    fig, ax_nstd = plt.subplots(figsize=(8, 8))

    if P is None:
        # [Item 23] Provide Optional Behavior with Keyword Arguments
        # matplot 라이브러리의 scatter함수는 keyword argumnet를 통해 직관적인 옵션을 제공합니다.
        plt.scatter(data['X'],data['Y'], s=5, alpha=0.7)
    else:
        plt.scatter(data['X'],data['Y'], s=5, alpha=0.7, c=P)

    for Cx, Cy in selected_point:
        plt.scatter(Cx, Cy, color = 'k', marker = 'x', s = 10)
        ax_nstd.add_patch(plt.Circle((Cx, Cy), radius,fill=False, alpha = 0.7))
            
    plt.show()

    # Linux shell에서는 plt.show()의 GUI를 지원하지 않아 result폴더에 따로 결과를 저장함.
    plt.savefig(title)
