import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot




def build_operation_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Operational Data ETL & Dashboard')
    st.write("""
    ### Introduction
    Before the analytics group was established 1/1/2021 there was no established feedback loop from
    EDF owned and operated solar and storage plants to the models used to develop them.  The purpose
    of the new group was to use the large streams of data coming from the EDF fleet to inform the 
    modeling of new development assets. 
    
    ### Methodology
    In order to create a feedback loop from operating power plant data to the performance models used to
    estimate their profitability, I first created a python library entitled "botany," meaning the study 
    of [power] plants in order to standardize data reading, timezone localization, data cleaning and ingestion.
    I then created a set of ETL operations organized as directed acyclic graphs within botany
    and orchestrated by Prefect on a remote server to automatically and reproducibly transform data into usable KPI's.  
    
    
    ### Result
    The feedback loop operates across EDF's fleet of utility scale solar power plants and removes the need
    to import, clean and track operational data against the original budget.  This saves time, 
    generates consistency and greatly reduces the likelihood of errors in analysis.
    """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Front End', 'Data Viz', 'Numerical', 'Domain', 'Orchestration', 'Storage', 'Version Control',
            'Streamlit', 'Plotly', 'Pvlib', 'Pandas', 'Prefect', 'Parquet', 'Github']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Solar Performance', 'Statistics', 'Math', 'Projects',
            'Error Metrics', 'Graph Theory', 'Utility Scale Projects']
    pos = [sd.labels.index(x) for x in sd.labels if x in used]
    for x in pos:
        sd.color_link[x] = '#9dd498'
    sd_fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(sd_fig)

    # --- Prefect ---
    st.write('## Figures')
    st.write('___')
    st.write('#')
    st.image(r'diagrams/prefect.png')
    st.write('#')


    return
