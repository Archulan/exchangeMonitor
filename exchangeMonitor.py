import requests
import json
from bs4 import BeautifulSoup
from h2o_wave import main, app, Q, ui, data

def scrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# HNB
HNB_data = scrape('https://www.hnb.net/exchange-rates')
HNB_results = HNB_data.findAll('td', {'class': 'exrateText'})
HNB = float(HNB_results[6].text)
print("HNB", HNB)

HNB_rate = round(HNB,1)

# Sampath
Sampath_data = scrape('https://www.sampath.lk/en/exchange-rates')
Sampath_results = Sampath_data.findAll('td')
Sampath = float(Sampath_results[57].text)
print("Sampath", Sampath)

Sampath_rate = round(Sampath,1)


# BOC
try:
    BOC_data = scrape('https://www.boc.web.lk/ExRates')
    BOC_results = BOC_data.findAll('font')
    BOC = float(BOC_results[90].text)
    print("BOC",BOC)
    BOC_rate = round(BOC,1)
except:
    BOC_rate = 260
    print("BOC server down")

# PB
try:
    PB_data = scrape('https://www.peoplesbank.lk/foreign-exchange-rates')
    PB_results = PB_data.findAll('td')
    PB = float(PB_results[69].text)
    #print(PB_results[69].text)
    PB_rate = round(PB,1)
    print("PB", PB)
except:
    PB_rate = 260
    print("PB server down")

# COM
COM_data = scrape('https://www.combank.lk/rates-tariff#exchange-rates')
COM_results = COM_data.findAll('td')
COM = float(COM_results[130].text)
print("COM",COM)
COM_rate = round(COM,1)

# Vega lite spec for a bar plot, defaults to linear scale.
spec_linear_scale = json.dumps(dict(
    mark='bar',
    encoding=dict(
        x=dict(field='Bank', type='ordinal'),
        y=dict(field='LKR value', type='quantitative')
    )
))

# Vega lite spec for a bar plot, log scaled.
spec_log_scale = json.dumps(dict(
    mark='bar',
    encoding=dict(
        x=dict(field='Bank', type='ordinal'),
        y=dict(field='LKR value', type='quantitative', scale=dict(type='log'))
    )
))

# Data for our plot.
plot_data = data(fields=["Bank", "LKR value"], rows=[
    ["Hatton National Bank", HNB_rate], ["Sampath Bank", Sampath_rate], ["Bank of Ceylon", BOC_rate],
    ["Commercial Bank", COM_rate], ["Peoples Bank", PB_rate]
])

linear_scale_command = ui.command(
    name='to_linear_scale',
    label='Linear Scale',
    icon='LineChart',
)

@app('/demo')
async def serve(q: Q):
    graph(q)
    await q.page.save()

def graph(q: Q):
    q.page['example'] = ui.vega_card(
            box='1 1 6 6',
            title='LKR Vs GBP',
            specification=spec_linear_scale,
            data=plot_data,
            commands=[linear_scale_command]
        )