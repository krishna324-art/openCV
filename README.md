# openCV — Computer Vision Experiments

A small collection of OpenCV-based experiments demonstrating basic real‑time video processing, object detection/counting, tracking with trails, segmentation, and a "cartoonify" effect. These scripts were implemented to explore common image processing techniques and to build simple demos that run on a webcam or video file.

## What I did (summary)
- Implemented several standalone Python scripts that demonstrate different OpenCV capabilities:
  - live camera capture and display with simple processing.
  - object counting using background/contour based techniques.
  - simple object detection demo(s).
  - tracking where detected people (or moving objects) leave visual trails.
  - image segmentation to isolate regions of interest.
  - a "cartoonify" effect that stylizes images using smoothing + edge detection (in the `cartoonify/` folder).
- Organized demos into top-level scripts and small folders for project assets and experiments (`cartoonify/`, `shap/`, `videos/`).

## Repository structure
- `live_camera_feed.py` — Capture frames from a webcam (or video device) and show a live feed with optional processing.
- `object_caounting.py` — Count moving objects/contours in a video stream. (Note: filename contains a typo `caounting`.)
- `people_with_trail.py` — Track moving people/objects and draw trails showing their recent paths.
- `segmentation.py` — Demonstrates simple segmentation techniques to separate foreground/background or isolate colors/regions.
- `simple _object_detection.py` — A minimal object detection example (file name contains a space: `simple _object_detection.py`).
- `cartoonify/` — Folder containing a script(s) and resources to convert images into a cartoon-like look (likely using bilateral filtering + edge detection).
- `shap/` — Auxiliary folder (contents may include SHAP explainability examples or other assets).
- `videos/` — Place sample videos here if you want to test the scripts with prerecorded input.

## Key techniques used
- Webcam / video capture with OpenCV (`cv2.VideoCapture`).
- Frame-by-frame processing (grayscale conversion, Gaussian/Bilateral filtering).
- Edge detection (Canny) and contour detection for counting / shape extraction.
- Background subtraction or frame-differencing for detecting motion.
- Simple tracking via centroid tracking / object ID assignment (for trails).
- Color thresholding or morphological operations for segmentation.
- Stylization (cartoon effect): smoothing + edge mask overlay.

## Prerequisites
- Python 3.8+
- OpenCV
- NumPy
- Optional: imutils (for helper functions), matplotlib (for visualization in some experiments)

Install the typical dependencies with pip:

```bash
python -m pip install --upgrade pip
pip install opencv-python numpy
# Optional helpers:
pip install imutils matplotlib
```

If you need full OpenCV contrib features (e.g., some advanced trackers or algorithms), install:
```bash
pip install opencv-contrib-python
```

## How to run the demos
General notes:
- Most scripts accept either a webcam device (default) or a path to a video file. If a script supports flags, the header or code will show the available CLI options.
- Press `q` (or the key indicated in the script) to quit windows and stop processing.

Examples:

- Live camera feed:
```bash
python live_camera_feed.py
```

- Object counting (example using a video file):
```bash
python object_caounting.py --input videos/example.mp4
```
If the script expects positional args or has specific flags, run it with `-h` or inspect the top of the file to see usage.

- People tracking with trails:
```bash
python people_with_trail.py --source 0
```
(Here `--source 0` selects the default webcam. Replace `0` with a file path to use a video.)

- Segmentation example:
```bash
python segmentation.py --image inputs/example.jpg
```

- Simple object detection:
```bash
python "simple _object_detection.py"
```
(Notice the filename includes a space; consider renaming it to `simple_object_detection.py` for convenience.)

- Cartoonify example (if the script is `cartoonify/cartoonify.py`):
```bash
python cartoonify/cartoonify.py --image inputs/example.jpg
```

## Tips and suggestions
- Rename files with typos or spaces to be more consistent (e.g., `object_counting.py`, `simple_object_detection.py`).
- Add a `requirements.txt` to make environment setup reproducible:
  ```
  opencv-python
  numpy
  imutils
  matplotlib
  ```
