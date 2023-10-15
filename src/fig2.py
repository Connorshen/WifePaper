from src.base_fig import BaseFig
import pandas as pd
import matplotlib.pyplot as plt
from os import path


class Fig2(BaseFig):
    def paint(self):
        df = pd.read_excel("../data/NvP DEG-Significant.xls", sheet_name="miRNA_diff_significant", index_col=0)
        # 柱状图宽度
        col_width = 0.4
        n_mean_cpm = df.loc[:, "N_mean_CPM"]
        p_mean_cpm = df.loc[:, "P_mean_CPM"]
        plt.figure(figsize=(10, 6))  # 宽度为8英寸，高度为6英寸
        plt.bar(x=[i - col_width / 2 + 1 for i in range(len(n_mean_cpm))], height=n_mean_cpm, width=col_width,
                label="N", color="gray")
        plt.bar(x=[i + col_width / 2 + 1 for i in range(len(p_mean_cpm))], height=p_mean_cpm, width=col_width,
                label="P", color="black")
        plt.yscale('symlog')
        plt.ylabel('mean cpm')
        plt.xticks([i + 1 for i in range(len(n_mean_cpm))], df.index.values, rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.savefig(path.join(self.OUTPUT_DIR, f"{self.__class__.__name__}.png"))


fig = Fig2()
fig.paint()
