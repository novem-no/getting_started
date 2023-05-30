import pandas as pd
from novem import Plot
from novem.colors import StaticColor as SC, DynamicColor as DC, USEDATA as _
from novem.table import Selector as S

# let's grab some sample data
df = pd.read_csv('https://data.novem.no/v1/examples/plot/nei_rgn_hier.csv', index_col=0)

tb = Plot('nei_rgn_hier', type="table")

# add our data
df.pipe(tb)

# right align our nmbers
tb.cell.align    = S(df.loc[:, "NAV":], ">", r=df)

tb.cell.format   = S(df.loc[:, "NAV"], ",.1f", r=df)
tb.cell.format  += S(df.loc[:, "DTD":], ",.1%", r=df)

# use index colors
tb.colors.type = 'ix'

# let's add a some shaded hierarhcy colors
tb.colors  = S(df.loc[df.level == 0, :], SC("bg","gray-500","gray-600"), r=df, c=':')
tb.colors += S(df.loc[df.level == 1, :], SC("bg","gray-400","gray-700"), r=df, c=':')
tb.colors += S(df.loc[df.level == 2, :], SC("bg","gray-300","gray-800"), r=df, c=':')

# create individual heatmaps for our country performance columns
hmap = DC("bg","red-200","neutral","green-200",_,0,_)
tb.colors += S(df.loc[df.level == 3, "DTD"], hmap, r=df)
tb.colors += S(df.loc[df.level == 3, "WTD"], hmap, r=df)
tb.colors += S(df.loc[df.level == 3, "MTD"], hmap, r=df)
tb.colors += S(df.loc[df.level == 3, "QTD"], hmap, r=df)
tb.colors += S(df.loc[df.level == 3, "YTD"], hmap, r=df)

# Add some spacing around our numbers
tb.cell.padding  = S(df.loc[:, :], "x 1", r=df)
#tb.cell.padding += S(df.loc[:, :], "r 1", r=df)

# add hierarchiacl indentation to our index column
tb.cell.padding += S(df.loc[df.level == 1], 'l 1', r=df, c='0')
tb.cell.padding += S(df.loc[df.level == 2], 'l 2', r=df, c='0')
tb.cell.padding += S(df.loc[df.level == 3], 'l 3', r=df, c='0')

# finaly let's bold the text and add a bottom border to the top row, we'll add
# this manually as pandas slicing doens't make it easy to slice for the index
# row
tb.cell.border = '0 : b 1 inverse'   # row 0, all columns, bottom 1 wide border
                                     # with the "inverse" color
tb.cell.text   = '0 : b'             # row 0, all columns, bold text

df.drop(columns=['level']).pipe(tb)

# name of the visualisation
tb.name = "Novem Example Index - Geographic Performance Breakdown"

# small caption for the table
tb.caption = """The above table shows the performance breakdown of the Novem
Example Index by return periods and geography.

Returns are structured so that each country show the weighted contriubiton of their
underlying stocks, with sub regions showing the weighted contribution of their countries
and so on. The world performance is identical to the aggreaget performance of the Novem
Example Index.

Data from nasdaq and yahoo finance, calculations by novem, all numbers as of 10th of
November 2022."""

# summary for listings
tb.summary = "Novem Example Index performance by geography"

# share it with the world
tb.shared += 'public'

# let's print our url
print(tb.url) # https://novem.no/p/NJy4w

# Set the render type
tb.type = 'mtable'

# Write a description with demo code
with open(__file__,'r') as f:
  ctnt = f.read().replace('````','```') # turtles

  desc = f"""
# A region breakdown heatmap

A table showing performance by time and geography dimensions.

````
{ctnt}
````

"""

  tb.description = desc
