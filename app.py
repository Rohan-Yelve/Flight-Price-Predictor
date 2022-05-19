import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn
from PIL import Image

image = Image.open('plane.png')
model = pickle.load(open('model.pkl','rb'))

st.image(image,width=300)
st.title('Flight Price Predictor')

dep_date = st.date_input('Departure Date')
Journey_day = int(pd.to_datetime(dep_date,format="%Y-%m-%d").day)
Journey_month = int(pd.to_datetime(dep_date,format="%Y-%m-%d").month)

source = st.selectbox('Source',['Delhi','Kolkata','Banglore','Mumbai','Chennai'])

destination = st.selectbox('Destination',['Cochin','Banglore','Delhi','New Delhi','Hyderabad','Kolkata'])

total_stops = st.selectbox('Total Stop',['Non-Stop','1 Stop','2 Stops','3 Stops','4 Stops'])

airline = st.selectbox('Airline',['IndiGo','Air India','Jet Airways','SpiceJet','Multiple carriers',
'GoAir','Vistara','Air Asia','Vistara Premium economy','Jet Airways Business',
'Multiple carriers Premium economy','Trujet'])


if st.button('Predict Price'):
    if total_stops == 'Non-Stop':
        Total_Stops = 0
    elif total_stops == '1 Stop':
        Total_Stops = 1
    elif total_stops == '2 Stops':
        Total_Stops = 2
    elif total_stops == '3 Stops':
        Total_Stops = 3
    else:
        Total_Stops = 4

    if source == 'Chennai':
        Source_Chennai = 1
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
    elif source == 'Delhi':
        Source_Chennai = 0
        Source_Delhi = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
    elif source == 'Kolkata':
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
    elif source == 'Mumbai':
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
    else:
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0

    if destination == 'Cochin':
        Destination_Cochin = 1
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata	= 0
        Destination_NewDelhi = 0
    elif destination == 'Delhi':
        Destination_Cochin = 0
        Destination_Delhi = 1
        Destination_Hyderabad = 0
        Destination_Kolkata	= 0
        Destination_NewDelhi = 0
    elif destination == 'Hyderabad':
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 1
        Destination_Kolkata	= 0
        Destination_NewDelhi = 0
    elif destination == 'Kolkata':
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata	= 1
        Destination_NewDelhi = 0
    elif destination == 'New Delhi':
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata	= 0
        Destination_NewDelhi = 1
    else:
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata	= 0
        Destination_NewDelhi = 0

    if airline == 'Air India':
        Airline_AirIndia = 1
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'GoAir':
        Airline_AirIndia = 0
        Airline_GoAir = 1
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'IndiGo':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 1
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Jet Airways':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 1
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Jet Airways Business':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 1
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Multiple carriers':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 1
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Multiple carriers Premium economy':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 1
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'SpiceJet':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 1
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Trujet':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 1
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Vistara':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 1
        Airline_VistaraPremiumEconomy = 0
    elif airline == 'Vistara Premium economy':
        Airline_AirIndia = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0
        Airline_MultipleCarriersPremiumeconomy = 0
        Airline_SpiceJet = 0
        Airline_Trujet = 0
        Airline_Vistara = 0
        Airline_VistaraPremiumEconomy = 1


    query = np.array([[Total_Stops, Journey_day, Journey_month, Airline_AirIndia,
       Airline_GoAir, Airline_IndiGo, Airline_JetAirways,
       Airline_JetAirwaysBusiness, Airline_MultipleCarriers,
       Airline_MultipleCarriersPremiumeconomy, Airline_SpiceJet,
       Airline_Trujet, Airline_Vistara, Airline_VistaraPremiumEconomy,
       Source_Chennai, Source_Delhi, Source_Kolkata, Source_Mumbai,
       Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Destination_NewDelhi]])

    query = query.reshape(1,23)
    st.title(int(model.predict(query)))
        

