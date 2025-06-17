import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
#from google import genai
from PIL import Image
import streamlit as st
st.set_page_config(page_title="Math Solver", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

col1,col2=st.columns([2,1])
with col1:
    run=st.checkbox("Run",value=True)
    FrameWindow=st.image([])
with col2:
    output=st.title("Answer")
    output=st.subheader("")


client=genai.configure(api_key="AIzaSyBaBkE8xHWPN2T5KmpbZ5kls4n4ibWh0HM")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
# responses = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works in a few words"
# )

cap = cv2.VideoCapture(0)
cap.set(3, 1200)  
cap.set(4, 720)
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Continuously get frames from the webcam
def getHandinfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)

        # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        return fingers1, lmList1
    else:
        return None

def draw(info,prev_pos,canvas):
    fingers, lmList = info
    current_pos=None
    if fingers==[0,1,0,0,0]:
        current_pos=tuple(map(int, lmList[8][0:2])) 
        if prev_pos is None:
            prev_pos=current_pos
        cv2.line(canvas,current_pos,prev_pos,(255,0,255),10)
    elif fingers==[1,0,0,0,0]:
        canvas=np.zeros_like(img)
    return current_pos,canvas

def sendtoAI(model,canvas,fingers):
    if fingers==[1,1,1,0,0]:
        pil_image = Image.fromarray(canvas)

        response= model.generate_content(['solve this math problem',pil_image])
        print(response.text)
        return response.text
    


prev_pos=None
canvas=None
image_combined = None
result=""
if run:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)  
        if canvas is None:
            canvas=np.zeros_like(img)
            
            
        
        info= getHandinfo(img)
        if info:
            fingers,lmList=info
            print(fingers)
            prev_pos,canvas=draw(info,prev_pos,canvas)
            result=sendtoAI(model,canvas,fingers)
        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.5, 0)
        FrameWindow.image(image_combined, channels="BGR",width=1000)
        
        output.text(result)

        # cv2.imshow("Image", img)
        # cv2.imshow("Canvas", canvas)
        # cv2.imshow("Combined", image_combined)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
cap.release()
