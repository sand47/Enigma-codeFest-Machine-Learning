# Enigma-codeFest-Machine-Learning 2018

Following is the approach I took for the Analytics Vidhya Enigma-codeFest-Machine-Learning Competition,I got a public Leaderboard loss of 787.56:

1. My solution approach was simple and straight forward. First, I did data visuluziation and saw the distribution of data and got an idea of what regression algorithm to use. I used seaborn to plot and find correlation to find important features on first look. I plotted the histrogram of the data and found that variables like Views and Reputuation are distributed with high values and UserName,ID features are unnecessary features which can be removed.

2. Next I spent most of my time on data preprocessing where I removed unwanted features,scaling,filtering and did feature engineering which was a key element for my success. I used Binarizer as a new feature in my training data which could say if Answers features has some value or not above a thershold.

3.I tried with different algorithms like SGDRegressor,SVR and even decision tree and neither of them work as I thought at first as the data distribution is polynomial.Therefore I took PolynomialRegressor with Linear regression LassoLars with alpha 0.021 and min_iter 75 which I found to be a best fit for this data

4.Cross validation was the key and I splitted my data with test size of 0.22 and trained it to get a r2 score of 0.91 on val set. To get less loss I tried different approachs like progressive learning, Xgboost,ANN and neither of them worked. So I decided to fine tuning hyperparamter that I had to get a good score. 

5. One important factor which I found important was that, I removed Views feature if the value was more than 3000000 from the training set as I found that only 4 values in the test set had similar higher value which contributed to majority of the loss. Once I removed it the loss reduced a lot and I varied my Binarizer thershold to get this score. 



 
