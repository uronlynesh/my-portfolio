import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Dark-Mode Styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Hero Welcome Style */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 5px;
        background: linear-gradient(0deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-tagline {
        font-size: 1.5rem;
        color: #a0aec0;
        margin-bottom: 40px;
    }
    /* Navigation Card Links */
    .nav-card {
        background-color: #1f293d;
        padding: 24px;
        border-radius: 12px;
        border-top: 4px solid #4facfe;
        text-align: center;
        margin-bottom: 15px;
    }
    .nav-card h3 {
        color: #ffffff;
        margin-bottom: 10px;
    }
    .nav-card p {
        color: #a0aec0;
        font-size: 0.95rem;
    }
    /* Project Cards */
    .project-card {
        background-color: #1f293d;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00f2fe;
        margin-bottom: 20px;
    }
    /* Skill Badges */
    .skill-badge {
        background-color: #2e374a;
        color: #00f2fe;
        padding: 6px 14px;
        border-radius: 20px;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
        font-weight: bold;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Handle Page State via Session State (Allows Main Page links to work seamlessly)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Main Page"

def change_page(page_name):
    st.session_state.current_page = page_name

# Navigation Menu List Options
navigation_options = ["Main Page", "Bio", "Portfolio", "Elevator Pitch"]

# Sidebar Navigation Sync
st.sidebar.title("Navigation")
sidebar_selection = st.sidebar.radio(
    "Go to:", 
    navigation_options,
    index=navigation_options.index(st.session_state.current_page)
)

# Sync sidebar clicking with session state
if sidebar_selection != st.session_state.current_page:
    st.session_state.current_page = sidebar_selection
    st.rerun()


# =========================================================================
# PAGE 1: MAIN PAGE
# =========================================================================
if st.session_state.current_page == "Main Page":
    st.markdown('<p class="hero-title">Frank Munene</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-tagline">Cyber security analyst, Freelancer</p>', unsafe_allow_html=True)
    
    st.write("Welcome to my professional hub. Select a section below or explore the sidebar to learn more about my work.")
    st.write("---")
    
    # 3-Column Navigation Grid acting as functional links
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
            <div class="nav-card">
                <h3>Bio</h3>
                <p>Discover my background, technical philosophy, and the drive behind my engineering journey.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Read My Bio →", use_container_width=True):
            change_page("Bio")
            st.rerun()
            
    with col2:
        st.markdown("""
            <div class="nav-card">
                <h3>Portfolio</h3>
                <p>Explore built applications, full-stack architectures, quantitative integrations, and live tools.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Portfolio →", use_container_width=True):
            change_page("Portfolio")
            st.rerun()
            
    with col3:
        st.markdown("""
            <div class="nav-card">
                <h3>⚡ Elevator Pitch</h3>
                <p>The core value proposition. A high-impact summary of what I bring to teams and clients.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Hear The Pitch →", use_container_width=True):
            change_page("Elevator Pitch")
            st.rerun()


# =========================================================================
# PAGE 2: BIO
# =========================================================================
elif st.session_state.current_page == "Bio":
    if st.button("← Back to Main Page", key="back_bio"):
        change_page("Main Page")
        st.rerun()
        
    st.title("About Me")
    col_bio1, col_bio2 = st.columns([2, 1], gap="large")
    
    with col_bio1:
        st.markdown("### My Journey")
        st.write(
            "I am a tech innovator focused on building fast, highly reliable, and optimized applications. "
            "My fascination with technology lies at the intersection of complex software development, scalable system architecture, "
            "and robust operational security. I look at problems from both an engineering standpoint (how to build it efficiently) "
            "and a security standpoint (how to defend it natively)."
        )
        st.write(
            "When I am not designing backends or writing clean front-end templates, I spend my time examining network "
            "topologies, experimenting with microcontroller signaling, or building data analysis utilities."
        )
        
        st.write("### Core Toolkit")
        skills = ["Python", "MERN Stack", "TypeScript", "Linux Environments", "Network Security", "API Orchestration", "Git/GitHub"]
        badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
    with col_bio2:
        st.image("https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500", 
                 caption="Translating complex ideas into production-ready logic.", use_container_width=True)


# =========================================================================
# PAGE 3: PORTFOLIO
# =========================================================================
elif st.session_state.current_page == "Portfolio":
    if st.button("← Back to Main Page", key="back_port"):
        change_page("Main Page")
        st.rerun()
        
    st.title("Project Showcase")
    st.write("A curated selection of technical applications built from the ground up:")
    st.write("---")
    
    # Project 1
    st.markdown("""
        <div class="project-card">
            <h3>📈 IntelliTrade Engine</h3>
            <p><strong>Tech Stack:</strong> Python, Pandas, Technical Indicators (EMA/ATR), Broker API Execution</p>
            <p>An automated quantitative analysis engine designed for real-time market scanning, tracking asset volatility, and handling rule-based algorithmic order execution with strictly automated risk mitigations.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
        <div class="project-card">
            <h3>💊 MediDrop Platform</h3>
            <p><strong>Tech Stack:</strong> MERN Stack (MongoDB, Express, React, Node.js), Safaricom Daraja API</p>
            <p>A full-stack online marketplace supporting safe medicine sales, utilizing integrated mobile payment endpoints for automated ledger reconciliations, real-time data lookups, and mobile-responsive order pipelines.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
        <div class="project-card">
            <h3>🔒 Vulcan - Audit Scanner</h3>
            <p><strong>Tech Stack:</strong> Python, Nmap Core Engine, Linux Script Automation</p>
            <p>An automated internal vulnerability auditing system designed to crawl local system ports, flag out-of-date assets, and cross-reference records against public CVE databases for fast risk reporting.</p>
        </div>
    """, unsafe_allow_html=True)


# =========================================================================
# PAGE 4: ELEVATOR PITCH & CONTACT
# =========================================================================
elif st.session_state.current_page == "Elevator Pitch":
    if st.button("← Back to Main Page", key="back_pitch"):
        change_page("Main Page")
        st.rerun()
        
    st.title("The Pitch")
    
    # Large format quote callout for high-impact readability
    st.markdown("""
    > **"I don't just build applications that scale; I design environments built to survive."**
    > 
    > In modern infrastructure, speed means nothing if a system is brittle or exposed. I bring a highly versatile combination 
    > of full-stack MERN expertise, advanced Python scripting, and practical security assessments to teams. Whether it's connecting secure 
    > e-commerce systems via production APIs, engineering automated high-speed data processors, or running vulnerability pipelines, 
    > I eliminate technical gaps. I turn complex logic into clean, functional code, and abstract architectures into reliable businesses.
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("---")
    
    # Interactive Contact Form directly underneath the Pitch
    st.subheader("Let's Collaborate")
    st.write("Ready to scale up your systems? Drop a secure message directly into my inbox:")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message Detail")
        submit = st.form_submit_button("Send Encryption-Routed Message")
        
        if submit:
            if name and email and message:
                FORMSPREE_ID = "mvzyodyd" 
                url = f"https://formspree.io/f/{FORMSPREE_ID}"
                payload = {"name": name, "email": email, "message": message}
                
                try:
                    with st.spinner("Processing network handshake..."):
                        res = requests.post(url, data=payload)
                    if res.status_code == 200:
                        st.success(f"Success! Thank you, {name}. Your transmission was pushed safely to my personal inbox.")
                    else:
                        st.error("Server handshake rejected. Verify API configuration parameters.")
                except Exception:
                    st.error("Network Exception. Unable to interface with outbound API framework gateways.")
            else:
                st.error("Validation Error: Please fill out all input fields prior to executing submission.")
