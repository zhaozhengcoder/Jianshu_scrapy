import matplotlib.pyplot as plt
import numpy as np


def show_top_author(new_merge_list):
    xlist=[]
    ylist=[]
    for item in new_merge_list:
        xlist.append(item[2])
        ylist.append(item[3]) 
    colors = np.random.rand(len(new_merge_list)) # 随机产生50个0~1之间的颜色值
    area = np.pi * (10 * np.random.rand(len(new_merge_list)))**2  # 点的半径范围:0~10
    # 画散点图
    plt.scatter(xlist,ylist, s=area, c=colors, alpha=0.5, marker=(9, 3, 30))
    plt.show()