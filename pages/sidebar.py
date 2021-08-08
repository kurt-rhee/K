import pandas as pd
import streamlit as st


def build_sidebar():
    """
    Parameters
    ----------
    None

    Returns
    -------
    navigation : Dictionary
        active_page
        user
        active_project

    """
    st.sidebar.write('# Kurt Rhee')
    st.sidebar.image(r'diagrams/profile.png')
    st.sidebar.header('Portfolio Navigation')

    # --- Get Active Navigation ---
    page_list = [
        'About Me', 'Index',
        'Operational Data ETL',
        'Energy Production Estimation',
        'Solar Layout Generator',
        'Non-Gaussian Uncertainty',
        'Non-Linear Satellite Correlation',
        'Test Facilities',
        'Utility Scale Projects',
        'Residential Scale Projects',
    ]

    # --- page selection ---
    page = st.sidebar.radio(
        label='Page',
        options=page_list
    )

    # --- Navigation Object --- 
    navigation = {
        'page': page,
        }

    return navigation
