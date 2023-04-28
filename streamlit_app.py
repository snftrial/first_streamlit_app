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
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries']);
#display df
streamlit.dataframe(my_fruit_list)
