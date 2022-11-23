# FaceZoom, Python, OpenCV - Face Lock and Auto Zoom 

## Uses OpenCV and Haar cascades to locate users face, and shows user face in a window.
Intended to locate a single face, this programe uses Haar cascades to locate a face and snap it to the window. It will scale the window/face to a specified resolution. Footage in window is stabilized through checking previous frames, for any stutters and previous faces.

## How to use:
1. Clone project
2. Install numpy, pillow, and opencv using "pip install <name>"
3. Run zoom.py

## Features to come:
- smooth-zoom.py - modified version of original which instead smoothly 'moves' closer to detected face, instead of snapping.

## Known issues:
- Due to file paths, currently only works on Windows systems
