import streamlit as st
from diagrams import employment_history



def build_about_page():
    """
    """
    # --- header ---
    st.write('## Employment History')

    # --- GANTT ---
    gantt = employment_history()
    st.plotly_chart(gantt, use_container_width=True)


    c1, c2 = st.columns([2, 3])
    # --- left column ---
    c1.write('## Logistics')
    c2.write('## Other Stuff')
    me1 = {
        'Pronouns': ['he', 'him', 'his'],
        'Locations': ['San Diego County, CA', 'Remote'],
        'Contact': [
            'kurtrhee@gmail',
            r'https://www.linkedin.com/in/simonkurtisrhee/',
            r'https://www.imdb.com/name/nm5560420/?ref_=fn_al_nm_7']
    }
    me2 = {
        'Surfing': [
            '10 plus years surfing shortboards, longboards, mid-lengths from San Diego to Sumatra',
            'Currently Riding:  Chemistry, 5ft 8 Inches, 28L'],
        'Rock Climbing': [
            '5 plus years bouldering (~v5), sport (~5.11) and trad (~5.8)',
            'Currently Climbing: Vital Climbing Gym'
            ],
        'Favorite Reading': [
            'Brothers Karamazov by Fyodor Dostoyevsky',
            'Stags Leap by Sharon Olds',
            'The Unbearable Lightness of Being by Milan Kundera'
            ],
        'Stunt Filmography': [
            "American Horror Stories - Multiple (2021)",
            "13 Reasons Why - Multiple (2019-2020)",
            "Sons of Anarchy - Red Rose (2014)",
            "The Hangover Part III (2013)",
            "Chuck - Chuck vs. the Cubic Z (2010)",
            "The Shield (2018)"
            ],
        'Environment': [
            '100% Electric Car',
            '90% Vegetarian',
            '80% Zero Waste'
            ]
    }
    c1.write(me1)
    c2.write(me2)
    return
