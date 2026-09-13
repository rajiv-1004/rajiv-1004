import os
from datetime import datetime

username = "rajiv-1004"

# Create dist folder
os.makedirs("dist", exist_ok=True)

svg = f'''<svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes slither {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(700px); }}
      }}
      .snake-body {{ animation: slither 3s infinite; }}
    </style>
  </defs>
  <rect width="800" height="200" fill="#0d1117"/>
  <g stroke="#21262d" stroke-width="1">
    <line x1="0" y1="50" x2="800" y2="50"/>
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="150" x2="800" y2="150"/>
  </g>
  <g class="snake-body">
    <circle cx="50" cy="100" r="12" fill="#58a6ff"/>
    <circle cx="35" cy="100" r="10" fill="#79c0ff"/>
    <circle cx="22" cy="100" r="9" fill="#79c0ff" opacity="0.8"/>
    <circle cx="11" cy="100" r="8" fill="#79c0ff" opacity="0.6"/>
  </g>
  <text x="400" y="30" font-family="Arial" font-size="24" fill="#c9d1d9" text-anchor="middle">
    Snake {username} Contribution Animation
  </text>
  <text x="400" y="190" font-family="Arial" font-size="12" fill="#8b949e" text-anchor="middle">
    Generated: {datetime.now().strftime('%Y-%m-%d')}
  </text>
</svg>'''

# IMPORTANT: Use UTF-8 encoding for Windows compatibility
with open("dist/github-contribution-grid-snake.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ Snake created successfully!")