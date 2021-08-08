import streamlit as st
from diagrams import employment_history



def build_about_page():
    """
    """
    # --- about ---
    st.write('## About Me')
    st.write("""
    Hello, my name is Kurt Rhee and I am a software developer and solar performance engineer, interested
    in the intersection between the two disciplines.  My educational background is in NanoEngineering, but I 
    taught myself how to program in Python in 2014 and I haven't stopped programming since.  
    
    Sankey diagrams located on each page throughout this portfolio display core competencies and libraries that I
    have actively used to create some body of work.  On each project page, the edges highlighted in green show which
    competencies I used on that specific project. If you are viewing this page on a small laptop screen, all of the
    parts of the sankey diagrams may not appear.  Please feel free to resize the browser or expand the diagrams to full
    size via the expand button located at the top right of each diagram
    
    Outside of my main body of work, I am a part time stunt man, surfer, rock climber, environmentalist and bibliophile.
    
    Nice to meet you, and please feel free to contact me directly regarding any of the projects you may
    want to talk about in greater detail.
    """)

    # --- GANTT ---
    st.write('## Employment History')
    gantt = employment_history()
    st.plotly_chart(gantt, use_container_width=True)

    # --- columns ---
    c1, c2 = st.columns([2, 3])

    # --- left column ---
    c1.write('## Logistics')
    c2.write('## Other Stuff')
    me1 = {
        'Pronouns': ['he', 'him', 'his'],
        'Locations': ['San Diego County, CA', 'Remote'],
        'Education': ['B.Sc. NanoEngineering from UCSD', 'Minor in Literature from UCSD'],
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
