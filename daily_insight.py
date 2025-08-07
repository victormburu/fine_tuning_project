import streamlit as st
import datetime
import ephem
import numpy as np
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Daily Numerology & Astrology Insights",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function to add ordinal suffix to day numbers
def get_day_suffix(day):
    if 11 <= day <= 13:
        return f"{day}th"
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return f"{day}{suffixes.get(day % 10, 'th')}"

# Reduce to single digit
def reduce_to_single_digit(a):
    while a > 9:
        a = sum(int(digit) for digit in str(a))
    return a
        
# Get current numerology day number
def get_daily_single_digit():
    today = datetime.date.today()
    total = today.year + today.month + today.day
    return reduce_to_single_digit(total)

# Basic Chinese Zodiac year lookup
def get_chinese_zodiac(year):
    animal_cycle = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Goat", "Monkey", "Rooster",
        "Dog", "Pig"
    ]
    return animal_cycle[(year - 4) % 12]

# Numerology meanings
def get_numerology_meaning(a):
    meaning = {
        1: "Leadership, independence, originality, initiative, self-reliance. This is a day for new beginnings and taking charge.",
        2: "Cooperation, balance, sensitivity, diplomacy, partnership. Focus on relationships and finding harmony today.",
        3: "Creativity, self-expression, joy, optimism, social interaction. Express yourself and enjoy social connections.",
        4: "Stability, practicality, hard work, organization, discipline. Focus on building solid foundations.",
        5: "Freedom, adventure, change, versatility, curiosity. Embrace new experiences and adaptability.",
        6: "Harmony, responsibility, nurturing, service, family. Focus on home, family, and caring for others.",
        7: "Introspection, spirituality, analysis, wisdom, contemplation. A day for reflection and inner growth.",
        8: "Power, authority, material success, ambition, business acumen. Focus on goals and achievements.",
        9: "Compassion, humanitarianism, idealism, selflessness, completion. A day for service and compassion.",
    }
    return meaning.get(a, "Unknown")

# Determine lucky, neutral, or bad based on Victor's life path number
LIFE_PATH = 9

# Get today's numerology day number
def analyse_day(day_num, today_day):
    lucky_numbers = [3, 5, 6, 9]
    unlucky_numbers = [2, 7]
    neutral_numbers = [1, 4, 8]
    lucky_dates = ["1st", "3rd", "5th", "6th", "9th", "10th", "12th", "14th", "15th", "18th",
                   "19th", "21st", "23rd", "24th", "27th", "30th"]
    neutral_dates = ["4th", "8th", "13th", "17th", "22nd", "26th", "28th", "31st"]
    unlucky_dates = ["2nd", "7th", "11th", "16th", "20th", "25th", "29th"]
    
    if today_day in lucky_dates or day_num in lucky_numbers:
        return "Lucky Day", (
            "🌟 Today is aligned with your Life Path 9 energy.\n"
            "- Start new projects, manifest ideas\n"
            "- Speak boldly, network, pitch\n"
            "- Use creativity and spiritual power"
        ), "#4CAF50"
    elif today_day in neutral_dates or day_num in neutral_numbers:
        return "Neutral Day", (
            "🧘 Stay balanced today\n"
            "- Focus on completing existing tasks\n"
            "- Reflect, learn, and maintain discipline\n"
            "- Stay grounded, not rushed"
        ), "#FFC107"
    elif today_day in unlucky_dates or day_num in unlucky_numbers:
        return "Unlucky Day", (
            "⚠️ Caution advised today\n"
            "- Avoid major decisions or risks\n"
            "- Focus on self-care and reflection\n"
            "- Stay patient, avoid conflicts"
        ), "#F44336"
    else:
        return "Neutral Day", (
            "🔮 The day has neutral energy\n"
            "- Proceed with mindfulness and balance"
        ), "#9E9E9E"

# Get today's Chinese Zodiac animal  
def get_tiger_relationship(user_zodiac):
    allies = ["Horse", "Dog"]
    enemies = ["Monkey", "Snake"]
    
    if user_zodiac in allies:
        return "Harmonious relationship with the Tiger today", "😊"
    elif user_zodiac in enemies:
        return "Potential challenges with the Tiger today", "😟"
    else:
        return "Neutral relationship with the Tiger today", "😐"

# Astrology insight (basic moon phase)
def get_moon_phase():
    moon = ephem.Moon()
    today = datetime.date.today()
    moon.compute(f"{today.year}/{today.month}/{today.day}")
    phase = moon.phase
    
    if phase < 7:
        return "New Moon", "A time for new beginnings and setting intentions", "🌑"
    elif 7 <= phase < 14:
        return "First Quarter", "A time for action and making progress on your goals", "🌓"
    elif 14 <= phase < 21:
        return "Waxing Gibbous", "A time for refinement and adjustment", "🌔"
    elif 21 <= phase < 28:
        return "Full Moon", "A time for culmination, reflection, and gratitude", "🌕"
    elif 28 <= phase < 35:
        return "Disseminating Moon", "A time for sharing knowledge", "🌖"
    elif 35 <= phase < 42:
        return "Last Quarter", "A time for introspection and letting go", "🌗"
    else:
        return "Balsamic Moon", "A time for rest and preparation for new cycles", "🌘"

