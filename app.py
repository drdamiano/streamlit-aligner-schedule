{\rtf1\ansi\ansicpg1250\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
from datetime import datetime, timedelta\
\
# Nag\uc0\u322 \'f3wek aplikacji\
st.title("Harmonogram Noszenia Nak\uc0\u322 adek")\
\
# Formularz dla pacjenta\
start_date = st.date_input("Wybierz dat\uc0\u281  rozpocz\u281 cia", datetime.now().date())\
start_aligner = st.number_input("Podaj numer pocz\uc0\u261 tkowej nak\u322 adki", min_value=1, step=1)\
days_per_aligner = st.number_input("Liczba dni noszenia jednej nak\uc0\u322 adki", min_value=1, step=1)\
\
# Przycisk do wygenerowania harmonogramu\
if st.button("Generuj harmonogram"):\
    # Generowanie harmonogramu\
    schedule = []\
    current_date = start_date\
    current_aligner = start_aligner\
\
    # Zak\uc0\u322 adamy, \u380 e b\u281 dzie maksymalnie 20 nak\u322 adek (mo\u380 na dostosowa\u263 )\
    for i in range(20):\
        schedule.append(\{\
            "Nak\uc0\u322 adka": current_aligner,\
            "Data rozpocz\uc0\u281 cia": current_date,\
            "Data zako\uc0\u324 czenia": current_date + timedelta(days=days_per_aligner - 1)\
        \})\
        current_date += timedelta(days=days_per_aligner)\
        current_aligner += 1\
\
    # Tworzenie tabeli z harmonogramem\
    schedule_df = pd.DataFrame(schedule)\
    st.write("### Harmonogram noszenia nak\uc0\u322 adek")\
    st.dataframe(schedule_df)\
\
    # Przycisk do pobrania harmonogramu\
    csv = schedule_df.to_csv(index=False).encode('utf-8')\
    st.download_button(\
        label="Pobierz harmonogram jako CSV",\
        data=csv,\
        file_name='harmonogram_nak\uc0\u322 adek.csv',\
        mime='text/csv',\
    )\
}