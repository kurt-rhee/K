import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot


def build_raytracing_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Terrain Aware Backtracking vis Forward Ray Tracing')
    st.write("""
    ### Description
    Nevados's unique terrain tolerant horizontal single axis tracking technology required a robust backtracking
    algorithm to avoid shading.  Available cross-axis backtracking algorithms did not account for the possibility
    of intra axis tilts, therefore requiring an entirely new algorithm.  Forward ray tracing was chosen and algorithm
    implemented and automated in the cloud using AWS ECS and AWS ECR.
    
    
    ### Result
    Novel forward ray tracing based backtracking algorithm scalable to any amount of projects and any size project for
    Nevados in the cloud.
    """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Front End', 'Data Viz', 'API', 'Numerical', 'Domain', 'Ops',
            'Streamlit', 'Plotly', 'FastAPI', 'Pvlib', 'Pandas', 'Numpy', 'Docker', 'AWS']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['Solar Performance', 'Math', 'Projects',
            'Ray Tracing', 'Utility Scale Projects']
    pos = [sd.labels.index(x) for x in sd.labels if x in used]
    for x in pos:
        sd.color_link[x] = '#9dd498'
    sd_fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(sd_fig)

    # --- Prefect ---
    st.write('## Figures')
    st.write('___')
    st.write('#')
    st.image(r'diagrams/trackers.gif')
    st.write('#')

    return