# Create a moon phase visualization
def create_moon_visualization(phase_percent):
    fig = go.Figure()
    
    # Create moon circle
    fig.add_shape(type="circle", x0=0.2, y0=0.2, x1=0.8, y1=0.8, 
                  line_color="lightgray", fillcolor="lightgray")
    
    # Create shadow based on phase
    if phase_percent < 50:
        # Waxing moon - shadow on left
        shadow_width = (50 - phase_percent) * 0.6 / 50
        fig.add_shape(type="circle", x0=0.2, y0=0.2, x1=0.8 - shadow_width, y1=0.8, 
                      line_color="#1a1a1a", fillcolor="#1a1a1a")
    else:
        # Waning moon - shadow on right
        shadow_width = (phase_percent - 50) * 0.6 / 50
        fig.add_shape(type="circle", x0=0.2 + shadow_width, y0=0.2, x1=0.8, y1=0.8, 
                      line_color="#1a1a1a", fillcolor="#1a1a1a")
    
    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        width=200,
        height=200,
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #ffffff;
    }
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #ffffff;
    }
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: #0e1117;
    }
    .css-1d391kg {
        background-color: rgba(255,255,255,0.1);
    }
    .reportview-container .markdown-text-container {
        color: white;
    }
    .header {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        padding: 0.5em;
        background: linear-gradient(90deg, #4A00E0 0%, #8E2DE2 100%);
        border-radius: 10px;
        margin-bottom: 1em;
    }
    .card {
        background: rgba(30, 30, 46, 0.7);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        border-left: 4px solid #8E2DE2;
    }
    .card-title {
        font-size: 1.4em;
        font-weight: bold;
        margin-bottom: 10px;
        color: #a6d1f2;
    }
    .emoji-large {
        font-size: 3em;
        text-align: center;
        margin: 10px 0;
    }
    .insight-box {
        background: rgba(46, 49, 146, 0.3);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .life-path {
        font-size: 1.2em;
        text-align: center;
        padding: 10px;
        background: rgba(142, 45, 226, 0.3);
        border-radius: 10px;
        margin: 10px 0;
    }
    .footer {
        text-align: center;
        margin-top: 2em;
        padding: 1em;
        color: #aaa;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

# Main app
def main():
    today = datetime.date.today()
    day_suffix = get_day_suffix(today.day)
    day_num = get_daily_single_digit()
    user_zodiac = get_chinese_zodiac(today.year)
    day_type, advice, color = analyse_day(day_num, day_suffix)
    tiger_relationship, tiger_emoji = get_tiger_relationship(user_zodiac)
    moon_phase_name, moon_phase_desc, moon_emoji = get_moon_phase()
    
    # Calculate moon phase percentage for visualization
    moon = ephem.Moon()
    moon.compute(f"{today.year}/{today.month}/{today.day}")
    phase_percent = moon.phase / 100 * 50  # Normalize for visualization
    
    # Header
    st.markdown(f'<div class="header">🔮 Daily Numerology & Astrology Insights</div>', unsafe_allow_html=True)
    
    # Top columns
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f'<div class="card"><div class="card-title">📅 Today\'s Date</div>'
                    f'<div style="font-size: 2em; text-align: center; margin: 20px 0;">{today.strftime("%A, %B")} {day_suffix}</div>'
                    f'<div style="text-align: center;">{today.strftime("%Y")}</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="card"><div class="card-title">🧭 Life Path Number</div>'
                    f'<div class="life-path">Your Life Path: {LIFE_PATH}</div>'
                    f'<div class="card-title">🎯 Today\'s Number</div>'
                    f'<div style="font-size: 3em; text-align: center; margin: 10px 0;">{day_num}</div>'
                    f'<div>{get_numerology_meaning(day_num)}</div></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'<div class="card"><div class="card-title">🐉 Chinese Zodiac</div>'
                    f'<div style="font-size: 2em; text-align: center; margin: 20px 0;">{user_zodiac}</div>'
                    f'<div class="card-title">🐅 Tiger Relationship</div>'
                    f'<div class="emoji-large">{tiger_emoji}</div>'
                    f'<div style="text-align: center;">{tiger_relationship}</div></div>', unsafe_allow_html=True)
    
    # Day Analysis
    st.markdown(f'<div class="card"><div class="card-title">🔍 Day Analysis</div>'
                f'<div style="background: {color}; padding: 15px; border-radius: 10px; text-align: center; font-size: 1.5em; margin: 15px 0;">'
                f'{day_type}</div>'
                f'<div class="insight-box">{advice}</div></div>', unsafe_allow_html=True)
    
    # Moon Phase
    col4, col5 = st.columns([1, 2])
    
    with col4:
        st.markdown(f'<div class="card"><div class="card-title">🌙 Moon Phase</div>'
                    f'<div class="emoji-large">{moon_emoji}</div>'
                    f'<div style="text-align: center; font-size: 1.4em; margin: 10px 0;">{moon_phase_name}</div>'
                    f'<div style="text-align: center;">{moon_phase_desc}</div></div>', unsafe_allow_html=True)
    
    with col5:
        st.markdown(f'<div class="card"><div class="card-title">🌗 Moon Phase Visualization</div>', unsafe_allow_html=True)
        fig = create_moon_visualization(moon.phase)
        st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown('<div class="footer">Created with ❤️ using Python and Streamlit | Daily Numerology & Astrology Insights</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()