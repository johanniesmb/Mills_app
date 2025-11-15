import pandas as pd
import plotly.express as px
import streamlit as st

#set a wide layout
st.set_page_config(layout='wide')
st.title('Auto MPG Dashboard')

#read data from the excel file
df = pd.read_csv("clean_auto_mpg.csv")

#implement tabs
unique_origin = list(df['origin'].unique())
unique_origin.sort()


#list comprehention. for every item in the list the text origin will be added
unique_origin_str = ['Origin: ' + str(origin) for origin in unique_origin]

#Add Tabs (3) and pass the list coprehendsion into it.
tab1, tab2, tab3 = st.tabs([unique_origin_str[0],
                            unique_origin_str[1],
                            unique_origin_str[2]],
                           )

#using the with key to put something on the tab.
with tab1:
    # Display the text in the list comrehention Origin1,2,3
    st.subheader(unique_origin_str[0])
#ceate column and distribute the ratio sizes equaly (1,1,1,1)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
#subset data
    df_tab = df[df['origin'] == unique_origin[0]]

    avg_displacement = round(df_tab['displacement'].mean(),1)
    avg_horsepower = round(df_tab['horsepower'].mean(), 1)
    avg_weight = round(df_tab['weight'].mean(), 1)
    avg_mpg = round(df_tab['mpg'].mean(), 1)

#display data (AVG) in the col1
    col1.metric(label='Avg Displacement', value=avg_displacement)
    col2.metric(label='Avg AVG Horsepower', value=avg_horsepower)
    col3.metric(label='Avg Weight', value=avg_weight)
    col4.metric(label='Avg MPG', value=avg_mpg)

#ceate column FOR SCATTER PLOT
####################### 4, 1 ratio simply mean the size allocation to the column
    col5, col6 = st.columns([4, 1])
    scatter = px.scatter(data_frame=df_tab,
                           x='weight',
                           y='horsepower',
                           hover_name='car name',
                           color='cylinders',
                           size='weight',
                           title='Weight vs HP for cars from {}'.format(unique_origin[0])
                        )
#display scatter plot on page
col5.plotly_chart(scatter)

#Create Histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution'
                              )
#display scatter plot on page
col6.plotly_chart(histogram_plot)




with tab2:
    # Display the text in the list comrehention Origin1,2,3
    st.subheader(unique_origin_str[1])
#ceate column and distribute the ratio sizes equaly (1,1,1,1)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
#subset data
    df_tab = df[df['origin'] == unique_origin[1]]

    avg_displacement = round(df_tab['displacement'].mean(),1)
    avg_horsepower = round(df_tab['horsepower'].mean(), 1)
    avg_weight = round(df_tab['weight'].mean(), 1)
    avg_mpg = round(df_tab['mpg'].mean(), 1)

#display data (AVG) in the col1
    col1.metric(label='Avg Displacement', value=avg_displacement)
    col2.metric(label='Avg AVG Horsepower', value=avg_horsepower)
    col3.metric(label='Avg Weight', value=avg_weight)
    col4.metric(label='Avg MPG', value=avg_mpg)

#ceate column FOR SCATTER PLOT
####################### 4, 1 ratio simply mean the size allocation to the column
    col5, col6 = st.columns([4, 1])
    scatter = px.scatter(data_frame=df_tab,
                           x='weight',
                           y='horsepower',
                           hover_name='car name',
                           color='cylinders',
                           size='weight',
                           title='Weight vs HP for cars from {}'.format(unique_origin[1])
                        )
#display scatter plot on page
col5.plotly_chart(scatter)

#Create Histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution'
                              )
#display scatter plot on page
col6.plotly_chart(histogram_plot)

with tab3:
    # ceate column and distribute the ratio sizes equaly (1,1,1,1)
    # Display the text in the list comrehention Origin1,2,3
    st.subheader(unique_origin_str[2])
    # ceate column
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    # subset data
    df_tab = df[df['origin'] == unique_origin[2]]

    avg_displacement = round(df_tab['displacement'].mean(), 1)
    avg_horsepower = round(df_tab['horsepower'].mean(), 1)
    avg_weight = round(df_tab['weight'].mean(), 1)
    avg_mpg = round(df_tab['mpg'].mean(), 1)

    # display data (AVG) in the col1
    col1.metric(label='Avg Displacement', value=avg_displacement)
    col2.metric(label='Avg AVG Horsepower', value=avg_horsepower)
    col3.metric(label='Avg Weight', value=avg_weight)
    col4.metric(label='Avg MPG', value=avg_mpg)

    # ceate column FOR SCATTER PLOT
    ####################### 4, 1 ratio simply mean the size allocation to the column
    col5, col6 = st.columns([4, 1])
    scatter = px.scatter(data_frame=df_tab,
                         x='weight',
                         y='horsepower',
                         hover_name='car name',
                         color='cylinders',
                         size='weight',
                         title='Weight vs HP for cars from {}'.format(unique_origin[2])
                         )
# display scatter plot on page
col5.plotly_chart(scatter)

# Create Histogram
histogram_plot = px.histogram(data_frame=df_tab,
                              x='mpg',
                              title='MPG Distribution'
                              )
# display scatter plot on page
col6.plotly_chart(histogram_plot)
