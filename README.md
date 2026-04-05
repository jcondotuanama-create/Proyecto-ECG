# ECG SIGNAL PROCESSING AND HEART RATE DETECTION - my first project

# Overview

This project focuses on the processing and analysis of electrocardiogram (ECG) data. Using the MIT-BIH Long-Term ECG Database, the program developed in Python extracts raw cardiac signals and calculates heart rate (BPM) through an adaptive peak-detection algorithm. The aim was learning and having a bit of contact with biomedical engineering role.

# Tools and technologies

Electrocardiogram data from database is not legible by python, then it must be read through specific tools. Python libraries have been used to extract all data and developing all signals and information useful for nurses and doctors. Used python libraries are wfbd, numpy, matplotlib and pandas.

**WFBD** is the Python library capable of parsing ECG-data 1into a Record object. Every atribute represent every crucial data from ECG. 

**Matplotlib** gives the plots from the ECG with all data which have been extracted by wfbd python library.

**Pandas** use ECG-data to export  the processed data into a structured CSV format.

**Numpy** was used for numerical computing and implementing the statistical logic of the peak-detection algorithm.




