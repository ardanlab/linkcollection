import streamlit as st

# Page config
st.set_page_config(
    page_title="My Apps - Links",
    page_icon="🔗",
    layout="centered"
)

# Custom CSS for Linktree-style design
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 600px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Profile section */
    .profile-section {
        text-align: center;
        padding: 2rem 0;
        animation: fadeIn 0.6s ease-in;
    }
    
    .profile-img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        margin-bottom: 1rem;
        object-fit: cover;
    }
    
    .profile-name {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .profile-bio {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        margin: 0.5rem 0 2rem 0;
    }
    
    /* Link button styling */
    .link-button {
        display: block;
        background: white;
        color: #667eea;
        padding: 1.2rem;
        margin: 1rem 0;
        border-radius: 12px;
        text-decoration: none;
        text-align: center;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        animation: slideUp 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .link-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .link-button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.1);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .link-button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .link-icon {
        margin-right: 8px;
        font-size: 1.2rem;
    }
    
    /* Social media icons */
    .social-links {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem 0;
    }
    
    .social-icon {
        display: inline-block;
        width: 45px;
        height: 45px;
        background: rgba(255,255,255,0.2);
        border-radius: 50%;
        margin: 0 8px;
        line-height: 45px;
        color: white;
        font-size: 1.3rem;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .social-icon:hover {
        background: white;
        color: #667eea;
        transform: scale(1.1);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Stagger animation for links */
    .link-button:nth-child(1) { animation-delay: 0.1s; }
    .link-button:nth-child(2) { animation-delay: 0.2s; }
    .link-button:nth-child(3) { animation-delay: 0.3s; }
    .link-button:nth-child(4) { animation-delay: 0.4s; }
    .link-button:nth-child(5) { animation-delay: 0.5s; }
    .link-button:nth-child(6) { animation-delay: 0.6s; }
    
    /* Footer */
    .custom-footer {
        text-align: center;
        color: rgba(255,255,255,0.7);
        padding: 2rem 0 1rem 0;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Profile Section
st.markdown("""
    <div class="profile-section">
        <img src="https://ui-avatars.com/api/?name=My+Apps&size=120&background=667eea&color=fff&bold=true" class="profile-img">
        <h1 class="profile-name">My Apps Collection</h1>
        <p class="profile-bio">Folder Ardan<br>Kumpulan aplikasi yang saya buat</p>
    </div>
""", unsafe_allow_html=True)

# App Links Data - EDIT SESUAI APLIKASI KAMU
apps = [
    {
        "name": "🗜️ 100% Safe Auto Compress PDF and Image",
        "url": "https://autocompress.streamlit.app/",
        "description": "Safe Auto Compress"
    },
    {
        "name": "🪙 Gold Price and Forecast",
        "url": "https://golddigger.streamlit.app",
        "description": "Gold Price and Forecast"
    },
    {
        "name": "📈 Crypto Prediction V1 CD",
        "url": "https://krippred.streamlit.app",
        "description": "Track your favorite Crypto"
    },
    {
        "name": "📈 Crypto Prediction V2 CG",
        "url": "https://krippred2.streamlit.app",
        "description": "Track your favorite Crypto"
    }
]

# Display Links
for i, app in enumerate(apps):
    st.markdown(f"""
        <a href="{app['url']}" target="_blank" class="link-button" style="animation-delay: {i*0.1}s;">
            <span class="link-icon">{app['name'].split()[0]}</span>
            <span>{' '.join(app['name'].split()[1:])}</span>
        </a>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# Social Media Links - EDIT SESUAI AKUN KAMU
st.markdown("""
    <div class="social-links">
        <a href="https://github.com/ardanplayground" target="_blank" class="social-icon">
            <i class="fab fa-github"></i> 💻
        </a>
        <a href="mailto:ardan.kusuma29@gmail.com" class="social-icon">
            📧
        </a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="custom-footer">
        Made with ❤️ using Streamlit<br>
        © 2024 All Rights Reserved
    </div>
""", unsafe_allow_html=True)
