"""
Online Resume
"""

import streamlit as st

from pages.sidebar import build_sidebar
from pages.front import build_front_page
from pages.about import build_about_page
from pages.operation import build_operation_page
from pages.epe import build_epe_page
from pages.autolayout import build_autolayout_page
from pages.kde import build_kde_page
from pages.ksi import build_ksi_page
from pages.backtracking import build_raytracing_page
from pages.tf import build_tf_page
from pages.usp import build_usp_page
from pages.rsp import build_rsp_page


from diagrams import SankeySoftware, SankeyDomain, make_plot


# --- Page Configuration ---
st.set_page_config(
    page_title='Kurt Rhee Portfolio',
    page_icon=':test_tube:',
    layout='wide',
    initial_sidebar_state='expanded')

# --- MAIN ---
def main():

    # --- sidebar ---
    navigation = build_sidebar()

    # --- build pages
    if navigation['page'] == 'Index':
        build_front_page()
    elif navigation['page'] == 'About Me':
        build_about_page()
    elif navigation['page'] == 'Operational Data ETL':
        build_operation_page()
    elif navigation['page'] == 'Energy Production Estimation':
        build_epe_page()
    elif navigation['page'] == 'Solar Layout Generator':
        build_autolayout_page()
    elif navigation['page'] == 'Non-Gaussian Uncertainty':
        build_kde_page()
    elif navigation['page'] == 'Non-Linear Satellite Correlation':
        build_ksi_page()
    elif navigation['page'] == 'Ray Tracing':
        build_raytracing_page()
    elif navigation['page'] == 'Test Facilities':
        build_tf_page()
    elif navigation['page'] == 'Utility Scale Projects':
        build_usp_page()
    elif navigation['page'] == 'Residential Scale Projects':
        build_rsp_page()
    else:
        build_front_page()



if __name__ == "__main__":
    main()




