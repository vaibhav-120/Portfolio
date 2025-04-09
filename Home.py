import streamlit as st

st.set_page_config(page_title="Vaibhav's Portfolio", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        height:0
    }
    .main-title {
        font-size: 50px;
        color: #2e63b8;
        font-weight: bold;
        text-align: center;
        animation: fadeInDown 2s ease-in-out;
        margin: 80px 0px 0px 0px;
    }
    .profilepic{
        border-radius: 50%
    }
    img{
        margin:15px 10px 0px 20px;
    }
    .imgwrapper {
        display: flex;
        justify-content: center;
    }
    .subtitle {
        font-size: 22px;
        color:rgb(122, 122, 122);
        text-align: center;
        margin-bottom: 40px;
        animation: fadeInDown 2.5s ease-in-out;
    }
    .name {
        font-size: 25px;
        text-align: center;
    }
    .summary {
        font-size: 18px;
        text-align: justify;
        animation: fadeInDown 2.5s ease-in-out;
    }
    .projectwrapper {
        display: flex;
        flex-wrap: wrap;
    }
    h5{
        text-align: center;
    }
    .projectcard {
        box-shadow: 0 5px 10px 0 rgba(46, 46, 46, 0.2);
        text-align: justify;
        margin: 20px;
        transition: 0.5s;
        width: 350px;
    }
    .projectcard img{
        object-fit:contain;
        margin:0;
    }
    .projectcard h5{
        margin:20px 0 0 0;
    }
    .projectcard p{
        margin: 0 20px 20px 20px;
    }
    .certificatecard {
        box-shadow: 0 5px 10px 0 rgba(46, 46, 46, 0.2);
        text-align: center;
        margin: 20px;
        padding: 20px;
        transition: 0.5s;
        width: 250px;
    }
    .footer{
        background-color: black;
    }
    a:link {
        text-decoration: none;
    }
    a:visited {
        text-decoration: none;
    }

    a:hover {
        text-decoration: none;
    }
    a:active {
        text-decoration: none;
    }
    .certificatecard:hover {
        box-shadow: 0 20px 40px 0 rgba(46, 46, 46, 0.2);
    }
    .projectcard:hover {
        box-shadow: 0 20px 40px 0 rgba(46, 46, 46, 0.2);
    }
    button{
        margin: 20px;
        border: 0;
        padding: 7px 14px;
        color: white;
        background-color: #2e63b8;
        border-radius: 40px;
    }
    .skillcard{
        height: 100px;
    }
    .skill{
        text-align: center;
        color: #444;
        margin: 0px 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, d,col2 = st.columns([1.5,1, 5])

with col1:
    st.markdown(f"""
                <img src="https://i.imgur.com/SHIUOPl.jpeg" class="profilepic"></img>
    """,unsafe_allow_html=True)
    st.markdown('<div class="name">Vaibhav Shrivastava</div>', unsafe_allow_html=True)
    st.markdown(f"""<div class="imgwrapper">
                <a href="www.linkedin.com/in/vaibhav-shrivastava120"><img src="data:image/png;base64,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", width=40px></img></a>
                <a href="https://github.com/vaibhav-120"><img src="data:image/png;base64,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", width= 37px></img></a>
                <a href="mailto:vs2409425@gmail.com?subject=Hi Vaibhav"><img src="data:image/png;base64,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", width=37px></img></a>
    </div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="imgwrapper">
                <a href="https://drive.google.com/file/d/1L2O-ibv1HQ7s9SzRusqwgsTHzMkaIDuh/view?usp=sharing"><button>Download Resume</button></a>
    </div>""", unsafe_allow_html=True)
    

with col2:
    st.markdown('<div class="main-title">Hi! I’m Vaibhav</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A passionate AI Engineer</div>', unsafe_allow_html=True)
    st.markdown('<div class="summary">I am a Computer Science student at DAV University with a GPA of 8.5+. I have worked with various tools and frameworks, including Python, TensorFlow, PyTorch, LangChain, OpenAI API, Hugging Face, and vector database like FAISS. My experience also extends to data science and analytics, enabling me to develop and optimize AI-driven solutions with a data-centric approach.', unsafe_allow_html=True)


st.markdown("---")

st.markdown('<div class="main-title">Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Implementation of my Skills and Learnings in real life</div>', unsafe_allow_html=True)
st.markdown("""<div class="projectwrapper">
            <a href="https://campus-reviewer.streamlit.app", class="projectcard">
                <img src="https://i.imgur.com/7ZjI1aS.png"></img>
                <h5>Campus Reviewer</h5>
                <p>Campus Reviewer is a python based website that helps students in choosing best fit institutions. It provides graphical representation on sentiment analysis of college reviews in terms of Infrastructure, Academics, Placements of the college. It also supports College recommendation system and JoSAA College predictor that assists students in their college searching process.</p>
            </a>
            <a href="https://dermalens.streamlit.app", class="projectcard">
                <img src="https://i.imgur.com/2t1GMNg.png"></img>
                <h5>DermaLens</h5>
                <p>DermaLens is a python based website developed using streamlit that helps in the diagnosis of skin diseases by taking image of affected area. Provides a brief description for the disease and remedies to cure it.</p>
            </a>
            <a href="https://drive.google.com/file/d/1JC3-93cKTsxZWMaCXrX22-my7uxaoQga/view?usp=sharing", class="projectcard">
                <img src="https://i.imgur.com/NJyiOdy.jpeg"></img>
                <h5>Multipage Dashboard for Maven Market</h5>
                <p>This is a multi-page interactive dashboard in Power BI that transforms raw data into actionable insights. This dashboard helps analyses of each factor like stores, customers, products that effects sales performance, revenue growth and market trends enabling data-driven decision-making. </p>
            </a>
            <a href="https://github.com/vaibhav-120/Fitness-Tracker", class="projectcard">
                <img src="https://i.imgur.com/APhtkjc.png"></img>
                <h5>Fitness Tracker</h5>
                <p>Fitness Tracker is a python based desktop application that helps users manage their fitness journey. It offers features like weight tracking, a meal generator and tracker, workout tracking with instructional exercise videos, and hydration reminders. It generates custom plan for the users according to the goal specified by them. The app provides an all-in-one solution for users to monitor their health goals and stay on track with their fitness routines.</p>
            </a>
            <a href="https://drive.google.com/file/d/1XKXRuc01eDyKhouwC_iYK6Dm1Vg1fB00/view?usp=sharing", class="projectcard">
                <img src="https://i.imgur.com/0OxIXXr.png"></img>
                <h5>Interactive Sales Dashboard in PowerBI</h5>
                <p>This Power BI dashboard was designed to provide a comprehensive and visually engaging overview of sales performance, enabling data-driven decision-making. Key features of the dashboard include: Revenue Insights, Regional Performance, Product Analysis, KPIs and Trends, Interactivity. This project demonstrates my ability to: Transform raw sales data into actionable insights, Leverage Power BI’s advanced visualization tools for storytelling, Optimize dashboards for performance and user engagement.</p>
            </a>
</div>""", unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="main-title">Skills</div>', unsafe_allow_html=True)
st.markdown("""<div class="projectwrapper">
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/gLTj173.png">
        <p>Python</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/WMb8ZJc.png">
        <p>Sci-kit Learn</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/jsbHqpp.png">
        <p>TensorFlow</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/QwcDSFq.png">
        <p>Pandas</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/QGsL4CD.png">
        <p>Numpy</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/PrPWBwX.png">
        <p>Matplotlib</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/O99cfxT.png">
        <p>Plotly</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/6uRQzUk.png">
        <p>Seaborn</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/Ur9UgBw.png">
        <p>Google Colab</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/tuVWtyl.png">
        <p>Streamlit</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/OWyJ7kC.png">
        <p>Jupyter Notebook</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/lVS2YvQ.png">
        <p>Computer Vision</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/w4RyGUO.png">
        <p>SQL, PL/SQL, Apex Oracle</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/FYu6KNu.png">
        <p>Git</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/3IAdfYi.png">
        <p>FastAPI</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/RhY0vQM.png">
        <p>C</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/Br3Extw.png">
        <p>C++</p>
    </div>
    <div class="skill">
        <img class="skillcard" src="https://i.imgur.com/dQrUf0y.png">
        <p>PowerBI</p>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("---")

st.markdown('<div class="main-title">Certifications & Achievements</div>', unsafe_allow_html=True)
st.markdown(f"""<div class="projectwrapper">
            <a href="https://courses.cognitiveclass.ai/certificates/5bed55e63db44036b2d31623bf7bfcd0", class="certificatecard">
                <h5>Python 101 for Data Science</h5>
                <p>Cognitive Class, Powered by IBM Developer Skills Network</p>
            </a>
            <a href="https://drive.google.com/file/d/1-q7i8TJJe36u8v2DY1MsWJ7SyZI48Qif/view?usp=sharing", class="certificatecard">
                <h5>Python Programming with Tkinter and SQL</h5>
                <p>O7 Services, Jalandhar</p>
            </a>
            <a href="https://drive.google.com/file/d/1U6_uJqmFltXoskDdtulwTp42PHyxBEiQ/view?usp=sharing", class="certificatecard">
                <h5>Data Science and Machine Learning</h5>
                <p>O7 Services, Jalandhar</p>
            </a>
            <a href="https://drive.google.com/file/d/1ky6cPNtyKYULzryomvmIb9P6nYXI5TWx/view?usp=sharing", class="certificatecard">
                <h5>The Brainiacs (Innovation Competition)</h5>
                <p>DAV University, Jalandhar</p>
            </a>
</div>""", unsafe_allow_html=True)