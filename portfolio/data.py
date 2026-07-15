"""
==============================================================================
 ALL YOUR PORTFOLIO CONTENT LIVES IN THIS ONE FILE.
 You should never need to touch an HTML template just to update your info —
 edit the values below and the site updates everywhere it's used.
==============================================================================
"""

PORTFOLIO = {

    # -------------------------------------------------------------------
    # BASIC INFO — shown in the nav, hero, and browser tab
    # -------------------------------------------------------------------
    "name": "NITHEESH GOWDA G S",
    "site_title": "NITHEESH GOWDA G S — Software Engineer Portfolio",
    "location": "BENGALURU, INDIA",
    "available": True,  # shows/hides the green "Available for opportunities" pill

    # Rotating titles typed out under your name in the hero
    "role_titles": [
        "Software Engineer",
        "Python Full-Stack Developer",
        "AI Engineer",
        "Problem Solver",
    ],

    "summary": (
    "Motivated Artificial Intelligence and Data Science graduate with a strong "
    "foundation in Python, SQL, Machine Learning, and Full-Stack Web Development. "
    "Experienced in building AI-powered applications using Django, React, SQLite, "
    "and XGBoost. Passionate about developing scalable, data-driven solutions and "
    "continuously learning emerging technologies."
),

    # -------------------------------------------------------------------
    # CONTACT — reused in the hero, contact section, and footer
    # -------------------------------------------------------------------
    "email": "nitheeshsiddegowda543@gmail.com",
    "phone": "+917204546369",          # digits only, used for the tel: link
    "phone_display": "+91-7204546369", # however you want it to look on screen
    "linkedin_url": "https://www.linkedin.com/in/nitheesh-gowda-g-s-9aa5a0312/",
    "linkedin_display": "linkedin.com/in/nitheesh-gowda-g-s-9aa5a0312",
    "github_url": "https://github.com/Nitheeshsiddegowda",
    "github_display": "github.com/Nitheeshsiddegowda",
    "address": "K M Doddi, Maddur, Mandya, Karnataka — 571422",

    # Put your actual resume.pdf inside the /media folder with this exact
    # name, or change this value to point wherever you'd rather host it.
    "resume_file": "resume.pdf",

    # -------------------------------------------------------------------
    # "AT A GLANCE" STATS CARD — value/suffix/decimals control the
    # count-up animation and how the number is displayed
    # -------------------------------------------------------------------
    "stats": [
        {"label": "Current CGPA",   "value": 8.59,  "decimals": 2, "suffix": " / 10"},
        {"label": "PUC Score", "value": 85.33, "decimals": 2, "suffix": "%"},
        {"label": "10th Grade",     "value": 85.83,  "decimals": 1, "suffix": "%"},
        {"label": "Projects Built", "value": 5,  "decimals": 0, "suffix": "+"},
        {"label": "Certifications", "value": 10,  "decimals": 0, "suffix": "+"},
    ],

    # -------------------------------------------------------------------
    # ABOUT — paragraphs shown top to bottom, plus skills/tools tags
    # -------------------------------------------------------------------
    "about_paragraphs": [
    "I'm a Bachelor of Engineering graduate in Artificial Intelligence "
    "and Data Science from SDM Institute of Technology, Ujire. I am "
    "passionate about building intelligent, scalable, and user-friendly "
    "software solutions that solve real-world problems through AI and "
    "modern web technologies.",

    "I have hands-on experience developing full-stack applications using "
    "Python, Django, Django REST Framework, React, SQL, and SQLite. "
    "My major project, an Energy Consumption Forecasting and Recommendation "
    "Agent, leverages XGBoost to deliver accurate energy predictions and "
    "AI-powered recommendations through an interactive web application.",

    "I am a quick learner who enjoys exploring new technologies and "
    "continuously improving my skills. With a strong foundation in "
    "Python, Machine Learning, Data Structures, and Web Development, "
    "I am eager to contribute to innovative teams and grow as a Software "
    "or AI Engineer."
    ],

    "skills": [
        "Python", "Django", "DSA", "HTML", "CSS",
        "SQL", "Artificial Intelligence", "Machine Learning", "Java Script", "React", "Power BI", "Tableau", "Python Libraries",
    ],

    "tools": [
        "VS Code", "GitHub", "Jupyter Notebook", "Excel", "Figma"
    ],

    "education": [
        {
            "years": "2022 — 2026",
            "degree": "B.E. — Artificial Intelligence and Data Science",
            "school": "SDM Institute of Technology, Ujire",
            "badge": "CGPA: 8.59",
        },
        {
            "years": "2020 — 2022",
            "degree": "Pre-University / 12th — Science (PCMB)",
            "school": "Deeksha CFL PU College, Bengaluru",
            "badge": "85.33%",
        },
        {
            "years": "2020",
            "degree": "10th (ICSE)",
            "school": "Cauvery Public School, Mandya",
            "badge": "85.83%",
        },
    ],

    # -------------------------------------------------------------------
    # EXPERIENCE — add/remove dicts to add/remove timeline entries
    # -------------------------------------------------------------------
    "experience": [
        {
            "date": "Jan 2026 — Ongoing",
            "org": "Pentagon Space Pvt. Ltd.",
            "location": "Bengaluru, Karnataka",
            "status": "Onsite · Active",
            "title": "Python Full-Stack Development Intern",
            "description": (
            "Completed hands-on training in Python Full-Stack Development, "
            "working with Python, SQL, HTML, CSS, JavaScript, and React. "
            "Built responsive web applications, strengthened problem-solving "
            "skills through real-world assignments, and gained practical "
            "experience in software development, database management, and "
            "version control using Git and GitHub."
            ),
            "tags": ["Python", "Django", "HTML", "CSS", "JavaScript", "SQL"],
        },
    ],

    # -------------------------------------------------------------------
    # PROJECTS — set "featured": True to highlight a card with the amber border
    # -------------------------------------------------------------------
    "projects": [
    {
        "num": "01",
        "category": "AI/ML · Full-Stack Web Application",
        "title": "Energy Consumption Forecasting and Recommendation Agent",
        "description": (
            "Developed a full-stack AI-powered web application that analyzes "
            "household energy consumption and predicts future electricity usage "
            "using an XGBoost model. Built with Django REST Framework, React, "
            "SQLite, JWT Authentication, and Recharts, the application provides "
            "dataset upload, data visualization, consumption forecasting, "
            "interactive dashboards, and personalized energy-saving recommendations."
        ),
        "tags": [
            "Python",
            "Django",
            "Django REST Framework",
            "React",
            "SQLite",
            "JWT",
            "XGBoost",
            "Recharts"
        ],
        "code_url": "https://github.com/Nitheeshsiddegowda/Energy_Consumption_Forecasting_and_Recommendation_Agent_ECFRA",
        "demo_url": "",
        "featured": True,
    },

    {
        "num": "02",
        "category": "Python · Automation",
        "title": "PdfTalker (PDF to Audio Converter)",
        "description": (
            "Built a Python application that converts PDF documents into spoken "
            "audio, making digital documents more accessible and convenient to "
            "consume. The application extracts text using PyPDF2 and generates "
            "natural speech using Google Text-to-Speech (gTTS), enabling users "
            "to listen to documents instead of reading them."
        ),
        "tags": [
            "Python",
            "PyPDF2",
            "gTTS"
        ],
        "code_url": "https://github.com/Hemanth-Gowda03/PdfTalker",
        "demo_url": "",
        "featured": False,
    },

    {
        "num": "03",
        "category": "Full-Stack Web Application",
        "title": "SmartConnect - College Management System",
        "description": (
            "Developed a comprehensive college management system with dedicated "
            "portals for management, teachers, and students. The platform "
            "supports attendance management, leave applications, academic "
            "records, and an integrated job portal where management can post "
            "placement opportunities and eligible students can apply based on "
            "defined criteria, providing a centralized solution for campus administration."
        ),
        "tags": [
            "Python",
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
            "SQLite"
        ],
        "code_url": "https://github.com/Nitheeshsiddegowda/SmartConnect",
        "demo_url": "",
        "featured": False,
    },
],

    # -------------------------------------------------------------------
    # CERTIFICATIONS
    # -------------------------------------------------------------------
    "certifications": [
    {
        "icon": "💼",
        "name": "Python Full-Stack Development Internship",
        "issuer": "Pentagon Space Pvt. Ltd.",
        "year": "2026",
    },
    {
        "icon": "🛡️",
        "name": "Google Cybersecurity Professional Certificate",
        "issuer": "Google & Coursera",
        "year": "2024",
    },
    {
        "icon": "🤖",
        "name": "Introduction to Artificial Intelligence",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "🧠",
        "name": "Introduction to Deep Learning",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "💬",
        "name": "Introduction to Natural Language Processing",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "🐍",
        "name": "Introduction to Python",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "🗄️",
        "name": "PostgreSQL Developer",
        "issuer": "Infosys Springboard",
        "year": "2025",
    },
    {
        "icon": "🍃",
        "name": "Developing with MongoDB",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "💻",
        "name": "Software Engineering Fundamentals",
        "issuer": "Infosys Springboard",
        "year": "2024",
    },
    {
        "icon": "✨",
        "name": "ChatGPT-4 Prompt Engineering: ChatGPT, Generative AI & LLM",
        "issuer": "Infosys Springboard",
        "year": "2025",
    },
    {
        "icon": "☁️",
        "name": "Google Cloud Project Fundamentals for DevOps",
        "issuer": "SDM Institute of Technology & KSCSST",
        "year": "2025",
    },
],

    # -------------------------------------------------------------------
    # ACHIEVEMENTS & INVOLVEMENT
    # -------------------------------------------------------------------
    "achievements": [
    {
        "emoji": "🏏",
        "title": "VTU-Level Sports Representative",
        "description": (
            "Represented SDM Institute of Technology in VTU-level cricket, "
            "demonstrating teamwork, leadership, discipline, and the ability "
            "to perform under pressure."
        ),
    },
    {
        "emoji": "🎓",
        "title": "Google Cybersecurity Professional Certificate",
        "description": (
            "Successfully completed Google's 8-course Cybersecurity "
            "Professional Certificate, gaining practical knowledge of "
            "Python, Linux, SQL, SIEM tools, IDS, and cybersecurity "
            "fundamentals."
        ),
    },
    {
        "emoji": "💼",
        "title": "Python Full-Stack Internship",
        "description": (
            "Successfully completed an onsite Python Full-Stack Development "
            "Internship at Pentagon Space Pvt. Ltd., gaining hands-on "
            "experience in Python, SQL, React, web technologies, Git, and "
            "real-world software development practices."
        ),
    },
    {
    "emoji": "🏏",
    "title": "Hobbies & Interests",
    "description": (
        "Enjoy playing cricket and basketball, traveling to new places, "
        "and following movies and sports. These activities help me stay "
        "active, improve teamwork, and maintain a healthy work-life balance."
    ),
    },
],
}
