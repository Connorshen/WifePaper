from src.base_fig import BaseFig
import pandas as pd


class Fig1(BaseFig):
    def paint(self):
        blue_count, yellow_count, same_count = [0, 0, 0]
        df = pd.read_excel("../data/miRNA_all_miRNA_exp.xlsx", sheet_name="miRNA_all_miRNA_exp")
        blue_df = df.loc[:,
                  ["LF_LH_7_2363", "LXY_LH_7_2363", "CF_LH_7_516", "DJL_LH_7_2363", "DKQ_LH_7_2363", "WHX_LH_7_2363",
                   "WJ_LH_7_2363", "WTT_LH_7_2363", "ZWT_LH_7_2363"]]
        # yellow_df = df.loc[:,
        #             ["HRY_LH_7_2363", "WY_LH_7_2363", "XLM_LH_7_2363", "ZLY_LH_7_2363", "ZNN_LH_7_2363"]]
        yellow_df = df.iloc[:, -5:]
        for ind in blue_df.index:
            blue_row = blue_df.loc[ind][:]
            yellow_row = yellow_df.loc[ind][:]
            blue_row_mean = blue_row.mean()
            yellow_row_mean = yellow_row.mean()
            if blue_row_mean == 0:
                blue_count += 1
            if yellow_row_mean == 0:
                yellow_count += 1
            if blue_row_mean == 0 and yellow_row_mean == 0:
                same_count += 1
        print(blue_count, yellow_count, same_count)


fig = Fig1()
fig.paint()
