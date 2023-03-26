import pandas as pd
import wikipedia as wp
html = wp.page("Wikipedia:Popular pages").html().encode("UTF-8")
try: 
    df = pd.read_html(html)[0]
except IndexError:
    df = pd.read_html(html)[0]
print(df.to_string())

# grep on the output of this script (write to some pages.txt) to get the list of pages 'grep -o '[A-Za-z-][A-Za-z-][A-Za-z -]*[A-Za-z-]' pages.txt'
# had to manually go through some entries cuz couldnt find the ideal regex but its cool