import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
import plotly.express as px




def create_connection():
    mydb =mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="",
        database="DS_project_1",
        autocommit = True)
    
    mycursor=mydb.cursor(buffered=True)
    return mydb 

st.set_page_config(page_title="Police Check Data")

st.sidebar.title("POLOCE CHECK DATA ANALYSYS")
page=st.sidebar.radio('Visit',["Home", "Project Explanation", "Police Check Data Analysis", "SQL Queries", "Predict Outcome and Violation Log", "Developer Info"])


   # page1 -  Home 

if page == "Home":
    
    st.header("Home")
    st.markdown(" ## Mini project 1:  ")
    st.markdown(" ### Title - Secure Check: A Python-SQL Digital Ledger for Police Post Logs")
    st.image("data:image/jpeg;base64,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")





  # page2 -  Project Explanation 

elif page == "Project Explanation":
    st.header("Project Explanation")
    st.image("data:image/jpeg;base64,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", width=300)
    st.write(""" **Problem Statement:** Police check posts require a centralized system 
             for logging, tracking, and analyzing vehicle movements. 
             Currently, manual logging and inefficient databases slow down security processes.  """)
    
    st.write(" **AIM:**  The main aim of this project is to build an SQL-based check post database with a Python-powered dashboard for real-time insights and alerts.")
    
    st.subheader("Dataset")
    df=pd.read_csv("F:\police project\cleaned_traffic_stops.csv") 
    st.dataframe(df)

   # page3 -  Police Check Data Analysis 

elif page == "Police Check Data Analysis":
    st.header("Police Check Data Analysis")

    st.subheader("🔎 Filters")
          
    df=pd.read_csv("F:\police project\cleaned_traffic_stops.csv") 
    vehicle_input = st.text_input("🔍 Enter vehicle number:")

    if vehicle_input:
        matching_vehicles = df[df['vehicle_number'].str.contains(vehicle_input, case=False)]

        if not matching_vehicles.empty:
           selected_vehicle = st.selectbox("Select vehicle number from matches:", matching_vehicles['vehicle_number'].unique())
           vehicle_data = df[df['vehicle_number'] == selected_vehicle]

           st.subheader("📊 Vehicle Stop Metrics")

           col1, col2, col3, col4 = st.columns(4)

           with col1:
             st.metric("Total Stops", value=len(vehicle_data))

           with col2:
            st.metric("Arrests", value=vehicle_data['is_arrested'].sum())

           with col3:
            st.metric("Drug-Related Stops", value=vehicle_data['drugs_related_stop'].sum())

           with col4:
            st.metric("Unique Violations", value=vehicle_data['violation'].nunique())

           with st.expander("🔎 View Stop Details"):
            st.dataframe(vehicle_data.reset_index(drop=True))

        else:
                 st.warning("No matching vehicle numbers found.")
    else:
      st.info("Please enter a vehicle number to begin search.")

    
    selected_country = st.selectbox("Select Country", ["All"] + sorted(df['country_name'].dropna().unique().tolist()))
     
    df['stop_date'] = pd.to_datetime(df['stop_date'], format="%Y-%m-%d")
    start_date = df['stop_date'].min().date()
    end_date = df['stop_date'].max().date()

    date_range = st.date_input("Select Date Range", [start_date, end_date])

    filtered_df = df.copy()
    if selected_country != "All":
       filtered_df = filtered_df[filtered_df['country_name'] == selected_country]

       if date_range:
          filtered_df = filtered_df[
          (filtered_df['stop_date'] >= pd.to_datetime(date_range[0])) &
          (filtered_df['stop_date'] <= pd.to_datetime(date_range[1]))
           ]

          # 1. Interactive Bar Chart: Top 10 stopped vehicles
          st.subheader("🚗 Top 10 Stopped Vehicles")
          top_vehicles = filtered_df['vehicle_number'].value_counts().head(10).reset_index()
          top_vehicles.columns = ['vehicle_number', 'stop_count']
          fig_bar = px.bar(top_vehicles, x='vehicle_number', y='stop_count', title='Top 10 Most Stopped Vehicles')
          st.plotly_chart(fig_bar)

          # 2. Interactive Pie Chart: Arrests
          st.subheader("🚨 Arrest Distribution")
          arrest_counts = filtered_df['is_arrested'].value_counts().rename({0: "Not Arrested", 1: "Arrested"}).reset_index()
          arrest_counts.columns = ['Arrest Status', 'Count']
          fig_pie = px.pie(arrest_counts, names='Arrest Status', values='Count', title='Arrest Distribution')
          st.plotly_chart(fig_pie)


    
    tab1, tab2,tab3,tab4= st.tabs(["driver_race","violation","stop_outcome","driver_gender"])

    
    with tab1:
     if not df.empty and 'driver_race' in df.columns:
          driver_race_df=df['driver_race'].value_counts().reset_index()
          driver_race_df.columns=['driver_race','count']
          fig=px.pie(driver_race_df,names='driver_race',values='count', title='driver_race',color='driver_race')
          st.plotly_chart(fig,use_container_width=True)
     else:
          st.warning("No data available")
    with tab2:
     if not df.empty and 'violation' in df.columns:
          violation_df=df['violation'].value_counts().reset_index()
          violation_df.columns=['violation','count']
          fig=px.bar(violation_df,x='violation',y='count', title='stops by violation',color='violation')
          st.plotly_chart(fig,use_container_width=True)
     else:
          st.warning("No data available")
    with tab3:
     if not df.empty and 'stop_outcome' in df.columns:
          stop_outcome_df=df['stop_outcome'].value_counts().reset_index()
          stop_outcome_df.columns=['stop_outcome','count']
          fig=px.bar(stop_outcome_df,x='stop_outcome',y='count', title='stops by stop_outcome',color='stop_outcome')
          st.plotly_chart(fig,use_container_width=True)
     else:
          st.warning("No data available")
    with tab4:
     if not df.empty and 'driver_gender' in df.columns:
          driver_gender_df=df['driver_gender'].value_counts().reset_index()
          driver_gender_df.columns=['driver_gender','count']
          fig=px.pie(driver_gender_df,names='driver_gender',values='count', title='driver_gender',color='driver_gender')
          st.plotly_chart(fig,use_container_width=True)
     else:
          st.warning("No data available")


    if 'country_name' in df.columns and 'driver_age' in df.columns:
       fig = px.box(
        df,
        x='country_name',
        y='driver_age',
        title='Distribution of Driver Age by Country',
        color='country_name',
        points='all'  # shows all individual data points
        )
       st.plotly_chart(fig, use_container_width=True)
    else:
     st.warning("Required columns not found in dataset.")





 
  # page4 -  SQL Queries 
 
