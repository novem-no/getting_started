from novem import Mail, Plot
from novem.mail import PreviewSection as PV, ParagraphSection as P, VisSection as V
  
mail = Mail('nei_rgn_summary')

mail.add_section(PV(
  "DTD: 4.5% | WTD: 4.0% | MTD: 4.4% | YTD: -15.7%"
))

mail.add_section(P("""Hello Jane,


Today the Novem Example Index is up by 4.5% driven by strong 
performance across the board, particularly in techology stocks (**AAPL** +9%,
**TSM** +9%, **ASML** +14%) and their consumer proxies (**AMZN** +12%, 
**BABA** +7.5%, **TSLA** +7%).


On the negative side, Brazil it's continuing it's fall and is down over 6%
on the day detracting 20bps from the overall index performance.


Overall the 4th quarter feels better with November continuing the trend of 
clawing back some of the underperformance so far in 2022.
"""
))


# Add our performance chart
mail.add_section(V(Plot('nei_rgn_perf'), margin='t4', include_link=True))

# Add our regional breakdown le
mail.add_section(V(Plot('nei_rgn_hier'), margin='t4', include_link=True))

# Add our top and bottom performers le
mail.add_section(V(Plot('nei_rgn_tb'), margin='t4', include_link=True))

disclaimer = """
The Novem Example Index (NEI) is an attempt by novem at creating a realistically
looking dataset for our visualisation offering. It's not trying to be an
accurate representation of a fund or an index. The calculations are inaccurate
and does not attempt to preserve history across runs or address errors in a
consistent way. Neither trade volume nor liquidity are considered.


Please do not use the information or example code beyond its intended scope.


Index Construction: The novem example index constituents are defined as the 500
largest companies from the Nasdaq stock screener. The YTD returns are
calculated from Yahoo finance price history and the returns weighted by historic
price adjusted market cap.
"""

# add a psuedo header
mail.add_section(P(
  'Disclaimer',
  font_size='m',
  font_style='b',
  margin='t4',
  fg='gray-600',
  border= 'b1 gray-600'
))


mail.add_section(P(
  disclaimer, 
  font_size='s',
  font_style='i',
  fg='gray-600'
))

# render the e-mail to the server
mail.render()

# set our recipients
mail.to = "me"

# and our subject
mail.subject = "Daily Performance Summary for the 10th of November 2022"

mail.name = "Novem Example Index - Daily Performance Summary"

mail.summary = "A daily performance demo mail for the Novem Example Index"

# share the mail with the public
mail.shared = 'public'

print(mail.url)

#mail.test()
#mail.send()

with open(__file__,'r') as f:
  ctnt = f.read().replace('````','```') # turtles

  desc = f"""
# A daily performance summary example


````
{ctnt}
````

"""

  mail.description = desc
