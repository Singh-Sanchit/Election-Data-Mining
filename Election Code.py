
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#===== Merging two excel files====
df = pd.DataFrame()

for f in ['C:\\Datasets\\elections\\2009maharashtraresults.xlsx', 'C:\\Datasets\\elections\\2014maharashtraresults.xlsx']:
    data = pd.read_excel(f, 'Sheet1') #this loop merges the two excel sheets into one.
    df = df.append(data)

df.to_excel("C:\\Datasets\\elections\\combineddata.xlsx")#resultant data is stored in this third excel sheet
data = pd.read_excel("C:\\Datasets\\elections\\combineddata.xlsx")
print(data)

plt.figure(figsize=(8, 4))
plt.scatter(
    data['PARTYNAME'],
    data['SEATS'],
    c='blue'
)
plt.xlabel("Party)")
plt.ylabel("Seats Won")
plt.xticks(rotation=90) # to print party names vertically
plt.show()

#=============================================================================
for i in data['PARTYNAME']:
     x = i
     t1 = (data[(data.PARTYNAME == x) & (data.YEAR == 2009)].SEATS).tolist() #retriving seats of similar partyname & at the same time converting it to List from panda.Series datatype
     t2 = (data[(data.PARTYNAME == x) & (data.YEAR == 2014)].SEATS).tolist() #retriving seats of similar partyname & at the same time converting it to List from panda.Series datatype
     t3 = t1 + t2 #combining both the list element into 1 list instead of adding here because either t1 or t2 can be empty as their record can be absent in dataset
     print("--------------")
     print ("Name of Party =", i)
     print ("NUMBER OF SEATS =", sum(t3)) #sum() function will add all the elements present into the list
     print("--------------")
# =============================================================================




