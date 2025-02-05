
Advanced Real-Time Face, Eye, Hand, and Person Detection System

This project is a real-time detection system that uses a webcam to monitor and track face direction, hand landmarks, and multiple people detection with color-coded frames for different scenarios. It's built using Python and MediaPipe, providing highly accurate tracking and detection.

Features
- Face Detection: Detects and tracks faces in real-time.
  - Green Frame: Face is centered in the camera.
  - Red Frame: Face is looking left, right, up, or down.
  - Blue Frames: When multiple faces are detected, each one gets a blue frame.
- Hand Detection: Draws white dots on detected hands for real-time tracking.
- Person Detection: Counts and highlights multiple people in the webcam view.
- Face Count Display: Shows how many faces are currently detected on the screen.

Requirements
- Python 3.9 or later (but not 3.13+ due to MediaPipe compatibility)
- OpenCV (cv2)
- MediaPipe (mediapipe)

Install Dependencies
Run the following commands to install the required packages:
```
pip install opencv-python-headless mediapipe numpy
```

Usage
1. Clone or download the project.
2. Run the main Python file:
   ```
   python facedetect.py
   ```
3. Press 'q' to stop the program.

How It Works
- Face Detection: Uses MediaPipe’s Face Detection and Face Mesh modules to track the position of the face.
- Hand Detection: Detects hands and marks key points using white dots.
- Multiple People Detection: Uses face detection to count the number of people in the frame.
- Frame Colors:
  - Green: When the face is at the center of the frame.
  - Red: When the face is looking left, right, up, or down.
  - Yellow: When multiple faces are detected.

Project Structure
```
- facedetect.py  # Main script for running the detection system
- README.md      # Project documentation
```

Demo
The detection system can be used for:
- Monitoring students in an examination hall.
- Real-time face and gaze tracking.
- Hand detection and gesture analysis.
- Crowd monitoring and counting.

Example Output
- When a face is detected at the center, the frame around it is green.
- Moving the face in any other direction turns the frame red.
- If multiple people appear in the frame, each face gets a blue frame.

Future Enhancements
- Add gesture-based controls using hand detection.
- Integrate object detection for identifying other items in the frame.
- Optimize for lower latency and higher frame rates.

Author
Developed by Riches Lomel with assistance from OpenAI.
