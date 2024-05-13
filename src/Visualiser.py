import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    OUTPUT_DIR = "../C2C-2024-DataSet/DataSets/example-set/"
    client_report = pd.read_csv(OUTPUT_DIR + "output_client_report.csv")
    exchange_report = pd.read_csv(OUTPUT_DIR + "output_exchange_report.csv")
    instrument_report = pd.read_csv(OUTPUT_DIR + "output_instrument_report.csv")
    return client_report, exchange_report, instrument_report


st.title("End of Day Statistics")
load_state = st.text("Loading Reports...")
data = get_data()
load_state.text("Done loading Reports!")

cr, er, ir = get_data()

st.dataframe(cr)
st.dataframe(er)
st.dataframe(ir)

