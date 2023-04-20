import streamlit
import pandas
streamlit.title('Hello World')
streamlit.header('Hello')
streamlit.text('from the outside')
streamlit.text('...')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
