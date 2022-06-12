import logging
from app.libs.ml.rec_engine import RecommendationEngine

def get_recommendation(title: None):

  logging.debug("get_recommendation")

  rec_engine = RecommendationEngine()

  if title not in rec_engine.get_all_titles():
    response_object = {
      "status": "Success",
      "message": "No data",
    }
    return response_object, 200

  result_final = rec_engine.get_recommendations(title)
  names = []
  dates = []
  for i in range(len(result_final)):
      names.append(result_final.iloc[i][0])
      dates.append(result_final.iloc[i][1])

  response_object = {
      "status": "Success",
      "message": names,
  }

  return response_object, 200