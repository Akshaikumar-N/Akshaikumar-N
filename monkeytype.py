import requests

APE_KEY = "YOUR_API_KEY"
URL = f"https://api.monkeytype.com/user/stats?key={NjkzZGU4OTAzNTQwYWRkNjQ2ZDYxNGM5Lmk2VXk3TmdPMTJUWVl0ZVpoNWxCS3NaUnZjTzhjM0lD}"

resp = requests.get(URL).json()

wpm = resp['wpm']
accuracy = resp['accuracy']

# Generate a simple SVG badge
svg = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="50">
  <rect width="300" height="50" fill="#111"/>
  <text x="10" y="30" fill="#fff" font-size="16">WPM: {wpm} | Acc: {accuracy}%</text>
</svg>
'''

with open("monkeytype.svg", "w") as f:
    f.write(svg)
