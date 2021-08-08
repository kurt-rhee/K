import pandas as pd
import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot, employment_history


def build_front_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    # --- header ---
    # st.write('#')


    # --- Project Key ---
    c1, c2 = st.columns([10, 10])
    c1.write('## Software Engineering')
    c2.write('## Solar Performance Modeling')
    automation_key = pd.DataFrame({
        'Project': [
            'Operational Data ETl',
            'Energy Prediction Workflow'
            ],
        'Description': [
            "Remote ETL orchestration across EDF's fleet of operational solar plants",
            "Automation of resource assessment and PVSyst workflow"
            ]
    })
    automation_key.set_index('Project', inplace=True, drop=True)
    c1.write('### Automation')
    c1.table(automation_key)

    data_science_key = pd.DataFrame({
        'Project': [
            'Layout Generation',
            'Non-Gaussian Uncertainty',
            'Non-Linear Satellite Correlation'
            ],
        'Description': [
            'Automatic utility scale solar layout generation via graph theory and clustering',
            'Solar performance uncertainty via Kernel Density Estimate',
            'Ground vs. satellite correlation via Kolmogorov Smirnoff Index fit'
            ]
    })
    data_science_key.set_index('Project', inplace=True, drop=True)
    c1.write('### Data Science')
    c1.table(data_science_key)

    fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(fig)

    # --- ENGINEERING ---
    engineering_key = pd.DataFrame({
        'Project': [
            'Mojave Test Facility [<1MW]',
            'Morris Ridge Test Facility [<1MW]',
            'Utility Scale Projects',
            'Residential Scale Projects'
            ],
        'Description': [
            'Resource assessment and bifacial gain test facility in CA',
            'Snow soiling and bifacial gain test facility in NY',
            'Solar Project Development and Operational Analysis in the US/MEX/CA',
            'Solar systems design in the US'
        ]
    })

    engineering_key.set_index('Project', inplace=True, drop=True)
    c2.write('### Engineering')
    c2.table(engineering_key)

    c2.write('#')
    c2.write('#')
    c2.write('#')
    c2.write('#')
    c2.write('#')
    fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(fig)





