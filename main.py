import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title("Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")   #upload button only accepting CSV files

if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader ("Data Summary")   #shows summary of the date such as AVG, mean STD etc
    st.write(df.describe())
#filter data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot data")
    x_column = st.selectbox("Selext x-axis column", columns)
    y_column = st.selectbox("Selext y-axis column", columns)
    
    st.text("Choose to generate a graph")
    
    left, middle, right = st.columns(3)
   
    if left.button("Generate Bar Chart") and x_column != y_column:  #Button to generate BAR CHART
        st.bar_chart(filtered_df.set_index(x_column)[y_column])

    elif x_column == y_column:      
        st.error("X and Y axis cannot be the same value")
           
    if middle.button("Generate Line Chart") and x_column != y_column:   # Button to generate LINE CHART
                st.line_chart(filtered_df.set_index(x_column)[y_column])

    if right.button("Generate Scatter Chart") and x_column != y_column:     #still recieves error if data in file not compatible for SCATTER CHART
          st.scatter_chart(df)
    
   
            
  


   
   