import logging
from app.libs.yolo import YoloEngine

yolo_engine = YoloEngine()

def predict_image(image: None):

  logging.debug("predict_image")

  response_object = {
      "status": "Success",
      "message": yolo_engine.predict(image=image),
  }

  return response_object, 200