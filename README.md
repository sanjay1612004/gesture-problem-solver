# ✋🧠 Handwritten Math Solver with AI (Gemini + OpenCV + Streamlit)

This project is a **Hand Gesture-Based Math Solver** that allows users to write math expressions in the air using hand tracking. It then uses **Google Gemini AI** to recognize and solve the handwritten equation.

---

## 🧰 Tech Stack

- **Python**
- **OpenCV** - For real-time webcam video processing
- **cvzone** - Simplified interface for OpenCV and MediaPipe hand tracking
- **Google Generative AI (Gemini API)** - For solving handwritten math problems
- **Streamlit** - For the web interface
- **Pillow** - Image handling before sending to AI

---

## 📸 Demo Screenshot

![Demo](assets/thumbnail.png)

---

## 🎥 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/EWNJfPrH384/maxresdefault.jpg)](https://www.youtube.com/watch?v=EWNJfPrH384)

Click the thumbnail above or [watch the video on YouTube](https://www.youtube.com/watch?v=EWNJfPrH384).

---

## 📺 Features

- ✋ Real-time **hand detection** and **gesture recognition**
- 🖌️ Draw math problems using only your **index finger**
- ♻️ Use the **thumb up gesture** to clear the canvas
- 🧠 Use the **three-finger gesture** to send the canvas to Google Gemini AI for solving
- 📺 Web-based UI using **Streamlit** for interaction and result display

---

## 🖥️ How It Works

| Gesture | Action |
|--------|--------|
| ☝️ Index finger up | Draw on canvas |
| 👍 Thumb up | Clear canvas |
| 🤟 First 3 fingers up | Send image to Gemini for solution |

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hand-math-solver.git
cd hand-math-solver
