import streamlit as st
from PIL import Image
def app():
	st.balloons()
	st.title("These are some of my projects")
	st.image(Image.open('tarang-github.png'), caption='My Github Profile')
	
	st.subheader("Covid19 Detection of Chest X-Ray Images using Google's Tensorflow Framework")
	st.write("This project utilizes the Keras library of the Tensorflow framework for image processing and the deep learning model does a binary classification and predicts whether a chest X-ray is of a covid positive patient or a covid negative person.")
	# st.subheader("Cryptocurrency Charting Application with Tradingview and Bitquery GraphQL API ")
	# st.write("Tradingview which is one of the most popular charting applications used by Stock Market analysts does not support Cryptocurrency data. In order to place cryptocurrency data in Tradingview, the data has to processed in OHLC format and then the charting is shown. The Chart rendered by Tradingview's widget along with the data passed on by Bitquery GraphQL API shows the data for the Binance Smart Chain Mainnet's latest prices in the Ethereum blockchain. The data is represented in the Candlestick format.")
	# st.image(Image.open('projects1.png'))
	st.write("Github Repository: [https://github.com/tarangshivraj/Covid19_Detection_using_Tensorflow](https://github.com/tarangshivraj/Covid19_Detection_using_Tensorflow)")
	
	st.subheader("Coronary Heart Disease Prediction")
	st.write("This project uses binary classification to predict whether a person may have coronary heart disease in the future or not by using machine learning. This project is deployed on a Streamlit web application.")
	# st.write("CIDS is an open source Intrusion Detection system which makes use RandomForestClassifier in differenciating between different types of intrusion attacks based upon a real world dataset. It has an accuracy of 98%.")
	st.write("Github Repository: [https://github.com/tarangshivraj/coronary-heart-disease](https://github.com/tarangshivraj/coronary-heart-disease)")
	
	st.subheader("House Price Prediction using Tensorflow")
	st.write("This project predicts the house price by using Tensorflow framework for linear regression.")
	# st.write("SocketChat is chat application made using NodeJS and Socket.io keeping vanilla JS as the frontend.")
	st.write("Github Repository: [https://github.com/tarangshivraj/House-Price-Prediction-using-Linear-Regression-and-Tensorflow](https://github.com/tarangshivraj/House-Price-Prediction-using-Linear-Regression-and-Tensorflow)")

	st.subheader("Human Emotional Analysis using MEDIAPIPE framework")
	st.write("This project makes use of the Google's MEDIAPIPE framework to capture human posture coordinates and face mesh and uses Scikit-Learn's RandomForestClassifier to make the multiclass classification which detects human emotions.")
	# st.write("Gift Recommendation System has a set of gifts meant for people above the age of 18 and some for people below the age of 18 in it's SQLite database. The Flask microservice operates a CRUD application along with specifying the type of gifts based upon the user's age.")
	st.write("Github Repository: [https://github.com/tarangshivraj/Human-Emotion-Analysis](https://github.com/tarangshivraj/Human-Emotion-Analysis)")
	st.image(Image.open('icons8-github-48.png'))
	st.write("Check out my [Github Repository](https://github.com/tarangshivraj) for other projects")
