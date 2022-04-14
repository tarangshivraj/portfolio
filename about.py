import streamlit as st
import datetime
import time 
from PIL import Image

def getAge(year: int, month: int, day: int)->int:
	year -= 2002
	if month == 8 and day == 6:
		return year
	else:
		return year-1

year, email = datetime.datetime.now(), 'tarangshivraj@gmail.com'
name, age = "Tarang Shivraj Jaiswal", getAge(year.year, year.month, year.day) #, 'https://www.cloudskillsboost.google/public_profiles/ff40dc52-a7bd-4376-b1a8-8201253937a3'
skills = ['Data Science', 'Software Development', 'Artificial Intelligence & Machine Learning']
dob, linkedin, muj = "6 August 2002", 'https://www.linkedin.com/in/tarang-shivraj-jaiswal-ab1069224/', 'I am currently pursuing B.Tech in Information Technology from Manipal University Jaipur'

code = f"def about_me():\n\tname, age = {name}, {age}\n\tskills = {skills}\n\tprint('{muj}')\n\tdate_of_birth = {dob}\n\tgithub = 'https://github.com/tarangshivraj'\n\tlinkedin = {linkedin}\n\temail = {email}\n\tphone = +91 8858923521\n\nabout_me()"

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

def app():
	st.balloons()
	# col1, col2, col3 = st.columns(3)
	# with col1:
	# 	st.write("")
	# with col2:
	st.image(Image.open('TarangOfficial1.jpeg'))
	# with col3:
	# 	st.write("")
	st.title("About Me")
	# Spawn a new Ace editor
	content = st_ace(value=code)
	# Display editor's content as you type
	content
	st.header("Technologies I am familiar with")
	# ------------------ Full Stack
	# Frontend
	st.header("Frontend")
	html, css, js, bootstrap = st.columns(4)  
	with html:
		st.image(Image.open('icons8-html-5-48.png'), caption='HTML5')
	with css:
		st.image(Image.open('icons8-css3-48.png'), caption='CSS3')
	with js:
		st.image(Image.open('icons8-javascript-is-a-high-level,-interpreted-programming-language-48.png'), caption='JavaScript')
	with bootstrap:
		st.image(Image.open('icons8-bootstrap-48.png'), caption='Bootstrap5')
	# with react:
	# 	st.image(Image.open('icons8-react-a-javascript-library-for-building-user-interfaces-48.png'), caption='ReactJS')
	# with tailwindcss:
	# 	st.image(Image.open('tailwind-css-icon.png'), caption='TailwindCSS', width=48)
	# with vue:
	# 	st.image(Image.open('icons8-vue-js-48.png'), caption='VueJS')
	# Backend
	# st.header("Backend")
	# nodejs, flask = st.columns(2)
	# with nodejs:
	# 	st.image(Image.open('icons8-nodejs-48.png'), caption='NodeJS')
	# with flask:
	# 	st.image(Image.open('flask-icon.png'), caption='Flask', width=48)
		# st.markdown("""![NodeJS](node-brands.svg)""", unsafe_allow_html=True)
	# database
	# st.header("Databases")
	# mongodb, firebase, mysql, sqlite, graphql = st.columns(5)
	# with mongodb:
	# 	st.image(Image.open('icons8-mongodb-48.png'), caption='MongoDB')
	# with firebase:
	# 	st.image(Image.open('icons8-firebase-48.png'), caption='Firebase')
	# with mysql:
	# 	st.image(Image.open('icons8-mysql-logo-48.png'), caption='MySQL')
	# with sqlite:
	# 	st.image(Image.open('sqlite-icon.png'), caption='SQLite3', width=48)
	# with graphql:
	# 	st.image(Image.open('icons8-graphql-48.png'), caption='GraphQL')
	# ------------------ Computer Vision
	st.header("Computer Vision")
	opencv, tensorflow, mediapipe = st.columns(3)
	with opencv:
		st.image(Image.open('icons8-opencv-48.png'), caption='OpenCV')
	with tensorflow:
		st.image(Image.open('icons8-tensorflow-48.png'), caption='Tensorflow')
	with mediapipe:
		st.image(Image.open('mediapipe.png'), caption='Mediapipe', width=48)

	st.header("Machine Learning")
	# ------------------ Machine Learning
	sklearn, matplotlib, numpy, pandas = st.columns(4)
	with sklearn:
		st.image(Image.open('sklearn.png'), caption='Scikit-Learn', width=48)
	with matplotlib:
		st.image(Image.open('matplotlib.png'), caption='Matplotlib', width=48)
	with numpy:
		st.image(Image.open('icons8-numpy-48.png'), caption='NumPy')
	with pandas:
		st.image(Image.open('pandas.png'), caption='Pandas', width=48)
	# ------------------ Programming Languages
	st.header("Software Development")
	java, python, js6 = st.columns(3)
	with java:
		st.image(Image.open('icons8-java-50.png'), caption='Java', width=48)
	with python:
		st.image(Image.open('icons8-python-48.png'), caption='Python')
	# with c_plus_plus:
	# 	st.image(Image.open('icons8-c++-48.png'), caption='C++')
	with js6:
		st.image(Image.open('icons8-javascript-is-a-high-level,-interpreted-programming-language-48.png'), caption='JavaScipt')

	# ------------------ Extras
	# flutter, socketio = st.columns(2)
	# with flutter:
	# 	st.header("Flutter Mobile Application Development")
	# 	st.image(Image.open('icons8-flutter-48.png'), caption='Flutter')
	# with socketio:
	# 	st.header("Web Socket")
	# 	st.image(Image.open('Socket-io.png'), caption='Socket.io', width=48)

	st.header("Contact Me")
	columnone, columntwo, columnfour = st.columns(3)
	with columnone:
		st.image(Image.open('icons8-gmail-48.png'))
		st.write("tarangshivraj@gmail.com")
	with columntwo: 
		st.image(Image.open('icons8-linkedin-96.png'), width=48)
		st.write("[Tarang Shivraj Jaiswal](https://www.linkedin.com/in/tarang-shivraj-jaiswal-ab1069224/)")
	# with columnthree:
	# 	st.image(Image.open('icons8-twitter-48.png'))
	# 	st.write("[@sayonsaidutta](https://twitter.com/sayonsaidutta)")
	with columnfour: 
		st.image(Image.open('icons8-instagram-50.png'), width=48)
		st.write("[@tarango.saurus](https://www.instagram.com/tarango.saurus/)")
	# form = st.form("my_form")
	# name, email, message = form.text_input('May I know your name'), form.text_input('May I know your email'), form.text_area('Your message for me')
	# feedback = form.slider('How much did you like my portfolio?')
	# submitted = form.form_submit_button("Submit")
	# if submitted:
	# 	pass




	


