# 2D BVH Generator
This code is designed to show the difference between brute force ray-tracing </br>
and using a BVH to simplify the process. </br>
## Installation
Clone repo: `git clone https://github.com/CJSadowitz/2D_BVH_Algorithm.git` </br>
Make venv: `python3 -m venv venv` </br>
Init venv: `source venv/bin/activate` </br>
Install Dependencies `pip install -r requirements.txt` </br>
## Simulating BVH in 2D
This is a 2D example of how a Bounding Volume Heirarchy is constructed for </br>
use in a ray tracer. </br>
### Running:
A random orientation of vertices will be drawn on screen and a BVH automatically constructed </br>
A brute force algorithm has been used aswell to show differences in implementation </br>
A Green Dot will appear on screen for brute force success (currently commented out in the code) </br>
A Red Dot will appear on screen along with an AABB for BVH collision success </br>
Run: `python3 main.py` to see a simulated construction of a BVH </br>
