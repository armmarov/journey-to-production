import re
import base64
import numpy as np
from io import BytesIO
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from PIL import Image

class YoloEngine:

  def __init__(self):

    # Load a pretrained YOLO model (recommended for training)
    self.model = YOLO('./app/libs/yolo/best.pt')

  def predict(self, image):

    img_strip = re.sub('^data:image/.+;base64,', '', image)
    img_raw = Image.open(BytesIO(base64.b64decode(img_strip)))
    img_resized = img_raw.resize((640, 640))

    # Perform object detection on an image using the model
    results = self.model.predict(img_resized)
    color_list = [(255,0,0)]
    for r in results:
        
        annotator = Annotator(np.ascontiguousarray(img_resized))
        
        boxes = r.boxes
        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            s = box.conf
            annotator.box_label(b, f"{self.model.names[int(c)]} {round(s.item(),3)}", color_list[0])
    
    img_annotated = annotator.result() 
    pil_img = Image.fromarray(img_annotated)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

    return new_image_string
