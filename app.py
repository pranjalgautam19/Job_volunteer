import streamlit as st

st.set_page_config(page_title="Job Volunteer | Elite Python Job Board", layout="wide", page_icon="🚀")

# Custom CSS styling for premium look and feel
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .job-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #3776AB;
    }
    .salary-tag {
        background-color: #e1f5fe;
        color: #0288d1;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Top Premium Navigation Header
st.title("🚀 Job Volunteer")
st.caption("The Premium Career Network for Python, Django, and Data Science Professionals")

# Metric counters for site authority
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Active Openings", "142 Jobs", "+12 Today")
col_m2.metric("Average Salary", "₹14.6 LPA", "Top Tier")
col_m3.metric("Verified Employers", "48 Companies", "100% Vetted")
st.divider()

# Sidebar Search & Custom Filters
st.sidebar.header("🎯 Filter Options")
search_query = st.sidebar.text_input("Search Title or Company", placeholder="e.g., Django, AI")
experience_level = st.sidebar.selectbox("Experience Level", ["All Levels", "Junior (0-2 yrs)", "Mid-Level (2-5 yrs)", "Senior (5+ yrs)"])
job_type = st.sidebar.radio("Work Setup", ["All", "Remote Only", "Hybrid / Office"])

# Local High-Fidelity Enterprise Data Engine
jobs = [
    {"title": "Senior Django Framework Architect", "company": "TechSol Labs", "loc": "Remote (Delhi/NCR)", "sal": "₹18,00,000 - ₹24,00,000", "tags": "Django, Postgres", "link": "https://example.com"},
    {"title": "AI Platform & LLM Backend Specialist", "company": "NeuralFlow AI", "loc": "Bangalore (Hybrid)", "sal": "₹22,00,000 - ₹30,00,000", "tags": "FastAPI, PyTorch", "link": "https://example.com"},
    {"title": "Junior Data Engineer (SQL & Automation)", "company": "DataMetrics Inc", "loc": "Mumbai (Office)", "sal": "₹8,00,000 - ₹12,00,000", "tags": "Pandas, PostgreSQL", "link": "https://example.com"},
]

# Filtering Logic Engine
filtered_jobs = [j for j in jobs if search_query.lower() in j['title'].lower() or search_query.lower() in j['company'].lower()]

# Render High-Fidelity UI Layout
if not filtered_jobs:
    st.info("No matching premium job openings found.")
else:
    for job in filtered_jobs:
        st.markdown(f"""
            <div class="job-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="margin:0; color:#1e293b;">{job['title']}</h3>
                        <p style="margin:4px 0; color:#64748b; font-weight:600;">🏢 {job['company']} &nbsp;&nbsp; 📍 {job['loc']}</p>
                        <span class="salary-tag">💰 {job['sal']}</span>
                        <p style="margin-top:10px; font-size:14px; color:#475569;">🔑 <b>Skills:</b> {job['tags']}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("View Details & Apply ↗", job['link'], use_container_width=True)
        st.write("")
