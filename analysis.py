# Create DataFrame of the top 10 countries which search for BBC.COM
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["CNN.COM"])
data = trends.interest_by_region()
data = data.sort_values(by="CNN.COM", ascending=False)
data = data.head(10)
print(data)

# visualize this data using a bar chart
data.reset_index().plot(x="geoName", 
                        y="CNN.COM", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

# trend of searches over the years
data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['CNN.COM'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['CNN.COM'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for CNN.COM', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()


