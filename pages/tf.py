import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot




def build_tf_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Test Facilities')
    st.write("""
        ### Introduction
        In order to study lesser known sections of the performance modeling chain, EDFR set up two 
        test facilities, one in the desert southwest and one in a snowy location in the northeast.  
        I was tasked with data retrieval, cleaning and studies at both test sites.
        
        ### Methodology
        Studies completed at both test sites include:
        * Decomposition model performance
        * Diffuse sensor performance
        * Satellite irradiance components performance
        * Clearsky model performance
        * Bifacial gain under desert and snowy conditions
        * Soiling models
        * Snow depth sensor studies
        * Snow soiling studies
        * Sub-hourly clipping
        
        ### Results
        Knowledge gained at the test facilities informed models chosen for development assets,
        increasing confidence in both well studies areas as well as new sub-fields for EDF.
        """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Front End', 'Data Viz', 'Numerical', 'Domain', 'Storage',
            'Streamlit', 'Plotly', 'Bokeh', 'Matplotlib', 'Pandas', 'Pvlib', 'Sci-Kit', 'Dask', 'Parquet', 'SQL']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Solar Performance', 'Statistics', 'Math', 'Projects',
            'PVSyst', 'Error Metrics', 'Regression', 'Test Facilities']
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
