import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array

# Load the MobileNetV2 pre-trained model
model = MobileNetV2(weights="imagenet")

# Start the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

print("Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Copy of frame for prediction
    image = cv2.resize(frame, (224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    # Predict object
    preds = model.predict(image)
    decoded = decode_predictions(preds, top=1)[0]
    label = decoded[0][1]    # object name
    confidence = decoded[0][2]  # confidence score

    # Show prediction only if confidence is good
    if confidence > 0.4:
        text = f"{label}: {confidence*100:.2f}%"
    else:
        text = "Object not clear"

    # Display prediction text on original frame
    cv2.putText(frame, text, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Live Camera Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()
