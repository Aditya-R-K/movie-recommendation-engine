import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("D:\Study\Acadamics\Third year\Sem 5\SEPM\SDL\Project\Code\movie_dataset.csv")
features = ['keywords','cast','genres','director']


for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row)

df["combined_features"] = df.apply(combine_features,axis=1)

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix) 

movie_user_likes = input("Enter movie name\n")
try:
	movie_index = get_index_from_title(movie_user_likes)
except :
	print("Movie not in database")
	quit()

similar_movies =  list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

print("Similar movies to ",movie_user_likes," is")
i=1
for element in sorted_similar_movies:
		print (get_title_from_index(element[0]))
		i=i+1
		if i>10:  
			break 