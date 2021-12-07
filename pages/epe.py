import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot


def build_epe_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Energy Production Estimate Workflow')
    st.write("""
        ### Description
        Automation of EDF's PVSyst workflow
        
        ### Results
        
        * 639.45% ROI
        * $433,817 NPV with a 5% discount rate over 5 years
        * $103,956 Yearly Saved Cost
            """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Front End', 'Data Viz', 'Numerical', 'Domain', 'Storage', 'Version Control',
            'Streamlit', 'Plotly', 'Bokeh', 'Pvlib', 'Pandas', 'SQL']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Solar Performance', 'Statistics', 'Math', 'Projects',
            'PVSyst', 'Utility Scale Projects']
    pos = [sd.labels.index(x) for x in sd.labels if x in used]
    for x in pos:
        sd.color_link[x] = '#9dd498'
    sd_fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(sd_fig)

    # --- Prefect ---
    st.write('## Figures')
    st.write('___')
    st.write('#')
    st.image(r'diagrams/epe.png')
    st.write('#')


    return
