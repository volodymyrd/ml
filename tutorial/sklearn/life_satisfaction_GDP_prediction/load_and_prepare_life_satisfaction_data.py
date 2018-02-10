import pandas as pd
from tabulate import tabulate

datapath = "data"
oecd_bli = pd.read_csv(datapath + "/oecd_bli_2015.csv", thousands=',')
print(tabulate(oecd_bli.head(2), headers='keys'))
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
print(tabulate(oecd_bli.head(2), headers='keys'))