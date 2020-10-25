import pandas as pd
filteredCountry=pd.read_csv("filteredCountry.csv")
price=dict()
for index,row in filteredCountry.iterrows():
    if row['SKU'] in price:
        price[row['SKU']].append(float(str(row['PRICE']).replace('.00','').replace('$','').replace(',','').replace('?','')))
    else:
        price[row['SKU']]=[float(str(row['PRICE']).replace('.00','').replace('$','').replace(',','').replace('?',''))]
sortedPrice=pd.DataFrame(columns=['SKU','FIRST_MINIMUM_PRICE','SECOND_MINIMUM_PRICE'])
i=0
for SKU,p in price.items():
    if len(p)>1:
        sortedPrice.loc[i]=[SKU,sorted(p)[0],sorted(p)[1]]
        i=i+1
sortedPrice.to_csv('lowestPrice.csv',index=False)
