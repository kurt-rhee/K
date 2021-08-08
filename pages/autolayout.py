import streamlit as st
from diagrams import SankeySoftware, SankeyDomain, make_plot




def build_autolayout_page():
    """
    """
    # --- config ---
    ss = SankeySoftware()
    sd = SankeyDomain()

    st.write('## Solar Layout Generation via Graph Theory and Clustering Algorithms')
    st.write("""
        ### Introduction
        Before the advent of the tool mentioned in this paper, exploring land scenarios and site designs was a manual
        process involving a project developer responsible for possible project boundaries and parcels,
        a GIS analyst responsible for removing unsuitable/un-buildable land sections from within the project boundary,
        and a Solar Engineer responsible for creating a design, implementing it in AutoCAD,
        and creating an energy assessment in PVSyst. Due to the time-cost associated with implementing a design in
        AutoCAD, often times, only one layout would be generated for each land scenario and possible alternative layouts
        that might fit in the same land scenario would be determined by ratio of ac/dc ratio, ground coverage ratio
        and module efficiency.
        
        Solving the generalized problem of fitting objects inside of a given boundary,
        optimizing for maximum number of objects has been studied in the fields of computational geometry
        and operations research for decades [1] and is considered NP-hard. The generalized problem specified to the
        solar engineering application is the fitting of racks inside of a buildable land polygon. This problem can be
        broken down into a a set of P complexity steps that approximate the global maximum while also taking into
        account factors that affect the design such as cable length, continuitiy of DC blocks, etc.
                
        ### Methodology
        * PreProcessing:  As a given project boundary can contain many discontiguous parcels and buildable areas,
        it is necessary to divide each of these polygons into their own separate optimization problems.
        Removing polygons which do not contain enough area to fit an entire DC block from consideration helps to speed
        up the process.
                
        * Fill Areas with Possible Tracker Objects
        Use all possible space (R2) to place trackers. N different starting positions are attempted, with
        only the iteration which results in the largest capacity chosen.
        
        * Remove Disconnected Tracker Objects
        Use graph theory techniques to remove disconnected tracker objects and tracker objects which cause the 
        capacity of the plant to go above the specified limit
         
        * Use Clustering Algorithm to Find Possible Blocks
        Implement a spectral clustering algorithm with number of clusters (k) equal to the possible
        number of blocks on each distinct contiguous area of possible tracker positions. Graph partitioning
        methods on their will not give equalized clusters.
        
        * Equalize Clustering Algorithm Output
        Create an adjacency matrix for all the clusters. The adjacency matrix should contain information not only
        of which clusters are contiguous with other clusters, but also the size of each cluster. Then
        implement local differences algorithm or adjacency pathway algorithm.
                
        ### Results
        A complete autolayout program as implemented by EDFR runs in approximately 4 minutes,
        compared to an engineer at approximately 30 minutues.
        This includes extra information, and more optimization attempts than the engineer.
        On top of this the program can be made more powerful by parallelization to increase throughput.
        This allows for applications such as iteration through a large matrix of possible plant designs,
        feeding the resulting capex, opex and generation profiles into a financial model and selecting the
        best performing plant. The tool decreases EDFR plant LCOE, increases competitiveness in bids and
        allows us to build better more profitable solar projects.    
        """)

    # --- header ---
    c1, c2 = st.columns([1, 1])

    # --- left column ---
    c1.write('## Software Engineering')
    used = ['Front End', 'Data Viz', 'Numerical', 'Domain', 'Storage', 'Version Control',
            'Streamlit', 'Plotly', 'Pandas', 'Numpy', 'Sci-Kit', 'NetworkX', 'GeoPandas', 'SQL', 'Github']
    pos = [ss.labels.index(x) for x in ss.labels if x in used]
    for x in pos:
        ss.color_link[x] = '#9dd498'
    ss_fig = make_plot(ss, ss.color_link)
    c1.plotly_chart(ss_fig)

    c2.write('## Solar Performance Modeling')
    used = ['C.A.D', 'Math', 'Projects',
            'AutoCAD', 'Graph Theory', 'Utility Scale Projects']
    pos = [sd.labels.index(x) for x in sd.labels if x in used]
    for x in pos:
        sd.color_link[x] = '#9dd498'
    sd_fig = make_plot(sd, sd.color_link)
    c2.plotly_chart(sd_fig)

    # --- Prefect ---
    st.write('## Figures')
    st.write('___')
    st.write('#')
    st.image(r'diagrams/autolayout.png', use_column_width=True)
    st.write('#')


    return
