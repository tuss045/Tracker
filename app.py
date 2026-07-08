import streamlit as st
import pandas as pd
from datetime import date

# Page configuration
st.set_page_config(page_title="Work Tracker", page_icon="🚀", layout="wide")

st.title("_______'s Automation Tracker 🚀")
st.write("A live record of my scripts, automations, and projects.")

# Default data pre-loaded with your recent work
default_projects = [
    {
        "Date": date.today().strftime("%Y-%m-%d"),
        "Project Name": "Social Media Dashboard Scraper",
        "Description": "Automated capturing screenshots of YouTube and Instagram dashboards.",
        "Tech Stack": "Python, Selenium WebDriver, Google OAuth"
    },
    {
        "Date": date.today().strftime("%Y-%m-%d"),
        "Project Name": "WhatsApp to Google Drive Pipeline",
        "Description": "Automated the transfer of screenshots from WhatsApp groups to specific Google Drive folders, automatically using image captions as filenames.",
        "Tech Stack": "Python, Google Drive API"
    }
]

# Initialize session state for the dataframe
if "project_data" not in st.session_state:
    st.session_state.project_data = pd.DataFrame(default_projects)

# Input Form
with st.sidebar:
    st.header("Log New Work")
    with st.form("new_project_form"):
        project_name = st.text_input("Project Name")
        tech_stack = st.text_input("Tools Used")
        date_completed = st.date_input("Date Completed", date.today())
        description = st.text_area("What does it do?")
        submitted = st.form_submit_button("Save Project")

        if submitted and project_name:
            new_entry = pd.DataFrame([{
                "Date": date_completed.strftime("%Y-%m-%d"), 
                "Project Name": project_name, 
                "Description": description, 
                "Tech Stack": tech_stack
            }])
            st.session_state.project_data = pd.concat([st.session_state.project_data, new_entry], ignore_index=True)
            st.success(f"Logged '{project_name}'!")

# Display Records
st.subheader("📚 Work Archive")
st.dataframe(st.session_state.project_data, use_container_width=True, hide_index=True)

st.markdown("---")
st.info("💡 **Deployment Note:** On Streamlit Community Cloud, new entries added via the sidebar will reset if the app goes to sleep. To permanently add a new project to your live site, simply add it to the `default_projects` list in your GitHub code!")
