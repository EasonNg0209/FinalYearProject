# Either add "sudo" before all commands or use "sudo su" 
# Amazon Linux 2023

#!/bin/bash
dnf install git -y
git clone https://github.com/EasonNg0209/FinalYearProject.git
cd FinalYearProject
dnf install python-pip -y
pip3 install subprocess.run scikit-learn opencv-python numpy tk pytesseract face_recognition PyPDF2 nltk flask pymysql
python3 app.py
