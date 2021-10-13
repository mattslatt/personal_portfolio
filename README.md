# Matt's Portfolio
Compilation of data science projects

# PhD Dissertation
"A nano-sized dose of toxicology: elucidating the disconnect between nanomaterial dosimetry and biological effects"
* Chapters 2 and 3 incorporate logistic regression modeling to predict pesticide toxicity
* Chapter 4 features the classification (Naive Bayes), multidimensional scaling (PCA), and statistical analysis (t-test, ANOVA) of >20 million data points
* Chapter 5 expands upon with additional classification (KNN) and multidimensional scaling (PCoA) techniques
![](/img/metagenomics abstract.png)


# [Project 1: Music Genre Analysis](https://github.com/mattslatt/spotify)
* Visualized genre time-series data with matplotlib and quantified changes with hypothesis testing
* Engineered novel features to recommend relatively unknown artists according to user input
* Combined Random Forest and KNN models to predict a song’s genre based on features called from Spotify’s API
![](/img/top_10_genre_time_scatter.png)

# [Project 2: Podcast Topic Mining](https://github.com/mattslatt/podcast_reviews)
* Cleaned and vectorized review text to train Naive Bayes and Linear Support Vector models for sentiment prediction, optimized for F1 score with minority class oversampling
* Highlighted podcast topics most likely to incur positive or negative audience responses based on text feature importance
![](/img/positive_text_coefficients.png)

# [Project 3: Fraudulent Transaction Detection](https://github.com/mattslatt/podcast_reviews)
* Collaborated with a team of four  to build and deploy an XGBoost model that flags fraudulent charges based on transaction metadata
* Engineered location-based features and resolved missing data by imputing values with linear regression to boost model performance