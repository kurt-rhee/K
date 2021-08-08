import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot




def build_usp_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Utility Scale Solar Projects')
    st.write("""
        ### Bluemex:  90MWac in Mexico
        Challenging soiling characteristics at the site required building of a new python version of a legacy 
        VBA monte carlo soiling tool.  Running all possible permutations of cleaning scenarios through the new
        tool and a financial model allowed EDF to make informed decisions around investment in cleaning schedules.
        
        ### Desert Harvest: 150MWac in California
        ARC degradation was studied at the development soiling & meteorological station.  The project
        is partially DC coupled to a BESS system.  

        ### Maverick:  500MWac in California
        This many stage project involved many co-optimizations between PPA holders, hedge contracts and possible
        future off-take agreements.     
        """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Data Viz', 'Numerical',
            'Plotly', 'Matplotlib', 'Pandas']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Solar Performance', 'Projects',
            'PVSyst', 'Utility Scale Projects']
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
