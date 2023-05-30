import pandas as pd
from novem import Plot
from novem.colors import StaticColor as SC, DynamicColor as DC
from novem.table import Selector as S

# grab our example numbers from novem data
df = pd.read_csv('https://data.novem.no/v1/examples/plot/nei_rgn_tb.csv', index_col=0)

# let's convert our Contribution to bps, Basis points)
df['Contribution'] *= 10000

# Create a novem e-mail table `mtable`
tb = Plot('nei_rgn_tb', type='table') 

# add our data
df.pipe(tb)

# right align our nmbers
tb.cell.align    = S(df.loc[:, "NAV":], ">", df)


# add some spacing to the left and right of numbers
tb.cell.padding  = S(df.loc[:, :], "l 2", df)
tb.cell.padding += S(df.loc[:, :], "r 1", df)

# add some padding below the header
tb.cell.padding += S(df.iloc[0, :], "t 2", df, c=":")

# add some padding between the top and bottom performers
tb.cell.padding += S(df.iloc[9, :], "b 4", df, c=":")


# let's format our numbers, first set NAV and all following 
# numbers as decimal, then override Return as percent
tb.cell.format   = S(df.loc[:, "NAV":], ",.1f", df)
tb.cell.format  += S(df.loc[:, "Return"], ",.1%", df)


# use index colors
tb.colors.type = 'ix'

# let's highlight rows with an individual stock return above 10%
tb.colors  = S(df.loc[df["Return"] > 0.1, :], SC("bg", "green-100"), df, c=":")

# let's highlight rows with an individual stock return below -10%
tb.colors += S(df.loc[df["Return"] < -0.1, :], SC("bg", "red-100"), df, c=":")

# Let's create a foreground, green, heatmap for our top 10 performers,
# we crate an individual heatmap for Returns and Contributions
tb.colors += S(df.iloc[:10, -1], DC("fg", min="green-300", max="green-600"), df)
tb.colors += S(df.iloc[:10, -2], DC("fg", min="green-300", max="green-600"), df)

# repeat the above exercise but for our detractors
tb.colors += S(df.iloc[10:, -1], DC("fg", min="red-600", max="red-300"), df)
tb.colors += S(df.iloc[10:, -2], DC("fg", min="red-600", max="red-300"), df)


# finaly let's bold the text and add a bottom border to the top row, we'll add 
# this manually as pandas slicing doens't make it easy to slice for the index 
# row
tb.cell.border = '0 : b 1 inverse'   # row 0, all columns, bottom 1 wide border
                                     # with the "inverse" color
tb.cell.text   = '0 : b'             # row 0, all columns, bold text


# add a caption to the table
tb.caption = """The above table shows the top 10 and bottom 10 contributors 
to the Novem Example Index performance on the 10th of November 2022.

The return numbers are the individual stocks DTD return whereas the contribution
number is its individual contribution to the overall index expressen in basis points, 
NAV is in million USD."""

# Let's add a discriptive name
tb.name = "Novem Example Index - Top & Bottom Contributors\n"

# and a short summary
tb.summary = "Example table of top 10 and bottom 10 contributors to the novem example index\n"

# share it with the world
tb.shared += 'public'

# let's print our url
print(tb.url) # https://novem.no/p/NJy4w

tb.type = 'mtable'

with open(__file__,'r') as f:
  ctnt = f.read().replace('````','```') # turtles

  desc = f"""
# Novem Example Index top and bottom performers


This table is an example of how you can highlight top and bottom performers 
for a fictive equity index or portfolio. The code with comments is available below.

Curious about the data side? [Check out how we created the sample data.](https://novem.no/blog/creating-the-novem-example-index/)

Want to learn more about novem and pandas? [We have an article for that.](https://novem.no/blog/novem-pandas/)


````
{ctnt}
````

"""

  tb.description = desc
