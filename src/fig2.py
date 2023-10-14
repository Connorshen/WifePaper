from src.base_fig import BaseFig
import pandas as pd
import matplotlib.pyplot as plt


class Fig2(BaseFig):
    def paint(self):
        df = pd.read_excel("../data/NvP DEG-Significant.xls", sheet_name="miRNA_diff_significant")
        # 柱状图宽度
        col_width = 0.4
        n_mean_cpm = df.loc[:, "N_mean_CPM"]
        p_mean_cpm = df.loc[:, "P_mean_CPM"]
        plt.bar([i - col_width / 2 + 1 for i in range(len(n_mean_cpm))], n_mean_cpm, width=col_width,
                label="N_mean_CPM")
        plt.bar([i + col_width / 2 + 1 for i in range(len(p_mean_cpm))], p_mean_cpm, width=col_width,
                label="P_mean_CPM")
        plt.yscale('log')
        plt.legend()
        plt.show()


fig = Fig2()
fig.paint()