elif page == "SQL Queries":
    st.header("SQL Queries")
    st.subheader("Medium level:")
    queries={
       "1. Total Number of Police Stops": "SELECT count(*) AS No_of_Police_stops FROM police_check_data",
       "2. Count of Stops by Violation Type": "SELECT Violation, COUNT(*) AS Violation_stops FROM police_check_data GROUP BY Violation ORDER BY Violation_stops DESC",
       "3. Number of Arrests vs. Warnings ":"SELECT stop_outcome,COUNT(*) AS Count FROM police_check_data WHERE stop_outcome IN ('Arrest', 'Warning') GROUP BY stop_outcome ORDER BY count DESC ",
       "4. Average Age of Drivers Stopped ":"SELECT AVG(driver_age) AS Avg_driver_age  FROM police_check_data ",
       "5. Top 5 Most Frequent Search Types ":"SELECT  search_type, COUNT(*) AS count   FROM police_check_data GROUP BY search_type ORDER BY count DESC LIMIT 5 ",
       "6. Count of Stops by Gender ":"SELECT  driver_gender AS gender, COUNT(*) AS stop_count   FROM police_check_data GROUP BY driver_gender ",
       "7. Most Common Violation for Arrests ":"SELECT  Violation, COUNT(*) AS arrest_count   FROM police_check_data WHERE is_arrested=TRUE GROUP BY Violation  ORDER BY arrest_count DESC LIMIT 1 ",
       "8. Average Stop Duration for Each Violation ":"""SELECT  Violation, AVG( CASE 
                                                        WHEN stop_duration = '0-15 Min' THEN 7.5
                                                        WHEN stop_duration = '16-30 Min' THEN 23
                                                        WHEN stop_duration = '30+ Min' THEN 35
                                                        ELSE NULL
                                                        END) AS avg_stop_duration   FROM police_check_data GROUP BY Violation""",
       "9. Number of Drug-Related Stops by Year ":"SELECT  YEAR(stop_date) AS stop_year, COUNT(*) AS drugs_related_stop_counts  FROM police_check_data WHERE drugs_related_stop=TRUE GROUP BY stop_year  ORDER BY stop_year ",
       "10. Drivers with the Highest Number of Stops ":"SELECT  vehicle_number, COUNT(*) AS drivers_stops  FROM police_check_data GROUP BY vehicle_number  ORDER BY drivers_stops DESC LIMIT 5 ",
       "11. Number of Stops Conducted at Night (Between 10 PM - 5 AM) ":"SELECT   COUNT(*) AS stops_at_night  FROM police_check_data WHERE TIME(stop_time)>= '22:00:00' OR TIME(stop_time) <= '05:00:00' ",
       "12. Number of Searches Conducted by Violation Type ":"SELECT violation,  COUNT(*) AS count_of_searches  FROM police_check_data WHERE search_conducted=TRUE GROUP BY violation ORDER BY count_of_searches DESC ",
       "13. Arrest Rate by Driver Gender ":"SELECT driver_gender,  ROUND(SUM(CASE WHEN is_arrested = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS arrest_rate  FROM police_check_data  GROUP BY driver_gender ",
       "14. Violation Trends Over Time (Monthly Count of Violations) ":"SELECT violation,  MONTH(stop_date) AS month,  COUNT(*)  AS counts  FROM police_check_data  GROUP BY MONTH(stop_date), violation ORDER BY counts DESC ",
       "15. Most Common Stop Outcomes for Drug-Related Stops":"SELECT stop_outcome,  COUNT(*)  AS counts  FROM police_check_data WHERE drugs_related_stop=TRUE GROUP BY stop_outcome ORDER BY counts DESC ", 
    }

    selected_query_list = st.selectbox("Choose a query", list(queries.keys()))
    selected_query=queries[selected_query_list]

    if st.button("Run Query",  key="run_query_button_1"):
        conn=create_connection()
        mycursor=conn.cursor(buffered=True)

        
        mycursor.execute(selected_query)
        data=mycursor.fetchall()
        columns=[i[0] for i in mycursor.description]

        query_result=pd.DataFrame(data,columns=columns)

        st.write("### Query Result:")
        st.dataframe(query_result)

        mycursor.close()
        conn.close()


    st.subheader("Complex level:")
    queries={
     "1. Yearly Breakdown of Stops and Arrests by Country (Using Subquery and Window Functions)":"""SELECT year, country_name, total_stops, arrest_count 
                 FROM (SELECT country_name,YEAR(stop_date) AS year, 
                 COUNT(*) OVER (PARTITION BY YEAR(stop_date), country_name) AS total_stops, 
                 SUM(CASE WHEN is_arrested = TRUE THEN 1 ELSE 0 END)
                  OVER (PARTITION BY YEAR(stop_date), country_name) AS arrest_count 
                  FROM police_check_data) AS sub
                  GROUP BY year, country_name, total_stops, arrest_count
                 ORDER BY year, country_name """,
     "2. Driver Violation Trends Based on Age and Race (Join with Subquery)":"SELECT violation, sub.age, sub.race,   COUNT(*)  AS counts  FROM (SELECT  violation, driver_age AS age, driver_race AS race FROM police_check_data ) AS sub  GROUP BY violation,  sub.age, sub.race ORDER BY counts DESC",
     "3. Time Period Analysis of Stops (Joining with Date Functions)":"""SELECT YEAR(STR_TO_DATE(stop_date, '%Y-%m-%d')) AS year, 
                 MONTH(STR_TO_DATE(stop_date, '%Y-%m-%d')) AS month,
                 DAYNAME(STR_TO_DATE(stop_date, '%Y-%m-%d')) AS weekday, 
                 HOUR(STR_TO_DATE(stop_time, '%H:%i')) AS hour, COUNT(*)  AS stop_counts  FROM police_check_data 
                 GROUP BY  year, month, weekday, hour ORDER BY year, month, weekday, hour""",
     " 4. Correlation Between Age, Violation, and Stop Duration (Subquery)":"""SELECT 
                 violation, 
                 driver_age_group,
                 ROUND(AVG(stop_duration_minutes), 2) AS avg_stop_duration,                  
                 COUNT(*)  AS counts 
                FROM 
                 (SELECT CASE WHEN driver_age < 18 THEN '<18'
                WHEN driver_age BETWEEN 18 AND 25 THEN '18-25'
                WHEN driver_age BETWEEN 26 AND 40 THEN '26-40'
                WHEN driver_age BETWEEN 41 AND 60 THEN '41-60'
                ELSE '60+'
                END AS driver_age_group,
                violation,
                CASE stop_duration
                WHEN '0-15 Min' THEN 10
                WHEN '16-30 Min' THEN 23
                WHEN '30+ Min' THEN 35
                ELSE NULL
                END AS stop_duration_minutes  FROM police_check_data) AS sub
                GROUP BY violation, driver_age_group ORDER BY counts DESC  """,
     "5. Violations with High Search and Arrest Rates (Window Function)":"""SELECT violation, search_type, ROUND(AVG(search_conducted)*100, 2) AS search_rate, 
                 ROUND(AVG(is_arrested)*100, 2) AS arrest_rate, RANK() OVER (ORDER BY AVG(search_conducted) DESC) AS search_rank,
                 RANK() OVER (ORDER BY AVG(is_arrested) DESC) AS arrest_rank,  COUNT(*)  AS counts  FROM police_check_data GROUP BY violation, search_type ORDER BY search_rank""",
     "6. Driver Demographics by Country (Age, Gender, and Race)":"""SELECT country_name,  driver_gender, ROUND(AVG(driver_age), 1) AS avg_age,
                 driver_race, COUNT(*)  AS counts  FROM police_check_data  GROUP BY country_name, driver_gender, driver_race ORDER BY country_name, counts DESC""",
     "7.Top 5 Violations with Highest Arrest Rates": """SELECT violation, ROUND(SUM(CASE WHEN is_arrested = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS arrest_rate,
                 COUNT(*)  AS police_stops  FROM police_check_data  GROUP BY violation ORDER BY arrest_rate DESC LIMIT 5""",
       }

    selected_query_list = st.selectbox("Choose a query", list(queries.keys()))
    selected_query=queries[selected_query_list]

    if st.button("Run Query", key="run_query_button_2"):
        conn=create_connection()
        mycursor=conn.cursor(buffered=True)

        
        mycursor.execute(selected_query)
        data=mycursor.fetchall()
        columns=[i[0] for i in mycursor.description]

        query_result=pd.DataFrame(data,columns=columns)

        st.write("### Query Result:")
        st.dataframe(query_result)

        mycursor.close()
        conn.close()


 
     # page5 -  Predict Outcome and Violation Log
