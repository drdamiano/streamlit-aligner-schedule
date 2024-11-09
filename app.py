import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Nagłówek aplikacji
st.title("Harmonogram Noszenia Nakładek")

# Formularz dla pacjenta
start_date = st.date_input("Wybierz datę rozpoczęcia", datetime.now().date())
start_aligner = st.number_input("Podaj numer początkowej nakładki", min_value=1, step=1)
days_per_aligner = st.number_input("Liczba dni noszenia jednej nakładki", min_value=1, step=1)

# Przycisk do wygenerowania harmonogramu
if st.button("Generuj harmonogram"):
    # Generowanie harmonogramu
    schedule = []
    current_date = start_date
    current_aligner = start_aligner

    # Zakładamy, że będzie maksymalnie 20 nakładek (można dostosować)
    for i in range(20):
        schedule.append({
            "Nakładka": current_aligner,
            "Data rozpoczęcia": current_date,
            "Data zakończenia": current_date + timedelta(days=days_per_aligner - 1)
        })
        current_date += timedelta(days=days_per_aligner)
        current_aligner += 1

    # Tworzenie tabeli z harmonogramem
    schedule_df = pd.DataFrame(schedule)
    st.write("### Harmonogram noszenia nakładek")
    st.dataframe(schedule_df)

    # Przycisk do pobrania harmonogramu
    csv = schedule_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Pobierz harmonogram jako CSV",
        data=csv,
        file_name='harmonogram_nakładek.csv',
        mime='text/csv',
    )
