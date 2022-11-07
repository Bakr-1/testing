import os
import cv2
import numpy as np
import mediapipe as mp

mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

image_path = 'images'
images = os.listdir(image_path)
image_index = 0
bg_image = cv2.imread(image_path + '/' + images[image_index])
cap = cv2.VideoCapture(0)

while cap.isOpened():
    image = cap.read()
    frame = cv2.flip(image, 1)
    height, width, channel = frame.shape
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_selfie_segmentation.process(RGB)
    mask = results.segmentation_mask
    conditon = np.stack((mask,) * 3, axis=-1) > 0.6
    bg_image = cv2.resize(bg_image, (width, height))
    output_image = np.where(conditon, frame, bg_image)
    cv2.imshow('Selfie Segmentation', output_image)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        if image_index != len(images) - 1:
            image_index += 1
        else:
            image_index = 0
        bg_image = cv2.imread(image_path + '/' + images[image_index])
cap.release()
cv2.destroyAllWindows()