elif page == "Predict Outcome and Violation Log":
  st.header("Predict Outcome and Violation Log")
    
  with st.form("new_post_log_form"):
   
    stop_date=st.date_input('Stop date', value=datetime.date.today())
    stop_time = st.time_input("Select a time", value=datetime.time(9, 0), step=datetime.timedelta(minutes=1))
    country_name=st.selectbox("Country name",['Canada', 'India', 'USA'])
    driver_gender=st.selectbox("Driver gender",['Male', 'Female'])
    driver_age=st.number_input("Driver age", min_value=18, max_value=80, step=1)
    driver_race=st.selectbox("Driver race",['Asian', 'Other', 'Black', 'White', 'Hispanic'])
    violation=st.selectbox("Violation",['Speeding', 'Other', 'DUI', 'Seatbelt', 'Signal'])
    search_type=st.selectbox("Search type",['Vehicle Search', 'Frisk'])
    search_conducted=st.selectbox("Was a search conducted",['1', '0'])
    stop_outcome=st.selectbox("Stop outcome",['Ticket', 'Arrest', 'Warning'])
    drugs_related_stop=st.selectbox("Was a drugs related",['1', '0'])
    stop_duration=st.selectbox("Stop duration",['16-30 Min', '0-15 Min', '30+ Min'])
    vehicle_number=st.text_input("Vehicle number")

  
    timestamp=pd.Timestamp.now()

    submitted=st.form_submit_button("Predict stop outcome and violation")
    df = pd.read_csv("F:\police project\cleaned_traffic_stops.csv")


    if submitted:
        filtered_data = df[
            (df['driver_gender'] == driver_gender) &
            (df['driver_age'] == driver_age) &
            (df['search_conducted'] == int(search_conducted)) &
            (df['stop_duration'] == stop_duration) &
            (df['drugs_related_stop'] == int(drugs_related_stop)) 
        ]
        if not filtered_data.empty:
            predicted_outcome=filtered_data['stop_outcome'].mode()[0]
            predicted_violation=filtered_data['violation'].mode()[0]
        else:
            predicted_outcome="warning"
            predicted_violation="speeding"

        search_text="A search was conducted" if int(search_conducted) else "No search was conducted"
        drug_text="was drug_related" if int(drugs_related_stop) else "was not drug-related"

        st.markdown(f""" 
                 🧠 Prediction summary 
                    
                🔍predicted stop outcome: {predicted_outcome}
                🚨predicted violation: {predicted_violation}
        
         👤 A {driver_age}-year-old {driver_gender} driver in {country_name} was 
         stopped at {stop_time.strftime('%I:%M %p')} on {stop_date}.
         🔎 {search_text}, and 💊 the stop {drug_text}.
        
        ⏱️ stop duration: {stop_duration}.
         🚗 vehicle number: {vehicle_number}.

        """)

   # page6 -  Developer Info
 
elif page == "Developer Info":
    st.header("👨‍💻Developer Info")
    st.markdown("""
    **Developed by:** B.LOGITHNATHAN 

    **Course:** Data Science                        
    **Skills:** Python, Pandas, MySQL, Data Analysis, Streamlit""", True)

    st.snow()
