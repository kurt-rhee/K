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
        ### Introduction
        The Solar Engineering Group at EDFR and at many other companies faces a large constraint which forces them to use PVSyst in their energy production estimate reports. This is due to the fact that large financing bodies have a longstanding familiarity with PVSyst and often do not want to use reports from other vendors. Legacy tools at the company to pre and post-process data into and out of PVsyst were all created in separate excel tools. In order to complete a full energy estimate, solar engineers needed to open up at least 3 different instances of excel and switch back and forth between them to gather the correct information.
        
        ### Methodology
        Streamlining this process meant combining many excel tools into just one, to serve as a front end for python code which runs on a remote server, introducing batch processing functionalities and the ability to create deliverable files for the newly formed storage team. These new deliverables not created in the original tool include energy for storage optimization at the battery terminals and energy shifting results.
        
        The tool begins with an excel based interface which simplifies the design of a grid scale PV plant. This design is then carried over to an interstitial page which allows the user to automatically create batch files for PVSyst, or test buildable land areas to see if they fit the desired design. Once these intermediate calculations are done, the user runs PVsyst and clicks "Run EPE" on the excel interface.
        
        Once the "Run EPE" button is clicked, a python script on a remote server post-processes all of the PVSyst losses, adding a few calculations and combines all of the resulting data into a deliverable template ready to be consumed by the end user.
        
        ### Results
        The end result of all of this automation is approximately 25 minutes per use of the tool. With the team at its current size, the tool gives the following financial benefits:
        
        * 639.45% ROI
        * $433,817 NPV with a 5% discount rate over 5 years
        * $103,956 Yearly Saved Cost
        
        These benefits are expected to grow as more people are added to the solar and storage engineering teams and more possible solar projects are examined.
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
