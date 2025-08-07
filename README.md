# Daily Numerology & Astrology Insights

![App Preview](https://via.placeholder.com/800x400?text=Beautiful+Numerology+and+Astrology+Insights)

This Streamlit application provides personalized daily numerology and astrology insights based on your life path number and current date. Discover your lucky days, understand your numerology number, explore Chinese zodiac relationships, and get moon phase insights - all in one beautiful interface.

## Features

- **Daily Numerology Number**: Calculate your unique numerology number for the day
- **Life Path Analysis**: Get personalized advice based on your life path number (9)
- **Chinese Zodiac**: Discover your zodiac animal and its relationship with the Tiger
- **Day Analysis**: Identify lucky, neutral, or unlucky days with specific advice
- **Moon Phase Visualization**: See the current moon phase with beautiful visualization
- **Responsive Design**: Works beautifully on both desktop and mobile devices

## How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/yourusername/numerology-insights.git
cd numerology-insights
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run daily_insight.py
```

## How to Use

1. The app will automatically calculate your daily insights based on the current date
2. View your numerology number and its meaning
3. See if today is a lucky, neutral, or unlucky day based on your life path
4. Discover your Chinese zodiac animal and its relationship with the Tiger
5. Explore the current moon phase and its significance

## Requirements

- Python 3.7+
- Streamlit
- Plotly
- Numpy

All dependencies are listed in the `requirements.txt` file.

## Project Structure

```
numerology-insights/
├── daily_insight.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in version control
```

## Deployment

This application can be easily deployed on Streamlit Cloud:

1. Create a new repository on GitHub with your code
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your GitHub repository
4. Select the repository branch and main file path (`daily_insight.py`)
5. Click "Deploy" - your app will be live in minutes!

## Customization

You can personalize this app by:

1. Changing the `LIFE_PATH` constant in the code to match your life path number
2. Modifying the color scheme in the CSS section
3. Adding more zodiac relationships or numerology interpretations
4. Integrating with astronomy APIs for real moon phase data

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This application provides entertainment purposes only. The insights and interpretations should not be taken as professional advice.
