import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime
import streamlit as st


class SankeySoftware:
    """
    Sankey Diagram of software competencies
    """

    def __init__(self):

        # --- labels ---
        main_type = ["Software"]
        categories = ["Front End", "Data Viz", "API", "Numerical", "Domain", "ETL", "Storage", 'Ops']
        front_end = ['Streamlit', 'Jupyter', 'Dash', 'HTML']
        data_viz = ['Plotly', 'Matplotlib', 'Bokeh']
        api = ['Flask', 'FastAPI']
        numerical = ['Pandas', 'Numpy', 'Sci-Kit', 'Dask']
        domain = ['Pvlib', 'NetworkX', 'GeoPandas']
        etl = ['Prefect']
        storage = ['Parquet', 'SQL']
        ops = ['Docker', 'AWS']

        self.labels = []
        self.sources = []
        self.values = []
        label_types = [main_type, categories, front_end, data_viz, api, numerical, domain, etl, storage, ops]
        for i, label_list in enumerate(label_types):

            # add to labels list
            self.labels.extend(label_list)

            # choose sources for edge in sankey graph
            j = i - 1 if i >= 2 else 0
            self.sources.extend([j for x in range(0, len(label_list))])

            # choose width of pipe in each node in category
            if i == 1:
                self.values.append(0)
            elif i >= 2:
                self.values.append(len(label_list))

        # --- colors ---
        self.color_link = ['#CCCCCC' for x in self.labels]

        # --- targets ---
        # Where the edges should go
        self.targets = list(range(0, len(self.sources)))

        # --- values ---
        # pipe width for individual libraries
        self.values.extend([1 for x in range(0, len(self.targets) - len(self.values))])


class SankeyDomain:
    """
    Sankey diagram of domain competencies
    """
    def __init__(self):

        # --- labels ---
        main_type = ["Domain"]
        categories = ['Solar Performance', 'C.A.D.', 'Statistics', 'Math', 'Machine Learning', 'Projects']
        solar_performance = ['PVSyst', 'Plant Predict', 'SAM']
        cad = ['AutoCAD', 'Solidworks']
        stats = ['Error Metrics', 'Monte Carlo', 'Kolmogorov-Smirnov', 'Kernel Density Estimate']
        math = ['Graph Theory', 'Ray Tracing']
        ml = ['Regression', 'Clustering']
        projects = ['Test Facilities', 'Utility Scale Projects', 'Residential Scale Projects']

        self.labels = []
        self.sources = []
        self.values = []
        label_types = [main_type, categories, solar_performance, cad, stats, math, ml, projects]
        for i, label_list in enumerate(label_types):

            # add to labels list
            self.labels.extend(label_list)

            # choose sources for edge in sankey graph
            j = i - 1 if i >= 2 else 0
            self.sources.extend([j for x in range(0, len(label_list))])

            # choose width of pipe in each node in category
            if i == 1:
                self.values.append(0)
            elif i >= 2:
                self.values.append(len(label_list))


        # --- colors ---
        self.color_link = ['#CCCCCC' for x in self.labels]

        # --- targets ---
        # Where the edges should go
        self.targets = list(range(0, len(self.sources)))

        # --- values ---
        self.values.extend([1 for x in range(0, len(self.targets) - len(self.values))])


def make_plot(sankey_base, color_link):

    # --- data to dict, dict to sankey ---
    link = dict(source=sankey_base.sources, target=sankey_base.targets, value=sankey_base.values, color=color_link)
    node = dict(label=sankey_base.labels, pad=50, thickness=10)
    data = go.Sankey(
        link=link,
        node=node)

    # plot
    fig = go.Figure(data)
    fig.update_layout(
        margin={
            'l': 0,
            'r': 0,
            'b': 10,
            't': 10
        },
        font=dict(size=16)
    )

    return fig


# --- GANTT ---
def employment_history():

    today = datetime.today().strftime('%Y-%m-%d')

    df = pd.DataFrame([
        dict(Task="PV Design", Start='2015-07-01', Finish='2015-10-01', Resource="Sunrun"),
        dict(Task="Sr.PV Design", Start='2015-10-01', Finish='2016-03-01', Resource="Sunrun"),
        dict(Task="Supervisor PV Design", Start='2016-03-01', Finish='2016-09-01', Resource="Sunrun"),
        dict(Task="Solar Engineer", Start='2016-10-01', Finish='2020-03-01', Resource="EDFR"),
        dict(Task="Senior R&D Engineer", Start='2020-03-01', Finish='2020-12-01', Resource="EDFR"),
        dict(Task="Manager Analytics", Start='2020-12-01', Finish='2021-09-01', Resource="EDFR"),
        dict(Task="Software Engineer", Start='2021-09-01', Finish=today, Resource="Nevados")
    ])
    color_map = {
        'Sunrun': '#14a2d9',
        'EDFR': '#272f6a',
        'Nevados': '#f26543'
    }
    fig = px.timeline(
        df,
        x_start="Start", x_end="Finish", y="Resource",
        color="Resource", color_discrete_map=color_map,
        text='Task'
        )
    fig.update_traces(textposition='inside')

    fig.update_layout(
        title="Employment History",
        yaxis_title="Position"
        )

    return fig
