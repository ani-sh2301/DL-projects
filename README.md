
# 1. Sign Language Detection
<li>Data Collection and Preprocessing: Selected the INCLUDE50 dataset and converted video files into frames for further analysis. Extracted relevant features from the video frames, focusing on hand movements, facial expressions, and body posture.

<li>Recognition System Development: Built an LSTM-based deep learning model for sign language recognition, training it with labeled data to recognize glosses or words from sign language videos. Optimized the model for real-time performance using knowledge distillation and LLM fine-tuning with the PEFT method(LoRA).

<li>Real-Time Sign Recognition and Translation: Implemented a system to process live video streams, ensuring low latency and high accuracy in recognizing sign language gestures. Translated the recognized glosses into complete sentences in English, facilitating seamless communication.

# 2. Virtual AI Mouse
<li>Hand Gesture-Based Cursor Control: This AI virtual mouse project utilizes computer vision techniques to detect and interpret hand gestures, allowing users to move the mouse cursor and perform various actions such as clicking, double-clicking, and scrolling. The system recognizes specific hand signs using 'mediapipe' in real-time to map them to corresponding mouse actions, providing an intuitive and touch-free interaction experience.

<li>Functionality and Automation: The project employs libraries such as pyautogui and autogui for automation tasks, enabling the virtual mouse to execute precise cursor movements and simulate mouse events programmatically. This includes single and double-clicking, as well as scrolling, making it a versatile tool for hands-free computer operation.

<li>Technological Integration: Combining advanced image processing techniques with real-time gesture recognition, the virtual mouse system processes live video feed from a camera. Using machine learning algorithms, it identifies hand positions and gestures accurately, translating them into seamless mouse commands for an efficient and user-friendly experience.
