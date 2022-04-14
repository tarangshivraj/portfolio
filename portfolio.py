import streamlit as st
import about
import experience
import education
import projects
import base64

st.set_page_config (
    page_title="Tarang Shivraj Jaiswal MUJ IT 2023",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded"
)

PAGES = {
	"About Me": about,
	"Education": education,	
	"Experience": experience,
	"Projects": projects
}

# col_one, col_two, col_three = st.columns(3)
# with col_one:
# 	st.write("")
# with col_two:	
st.title("TARANG SHIVRAJ JAISWAL")
# with col_three:
# 	st.write("")
st.sidebar.title('TARANG SHIVRAJ JAISWAL')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
