import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
with open("C:/Users/sakth/ss.pkl","rb")as file:
    ss=pickle.load(file)
with open("C:/Users/sakth/model.pkl","rb") as file:
    model=pickle.load(file)
with open("C:/Users/sakth/kidneymodel.pkl","rb")as file:
    kidneymodel=pickle.load(file)
with open("C:/Users/sakth/livermodel2.pkl","rb")as file:
    livermodel1=pickle.load(file)
with  st.sidebar:
    selection=option_menu('MultipleDiseasePrediction',['Home','LiverPredict','KidneyPrediction','ParkinsonsPredict'],
                          menu_icon="hospital_fill",
                          icons=['house','activity','heart','cloud'],
                          default_index=0)
if selection=='Home':
    st.markdown("""
            <style>

                .stApp {
                    background-color:   #4FB5D6;  
                }


            </style>
        """, unsafe_allow_html=True)

    st.title("Hello Teammates I am kannan")
    st.markdown("""
    :moon:
    ## Description :

    """)
    st.title("Multiple Disease Prediction")

    st.markdown("""
    ### PROBLEMSTATEMENT:
    ### OBJECTIVE:
    To build a scalable and accurate system that:
    Assists in early detection of diseases.
    Improves decision-making for healthcare providers.
    Reduces diagnostic time and cost by providing quick predictions.
    ### MENTOR :
    ### Mrs.GOMATHI ,Mrs.SHADIYA.
    ### Mrs.NEHLATH HARMAIN,Mr.ASVIN

    """)
    st.balloons()
    st.success("ONCE AGAIN THANKYOU GUVI")


elif selection=="ParkinsonsPredict":
    st.markdown("""
        <style>

            .stApp {
                background-color:  #90EE90;  
            }


        </style>
    """, unsafe_allow_html=True)
    st.title("Parkinsons_Predict")
    col1,col2=st.columns(2)
    with col1:
        HNR=st.number_input('HNR')
        MDVP_Fo_Hz=st.number_input('MDVP_Fo_Hz')
        MDVP_Fhi_Hz=st.number_input('MDVP_Fhi_Hz')
        MDVP_Flo_Hz=st.number_input('MDVP_Flo_Hz')
        MDVP_Jitter=st.number_input('MDVP_Jitter')
        MDVP_Shimmer=st.number_input('MDVP_Shimmer')
        NHR=st.number_input('NHR')
        RPDE=st.number_input('RPDE')
        DFA=st.number_input('DFA')
    with col2:
        D2	=st.number_input('D2')
        PPE	=st.number_input('PPE')
        spread1=st.number_input('spread1')
        spread2 = st.number_input('spread2')
        MDVP_RAP=st.number_input('MDVP_RAP')
        MDVP_PPQ=st.number_input('MDVP_PPQ')
        Shimmer_DDA	=st.number_input('Shimmer_DDA')
        MDVP_Jitter_Abs=st.number_input('MDVP_Jitter_Abs')
    data=(MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter,
       MDVP_Shimmer, NHR, HNR, RPDE, DFA, D2, PPE, spread1,
       spread2, MDVP_RAP, MDVP_PPQ, Shimmer_DDA, MDVP_Jitter_Abs)
    if data and st.button('PREDICT'):
        input_data = np.array(data).reshape(1, -1)
        prediction = model.predict(ss.transform(input_data))
        if prediction[0] == 1:
            st.error("Parkinson_is_caused")
        else:
            st.success("Parkinsons_is_not_caused")
elif selection=="KidneyPrediction":
    st.markdown("""
        <style>

            .stApp {
                background-color:  #FFB6C1;  
            }


        </style>
    """, unsafe_allow_html=True)
    st.title("kidney_Prediction")
    st.snow()
    col1,col2=st.columns(2)
    with col1:
        age=st.number_input("Age")
        blood_pressure=st.number_input("BloodPressure")
        specificGravity=st.number_input("SpecificGravity")
        aluminum=st.number_input("Aluminum")
        sugar=st.number_input("Sugar")
        redblood=st.number_input("Redblood")
        pucells=st.number_input("pucells")
        bloodureanitrogen=st.number_input("BloodUreaNitrogen")
        serumcrestine=st.number_input("SerumCrestine")
    with col2:
         sodium=st.number_input("sodium")
         potassium=st.number_input("potassium")
         hemoglobin=st.number_input("Hemoglobin")
         packedcellvolumne=st.number_input("Packedcellvolumne")
         whitebloodcellscount=st.number_input("Whitebloodcellscount")
         hypertension=st.number_input("hypertension")
         appetite=st.number_input(" appetite")
    data1=(age, blood_pressure, specificGravity, aluminum, sugar,
       redblood, pucells, bloodureanitrogen, serumcrestine, sodium,
       potassium, hemoglobin, packedcellvolumne, whitebloodcellscount,
       hypertension, appetite)
    if data1 and st.button('PREDICT'):
        inputdata = np.array(data1).reshape(1, -1)
        prediction = kidneymodel.predict((inputdata))
        if prediction[0] == 'ckd':
            st.error("Chronic_Kidney_is_caused")
        else:
            st.success("Not_Chronic_Kidney_is_caused")
elif selection=="LiverPredict":
    st.title("LiverPredict")
    st.balloons()
    st.markdown("""
            <style>

                .stApp {
                    background-color:  #ADD8E6;  
                }


            </style>
        """, unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col1:
        Age = st.number_input("Age")
        Total_Bilirubin=st.number_input("Total_Bilirubin")
        Direct_Bilirubin=st.number_input("Direct_Bilirubin")
        Alkaline_Phosphotase=st.number_input("Alkaline_Phosphotase")
        Alamine_Aminotransferase=st.number_input("Alamine_Aminotransferase")
    with col2:
        Aspartate_Aminotransferase=st.number_input("Aspartate_Aminotransferase")
        Total_Protiens=st.number_input("Total_Protiens")
        Albumin=st.number_input("Albumin")
        Albumin_and_Globulin_Ratio=st.number_input("Albumin_and_Globulin_Ratio")

    data2=(Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
       Alamine_Aminotransferase, Aspartate_Aminotransferase,
       Total_Protiens, Albumin, Albumin_and_Globulin_Ratio)
    if data2 and st.button("PREDICT"):
        inputdata = np.array(data2).reshape(1, -1)
        prediction = livermodel1.predict((inputdata))
        if prediction[0] == 1:
            st.error("liver_is_caused")
        else:
            st.success("Not_liver_is_caused")

