import requests
from collections import defaultdict
import pandas as pd
import plotly.graph_objs as go


def load_api_data():
    '''
    Load data on fertility rates (births per woman) from https://data.worldbank.org/
    for the following countries: de;at;ch;nl;es;it;gb;fr;pt;be;swe;fi;nor
    for the following year: 1990:2020
    :return: data (dict)
    '''
    payload = {'format': 'json', 'per_page': '500', 'date': '1990:2021'}
    r = requests.get(
        'http://api.worldbank.org/v2/countries/de;at;ch;nl;es;it;gb;fr;pt;be;swe;fi;nor/indicators/SP.DYN.TFRT.IN',
        params=payload)

    # Clean the data and put it in a dictionary
    data = defaultdict(list)

    for entry in r.json()[1]:
        # Check if country is already in dictionary. If so, append the new x and y values to the lists
        if data[entry['country']['value']]:
            data[entry['country']['value']][0].append(int(entry['date']))
            data[entry['country']['value']][1].append(entry['value'])
        else:  # If country not in dictionary, then initialize the lists that will hold the x and y values
            data[entry['country']['value']] = [[], []]
    return data


def cleandata(filtercountries=None, filteryears=None):
    '''
    Clean data for visualization dashboard.
    :param filtercountries: Filter final dataset on countries
    :param filteryears: Filter final dataset on years
    :return: df (dataframe) - Fertility rates for specific years and countries
    '''
    # Load data from API and prepare plotly visualizations.
    data = load_api_data()

    # Transform dict data to dataframe by appending yearly fertility rates of all countries
    df = pd.DataFrame(columns=['year', 'fertility_rate', 'country'])
    for country in data:
        data_tuples = list(zip(data[country][0], data[country][1]))
        df_single = pd.DataFrame(data_tuples, columns=['year', 'fertility_rate'])
        df_single['country'] = [country] * 31
        df = df.append(df_single)

    # Filter on countries
    if filtercountries is None:
        filtercountries = df['country'].unique().tolist()
    df = df[df['country'].isin(filtercountries)]

    # Filter on years
    if filteryears is None:
        filteryears = df['year'].unique().tolist()
    # Filter on years must always smaller than 2019
    df = df[(df['year'].isin(filteryears)) & (df['year'] < 2019)]

    return df


def return_figures():
    '''
    Create four plotly visualizations.
    :return: figures
    '''

    # First chart plots fertility rate from 1990 to 2018 in Germany
    # As a line chart
    graph_one = []
    df = cleandata(filtercountries=['Germany'])
    df = df.sort_values('year')

    graph_one.append(
        go.Scatter(
            x=df['year'].to_list(),
            y=df['fertility_rate'].to_list(),
            mode='lines'
        )
    )

    layout_one = dict(title='Fertility Rate in Germany (1990-2018)',
                      xaxis=dict(title='Year'),
                      yaxis=dict(title='Fertility Rate'),
                      )

    # Second chart plots fertility rate from 1990 to 2018 in several european countries
    # As a line chart
    graph_two = []
    df = cleandata()
    df = df.sort_values('year')
    countrylist = df['country'].unique().tolist()

    for country in countrylist:
        graph_two.append(
            go.Scatter(
                x=df[df['country'] == country]['year'].tolist(),
                y=df[df['country'] == country]['fertility_rate'].tolist(),
                mode='lines',
                name=country
            )
        )

    layout_two = dict(title='Fertility Rate in Selected European Countries (1990-2018)',
                      xaxis=dict(title='Year'),
                      yaxis=dict(title='Fertility Rate'),
                      )

    # Third chart plots fertility rate for 1990 vs. 2018 in several european countries
    # As a bar chart
    graph_three = []
    df = cleandata(filteryears=[1990,2018])
    df = df.sort_values('fertility_rate', ascending=False)
    yearlist = df['year'].unique().tolist()

    for year in yearlist:
        graph_three.append(
            go.Bar(
                x=df[df['year'] == year]['country'].tolist(),
                y=df[df['year'] == year]['fertility_rate'].tolist(),
                name=year
            )
        )

    layout_three = dict(title='Comparison of Fertility Rate (1990 vs. 2018)',
                      #xaxis=dict(title='Country', ),
                      yaxis=dict(title='Fertility Rate'),
                      )

    # Fourth chart plots difference in fertility rate between 1990 and 2018 for several european countries
    # As a scatter chart
    graph_four = []
    df = cleandata(filteryears=[1990, 2018])
    xvals = df[df['year'] == 1990]['country'].tolist()
    yvals = [x1 - x2 for (x1, x2) in zip(df[df['year'] == 2018]['fertility_rate'].tolist(), df[df['year'] == 1990]['fertility_rate'].tolist())]

    graph_four.append(
        go.Scatter(
            x=xvals,
            y=yvals,
            mode='markers'
        )
    )

    layout_four = dict(title='Difference in Fertility Rate (1990 vs. 2018)',
                       #xaxis=dict(title='Country'),
                       yaxis=dict(title='Fertility Rate Difference (absolute)'),
                       )

    # Append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
