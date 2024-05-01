import pandas as pd

file_name = "C:/Users/ceut1/Documents/repositorios/Python_be/Archive/AmazonSaleReport.csv"
df_AmazonSalesReport = pd.read_csv(file_name, encoding="utf-8", delimiter=",", low_memory=False)

# Graphic
status_quantity = list(df_AmazonSalesReport.sort_values(by="Status").groupby(["Status"])["Status"].count())
status = df_AmazonSalesReport[["Status"]]
status_list = status.sort_values(by="Status").drop_duplicates("Status")
status_name = status_list["Status"].values.tolist()



