import streamlit
import pandas

streamlit.title('Hello World')
streamlit.header('Hello')
streamlit.text('from the outside')
streamlit.text('...')

#read in csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set index key
my_fruit_list= my_fruit_list.set_index('Fruit');

#enable select
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show=my_fruit_list.loc[fruits_selected];

#display df
streamlit.dataframe(fruits_to_show)

#New section to display api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #print data

# parse json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# show df
streamlit.dataframe(fruityvice_normalized)
