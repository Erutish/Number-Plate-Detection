import streamlit as st
from ultralytics import YOLO
from easyocr import Reader
import time
import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from detect_and_recognize import detect_number_plates, recognize_number_plates


st.set_page_config(page_title="Auto NRP", page_icon=":car:", layout="wide")

st.title("Auto Number Plate Recognition System :car:")
st.markdown(".......")


uploaded_file=st.file_uploader("upload an Image", type=["png","jpg","jpeg"])
upload_path = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(upload_path, exist_ok=True)
print(uploaded_file)
if uploaded_file is not None:
    # construct the path to the uploaded image
    # and then save it in the `uploads` folder
    image_path=os.path.sep.join([upload_path,uploaded_file.name])
    with open(image_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("In progress....🛠"):
        # load the model from the local directory
        model=YOLO("../runs/detect/train2/weights/best.pt")

        # initialize the EasyOCR reader
        reader=Reader(["en"],gpu=True)

        # convert the image from BGR to RGB
        image=cv2.cvtColor(cv2.imread(image_path),cv2.COLOR_BGR2RGB)

        # make a copy of the image to draw on it
        image_copy=image.copy()


        col1,col2=st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image)

        number_plate_list=detect_number_plates(image, model)

        if number_plate_list !=[]:
            number_plate_list = recognize_number_plates(image_path, reader,
                                                        number_plate_list)
            
            for box,text in number_plate_list:
                cropped_number_plate=image_copy[box[1]:box[3], box[0]:box[2]]

                cv2.rectangle(image,(box[0],box[1]),(box[2],box[3]), (0,255,0),2)
                cv2.putText(image,text,(box[0], box[3]+15),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

                with col2:
                    st.subheader("Number Plate Detection ")
                    st.image(image)

                st.subheader("ropped Number Plate ")
                st.image(cropped_number_plate)
                st.success("Number plate test:**{}**".format(text))

else:
    st.info("Please, upload an image to get started")
