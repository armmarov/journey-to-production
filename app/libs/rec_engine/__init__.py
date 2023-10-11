import difflib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:

  def __init__(self):

    self.df2 = pd.read_csv('./app/libs/rec_engine/tmdb.csv')

    count = CountVectorizer(stop_words='english')
    self.count_matrix = count.fit_transform(self.df2['soup'])

    cosine_sim2 = cosine_similarity(self.count_matrix, self.count_matrix)

    self.df2 = self.df2.reset_index()
    self.indices = pd.Series(self.df2.index, index=self.df2['title'])
    self.all_titles = [self.df2['title'][i] for i in range(len(self.df2['title']))]

  def get_recommendations(self, title):
    cosine_sim = cosine_similarity(self.count_matrix, self.count_matrix)
    idx = self.indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = self.df2['title'].iloc[movie_indices]
    dat = self.df2['release_date'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title','Year'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return return_df
  
  def get_all_titles(self):
    return self.all_titles