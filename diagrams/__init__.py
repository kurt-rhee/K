import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime

class SankeySoftware:
    """
    Sankey Diagram of software competencies
    """

    def __init__(self):

        # --- labels ---
        self.labels = [
            "Software",

            # Categories
            "Front End", "Data Viz", "API",
            "Numerical", "Domain", "ETL", "Storage", 'Ops',

            'Streamlit', 'Jupyter', 'Dash', 'HTML',     # Front End
            'Plotly', 'Matplotlib', 'Bokeh',            # Data Viz
            'Flask', 'FastAPI',                         # API
            'Pandas', 'Numpy', 'Sci-Kit', 'Dask',       # Numerical
            'Pvlib', 'NetworkX', 'GeoPandas',           # Domain
            'Prefect',                                  # ETL
            'Parquet', 'SQL',                           # Storage
            'Docker', 'AWS ECR', 'AWS ECS'              # Operations
        ]

        # --- colors ---
        self.color_link = ['#CCCCCC' for x in self.labels]

        # --- sources ---
        # Where the edges should start
        self.sources = [
            0,
            0, 0, 0, 0, 0, 0, 0, 0,                     # Categories
            1, 1, 1, 1,                                 # Front End
            2, 2, 2,                                    # Data Viz
            3, 3,                                       # API
            4, 4, 4, 4,                                 # Numerical
            5, 5, 5,                                    # Domain
            6,                                          # ETL
            7, 7,                                       # Storage
            8, 8, 8                                     # Operations
        ]

        # --- targets ---
        # Where the edges should go
        self.targets = list(range(0, len(self.sources)))

        # --- values ---
        # Width of the pipes to each node
        self.values = [
            0,  # Categories
            4,  # Front End
            3,  # Data Viz
            1,  # API
            4,  # Numerical
            3,  # Domain
            1,  # ETL
            2,  # Storage
            3,  # Operations
        ]
        self.values.extend([1 for x in range(0, len(self.targets) - len(self.values))])


class SankeyDomain:
    """
    Sankey diagram of domain competencies
    """
    def __init__(self):
        # --- labels ---
        self.labels = [
            "Domain",

            # Categories
            'Solar Performance', 'C.A.D.', 'Statistics', 'Math',
            'Machine Learning', 'Projects',

            'PVSyst', 'Plant Predict', 'SAM',                                               # Solar Performance Modeling
            'AutoCAD', 'Solidworks',                                                                # CAD
            'Error Metrics', 'Monte Carlo', 'Kolmogorov-Smirnov', 'Kernel Density Estimates',       # Stats
            'Graph Theory', 'Ray Tracing',                                                          # Math
            'Regression', 'K-Means Clustering', 'Spectral Clustering', 'Hierarchical Clustering',   # ML
            'Test Facilities', 'Utility Scale Projects', 'Residential Scale Projects'               # Projects
        ]

        # --- colors ---
        self.color_link = ['#CCCCCC' for x in self.labels]

        # --- sources ---
        # Where the edges should start
        self.sources = [
            0,
            0, 0, 0, 0, 0, 0,   # Categories
            1, 1, 1,            # Solar Performance Modeling
            2, 2,               # CAD
            3, 3, 3, 3,         # Stats
            4, 4,               # Math
            5, 5, 5, 5,         # ML
            6, 6, 6             # Projects
        ]

        # --- targets ---
        # Where the edges should go
        self.targets = list(range(0, len(self.sources)))

        # --- values ---
        # Width of the pipes to each node
        self.values = [
            0,
            3,  # Solar Performance Modeling
            2,  # CAD
            4,  # Stats
            1,  # Math
            4,  # ML
            3   # Projects
        ]
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
