import pandas as pd
from novem import Plot

# let's grab some sample data
df = pd.read_csv('https://data.novem.no/v1/examples/plot/nei_rgn_perf.csv', index_col=0)

plt = Plot('nei_rgn_perf', type='line')

# add our data
df.pipe(plt)

# name of the visualisation
plt.name = "Novem Example Index - Performance History"

# set colored lines as label format
plt.config.legend.format = "%cl %l"

# summary for listings
plt.summary = "Performance history by region"

# add a caption to the table
plt.caption = """The above chart shows the Year To Date performance for the 
Novem Example Index (NEI) as well as the performance of the key underlying regions.

Regional performance show the total performance of the region and not it's 
contribution to the aggregate NEI.
"""


# share it with the world
plt.shared += 'public'

# let's print our url
print(plt.url) # https://novem.no/p/NJy4w

with open(__file__,'r') as f:
  ctnt = f.read().replace('````','```') # turtles

  desc = f"""
# Novem Example Index - Performance history by region

A line chart showing historical performance by region

````
{ctnt}
````

"""

  plt.description = desc
