
import streamlit as st
import pandas as pd

    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "1oWMiyXeP8MlhtmiN8aUEn56tg3YFjVnP3BYkRscyiCo-cdFU"
    sheet_name = "test2"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")