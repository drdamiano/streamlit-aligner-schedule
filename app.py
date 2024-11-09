import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from io import BytesIO

# Funkcja do generowania zrzutu ekranu harmonogramu
def generate_image(schedule_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    ax.axis('tight')
    
    # Rysowanie tabeli z harmonogramem na obrazie
    ax.table(cellText=schedule_df.values, colLabels=schedule_df.columns, cellLoc='center', loc='center')
    
    # Zapisywanie tabeli jako obraz w pamięci
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close(fig)
    return buf

# Wyświetlenie logo na środku
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/drdamiano/streamlit-aligner-schedule/main/logo.PNG' width=200>
    </div>
    """, unsafe_allow_html=True)

# Stylizowane linki do strony i Instagrama z nowymi kolorami
st.markdown("""
    <style>
        .link-button {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 5px;
            border: 2px solid black;
            border-radius: 8px;
            background-color: black;
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
        }
        .link-button:hover {
            background-color: #333333;
        }
    </style>
    <div style="text-align: center;">
        <a href="https://drnowacki.pl" class="link-button" target="_blank">drnowacki.pl</a>
        <a href="https://instagram.com/drnowacki" class="link-button" target="_blank">Instagram</a>
    </div>
    """, unsafe_allow_html=True)

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

    # Przycisk do pobrania harmonogramu jako CSV
    csv = schedule_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Pobierz harmonogram jako CSV",
        data=csv,
        file_name='harmonogram_nakładek.csv',
        mime='text/csv',
    )

    # Generowanie obrazu tabeli
    img_buffer = generate_image(schedule_df)
    st.image(img_buffer, caption="Harmonogram jako obraz")

    # Przycisk do pobrania obrazu
    st.download_button(
        label="Pobierz harmonogram jako obraz PNG",
        data=img_buffer,
        file_name="harmonogram_nakładek.png",
        mime="image/png"
    )
