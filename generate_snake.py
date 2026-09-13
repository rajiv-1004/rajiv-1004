import os
from datetime import datetime

username = "rajiv-1004"

# Create dist folder
os.makedirs("dist", exist_ok=True)

# Contribution grid (based on your profile - 94 contributions)
# Row = day of week (Mon, Wed, Fri), Column = week
# 0 = no contribution, 1 = low, 2 = high
contributions = [
    # Mon row
    [0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # Wed row
    [0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # Fri row
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

cell_size = 12
cell_gap = 2
padding = 40
grid_width = 54
grid_height = 3

width = grid_width * (cell_size + cell_gap) + padding * 2
height = grid_height * (cell_size + cell_gap) + padding * 2 + 120

# Create SVG
svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes slither {{
        0% {{ transform: translateX(0px); }}
        100% {{ transform: translateX(800px); }}
      }}
      
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.6; }}
      }}
      
      .snake-body {{
        animation: slither 4s ease-in-out infinite;
      }}
      
      .contribution-cell {{
        transition: fill 0.2s;
      }}
      
      .contribution-cell:hover {{
        filter: brightness(1.5);
      }}
    </style>
  </defs>
  
  <!-- Dark Background -->
  <rect width="{width}" height="{height}" fill="#0d1117"/>
  
  <!-- Title -->
  <text x="{width/2}" y="30" font-family="Arial, sans-serif" font-size="22" fill="#E63946" text-anchor="middle" font-weight="bold">
    GitHub Contribution Snake
  </text>
  
  <!-- Subtitle -->
  <text x="{width/2}" y="52" font-family="Arial, sans-serif" font-size="12" fill="#8b949e" text-anchor="middle">
    Your contribution pattern: {username}
  </text>
  
  <!-- Contribution Grid -->
  <g id="grid" transform="translate({padding}, {padding})">
'''

# Generate contribution grid cells
for row in range(len(contributions)):
    for col in range(len(contributions[row])):
        x = col * (cell_size + cell_gap)
        y = row * (cell_size + cell_gap)
        contribution_level = contributions[row][col]
        
        # Color based on contribution level
        if contribution_level == 0:
            color = "#161B22"
        elif contribution_level == 1:
            color = "#0E4429"
        else:
            color = "#39D353"
        
        svg += f'    <rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="{color}" stroke="#21262d" stroke-width="0.5" class="contribution-cell" rx="2"/>\n'

svg += '''  </g>
  
  <!-- Snake Animation -->
  <g class="snake-body" transform="translate(50, 150)">
    <!-- Snake Head (Red) -->
    <circle cx="0" cy="0" r="8" fill="#E63946" filter="drop-shadow(0 0 4px #E63946)"/>
    <!-- Snake Body -->
    <circle cx="-12" cy="0" r="7" fill="#F1FAEE" opacity="0.85"/>
    <circle cx="-22" cy="0" r="6" fill="#E63946" opacity="0.7"/>
    <circle cx="-30" cy="0" r="5" fill="#E63946" opacity="0.5"/>
  </g>
  
  <!-- Legend -->
  <g transform="translate(40, ''' + str(int(height) - 50) + ''')">
    <text x="0" y="0" font-family="Arial, sans-serif" font-size="11" fill="#8b949e" font-weight="bold">LEGEND:</text>
    
    <rect x="0" y="10" width="12" height="12" fill="#161B22" stroke="#21262d"/>
    <text x="18" y="18" font-family="Arial, sans-serif" font-size="10" fill="#8b949e">None</text>
    
    <rect x="80" y="10" width="12" height="12" fill="#0E4429" stroke="#21262d"/>
    <text x="98" y="18" font-family="Arial, sans-serif" font-size="10" fill="#8b949e">Low</text>
    
    <rect x="150" y="10" width="12" height="12" fill="#39D353" stroke="#21262d"/>
    <text x="168" y="18" font-family="Arial, sans-serif" font-size="10" fill="#8b949e">High</text>
    
    <circle cx="230" cy="16" r="5" fill="#E63946" filter="drop-shadow(0 0 2px #E63946)"/>
    <text x="242" y="18" font-family="Arial, sans-serif" font-size="10" fill="#8b949e">Snake</text>
  </g>
  
  <!-- Footer -->
  <text x="{width/2}" y="{height - 15}" font-family="Arial, sans-serif" font-size="9" fill="#6e7681" text-anchor="middle">
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 94 contributions in last year
  </text>
</svg>'''

# Write SVG to file
output_path = "dist/github-contribution-grid-snake.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ Snake animation created successfully!")
print(f"📁 File saved: {output_path}")
print(f"🐍 Your snake is now eating through your contributions!")
print(f"🔴 Color: Red (#E63946) - Your brand color")
