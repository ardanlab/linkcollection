import streamlit as st
import base64
from PIL import Image
import io

# Konfigurasi halaman
st.set_page_config(
    page_title="Synx Tech Portfolio",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS kustom untuk styling
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem auto;
        max-width: 500px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .profile-section {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .profile-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid white;
        margin: 0 auto 1rem;
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        color: white;
        font-weight: bold;
    }
    
    .title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: rgba(255,255,255,0.8);
        font-size: 1rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    .link-button {
        display: block;
        width: 100%;
        padding: 15px 20px;
        margin: 10px 0;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        color: white;
        text-decoration: none;
        text-align: center;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .link-button:hover {
        background: rgba(255,255,255,0.2);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 2rem;
    }
    
    .social-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: rgba(255,255,255,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-decoration: none;
        transition: all 0.3s ease;
        font-size: 1.2rem;
    }
    
    .social-icon:hover {
        background: rgba(255,255,255,0.2);
        transform: scale(1.1);
    }
    
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.6);
        font-size: 0.8rem;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Data portfolio - GANTI DENGAN DATA ANDA SENDIRI
portfolio_data = {
    "profile": {
        "name": "Synx Tech",
        "title": "Full Stack Developer & AI Enthusiast",
        "initials": "ST"
    },
    "links": [
        {
            "title": "🌐 Personal Website",
            "url": "https://synxtech.com",
            "description": "Portfolio lengkap dan blog pribadi"
        },
        {
            "title": "💼 LinkedIn Profile",
            "url": "https://linkedin.com/in/synxtech",
            "description": "Koneksi profesional dan pengalaman kerja"
        },
        {
            "title": "📁 GitHub Repository",
            "url": "https://github.com/synxtech",
            "description": "Source code dan project open source"
        },
        {
            "title": "📝 Technical Blog",
            "url": "https://blog.synxtech.com",
            "description": "Tutorial dan artikel teknis"
        },
        {
            "title": "🎨 UI/UX Portfolio",
            "url": "https://dribbble.com/synxtech",
            "description": "Koleksi design dan prototype"
        },
        {
            "title": "📱 Mobile Apps",
            "url": "https://play.google.com/store/apps/dev?id=synxtech",
            "description": "Aplikasi mobile di Play Store"
        }
    ],
    "social_media": [
        {"icon": "🐦", "url": "https://twitter.com/synxtech", "name": "Twitter"},
        {"icon": "📸", "url": "https://instagram.com/synxtech", "name": "Instagram"},
        {"icon": "💼", "url": "https://linkedin.com/in/synxtech", "name": "LinkedIn"},
        {"icon": "📧", "url": "mailto:hello@synxtech.com", "name": "Email"}
    ]
}

def main():
    local_css()
    
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Profile Section
    st.markdown('<div class="profile-section">', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-image">{portfolio_data["profile"]["initials"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="title">{portfolio_data["profile"]["name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{portfolio_data["profile"]["title"]}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Links Section
    for link in portfolio_data["links"]:
        st.markdown(
            f'<a href="{link["url"]}" target="_blank" class="link-button">'
            f'<strong>{link["title"]}</strong><br>'
            f'<small>{link["description"]}</small>'
            f'</a>',
            unsafe_allow_html=True
        )
    
    # Social Media Links
    st.markdown('<div class="social-links">', unsafe_allow_html=True)
    for social in portfolio_data["social_media"]:
        st.markdown(
            f'<a href="{social["url"]}" target="_blank" class="social-icon" title="{social["name"]}">'
            f'{social["icon"]}'
            f'</a>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(
        '<div class="footer">'
        '© 2024 Synx Tech. All rights reserved.<br>'
        'Made with ❤️ using Streamlit'
        '</div>',
        unsafe_allow_html=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
