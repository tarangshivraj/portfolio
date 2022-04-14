import streamlit as st
from PIL import Image
import base64

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     # pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
# 	pdf_display = F"""<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>"""
#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

# video_file_bitquery = open('Bitquery-video.mp4', 'rb')
# video_bytes_bitquery = video_file_bitquery.read()

def app():
	st.balloons()
	st.title("Some of my work experience")
	st.header("Bitquery")
	st.write("Role: Technical Support Intern")
	# colone, coltwo = st.columns(2)
	# with colone:
	# 	st.video(video_bytes_bitquery)
	# # st.write("Role: Software Development Intern")
	# with coltwo:
	st.image(Image.open('Internship Completion Certificate Bitquery TARANG SHIVRAJ JAISWAL (1) (1)-1.png'), caption='Bitquery Internship Completion Certificate')
	# displayPDF('Internship Completion Certificate Bitquery Sayon Sai Dutta FINAL-signed.pdf')
	st.header("Good Host Spaces")
	st.write("Role: Technical Support Intern")
	# coll = st.columns(1)
	# # with col:
	# # 	st.video(video_bytes_edumee)
	# with coll:
	st.image(Image.open('Good Host Certification-1.png'), caption='Good Host Spaces Internship Completion Certificate')
	# st.header("Deloitte")
	# st.write("Role: Technical Consultancy Virtual Internship Experience")
	# st.image(Image.open('Deloitte Virtual Internship Certificate-1.png'), caption='Deloitte Technical Consultancy Virtual Internship Experience Certificate')
	# displayPDF('Deloitte Virtual Internship Certificate.pdf')