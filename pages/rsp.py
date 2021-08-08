import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot




def build_rsp_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Residential Solar Design @ Sunrun')
    st.write("""
        ### PV Designer Summary
        I designed residential solar projects at Sunrun, including single/three line diagrams, cable and 
        conduit sizing, voltage drop calculations, etc. During my time as a designer I routinely
        achieved over 200% of my throughput goal.
        
        ### Sr. PV Designer Summary
        As a Sr. Designer I formally trained incoming classes of designers and wrote training manuals
        to improve ramp rate.  I also created a data driven methodology to inform layoff decision making
        for upper management.
        
        ### PV Design Supervisor
        As a Supervisor I managed a team of 15 PV designers and automated KPI calculations from Salesforce
        which highly reduced supervisory staff needs.
        """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = []
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Projects',
            'Residential Scale Projects']
    pos = [sd.labels.index(x) for x in sd.labels if x in used]
    for x in pos:
        sd.color_link[x] = '#9dd498'
    sd_fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(sd_fig)

    # # --- Prefect ---
    # st.write('## Figures')
    # st.write('___')
    # st.write('#')
    # st.image(r'diagrams/ksi_r2.png', use_column_width=True)
    # st.image(r'diagrams/ksi_diffuse.png', use_column_width=True)
    # st.write('#')


    return
