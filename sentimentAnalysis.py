import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from pywaffle import Waffle
import numpy as np


def main():

	csv_plot('radison_blu.csv')
	csv_plot('e_hotel.csv')
	csv_plot('park_hyatt.csv')
	csv_plot('raj_park_chennai.csv')
	csv_plot('raj_residency.csv')
	csv_plot('residency_towers.csv')
	csv_plot('the_park_chennai.csv')
	csv_plot('accord.csv')
	csv_plot('peace_inn.csv')


def csv_plot(str):
	reviews = pd.read_csv(str)
	sia = SentimentIntensityAnalyzer()

	reviews['neg'] = reviews['Review_Text'].apply(lambda x:sia.polarity_scores(x)['neg'])
	reviews['neu'] = reviews['Review_Text'].apply(lambda x:sia.polarity_scores(x)['neu'])
	reviews['pos'] = reviews['Review_Text'].apply(lambda x:sia.polarity_scores(x)['pos'])
	reviews['compound'] = reviews['Review_Text'].apply(lambda x:sia.polarity_scores(x)['compound'])
	

	print(reviews.head())
	plt.title(str,fontdict=None,loc='center',pad=None)
	#print(reviews['compound'])
	height = reviews['compound']
	bars = ()
	y_pos = np.arange(len(reviews['Hotel_name']))
	plt.bar(y_pos, height)
	plt.xticks(y_pos, bars)
	#plt.show()


	pos_review = [j for i,j in enumerate(reviews['Review_Text']) if reviews['compound'][i] > 0.2]
	neu_review = [j for i,j in enumerate(reviews['Review_Text']) if 0.2>=reviews['compound'][i] >=-0.2]
	neg_review = [j for i,j in enumerate(reviews['Review_Text']) if reviews['compound'][i] < -0.2]
	
	pos_percent = len(pos_review)*100/len(reviews['Review_Text'])
	neu_percent = len(neu_review)*100/len(reviews['Review_Text'])
	neg_percent = len(neg_review)*100/len(reviews['Review_Text'])
	
	print("Percentage of positive review: {}%".format(pos_percent))
	print("Percentage of neutral review: {}%".format(neu_percent))
	print("Percentage of negative review: {}%".format(neg_percent))
	
	data = {'Positive':pos_percent,'Negative':neg_percent,'Neutral':neu_percent}
	fig = plt.figure(
	    FigureClass = Waffle, 
	    rows=5, 
	    values=data,
	    legend = {'loc':'upper left','bbox_to_anchor':(1.1, 1)}
	)
	#plt.show()


	return


if __name__ == '__main__':
	main()



