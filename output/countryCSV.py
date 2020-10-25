import pandas as pd
data=pd.read_csv("main.csv",index_col=False)
#options=['USA (CA)','USA (DC)']
rst=data[data["COUNTRY"].str.contains("USA")]
print('\nResult data :\n',rst)
rst.to_csv("filteredCountry.csv",index=False)
