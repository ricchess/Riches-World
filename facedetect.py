import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe modules
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
hands = mp_hands.Hands(max_num_hands=4)
pose = mp_pose.Pose()

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for mirror effect and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Initialize counts and frame color
    frame_color = (0, 255, 0)  # Default green for center gaze
    hand_count = 0
    person_count = 0
    gaze_direction = "Looking Center"

    # Face and gaze detection
    face_results = face_mesh.process(rgb_frame)
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            left_eye = face_landmarks.landmark[474]
            right_eye = face_landmarks.landmark[469]
            nose_tip = face_landmarks.landmark[1]
            
            frame_height, frame_width, _ = frame.shape
            left_eye_x, left_eye_y = int(left_eye.x * frame_width), int(left_eye.y * frame_height)
            right_eye_x, right_eye_y = int(right_eye.x * frame_width), int(right_eye.y * frame_height)
            avg_eye_x = (left_eye_x + right_eye_x) // 2
            avg_eye_y = (left_eye_y + right_eye_y) // 2
            
            horizontal_threshold = frame_width // 10
            vertical_threshold = frame_height // 10

            if avg_eye_x < frame_width // 2 - horizontal_threshold:
                gaze_direction = "Looking Left"
                frame_color = (0, 0, 255)  # Red
            elif avg_eye_x > frame_width // 2 + horizontal_threshold:
                gaze_direction = "Looking Right"
                frame_color = (0, 0, 255)  # Red
            elif avg_eye_y < frame_height // 2 - vertical_threshold:
                gaze_direction = "Looking Up"
                frame_color = (0, 0, 255)  # Red
            elif avg_eye_y > frame_height // 2 + vertical_threshold:
                gaze_direction = "Looking Down"
                frame_color = (0, 0, 255)  # Red"
            else:
                gaze_direction = "Looking Center"

    # Hand detection
    hand_results = hands.process(rgb_frame)
    if hand_results.multi_hand_landmarks:
        hand_count = len(hand_results.multi_hand_landmarks)
        frame_color = (255, 0, 0)  # Blue if hands are detected

    # Person detection (using Pose to approximate person count)
    pose_results = pose.process(rgb_frame)
    if pose_results.pose_landmarks:
        person_count = 1  # Assume at least one person if Pose is detected
        frame_color = (0, 255, 255)  # Yellow if additional people are detected

    # Display information on frame
    cv2.putText(frame, f"Gaze: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, frame_color, 2)
    cv2.putText(frame, f"Hands Detected: {hand_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"People Count: {person_count}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.rectangle(frame, (30, 30), (frame_width - 30, frame_height - 30), frame_color, 3)

    # Show the frame
    cv2.imshow('Advanced Detection System', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
