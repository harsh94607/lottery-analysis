import streamlit as st
import pandas as pd

def extract_numbers(row):
    row = row.iloc[4:10] 
    row = set(row.tolist())
    return row

def check_historical_occurrence(user_numbers, historical_numbers):
    user_numbers_set = set(user_numbers)
    
    check_occurrence = historical_numbers.apply(lambda x: x == user_numbers_set)
    n_occurrences = check_occurrence.sum()
    
    if n_occurrences == 0:
        return '''The combination {} has never occurred.
This doesn't mean it's more likely to occur now. Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, user_numbers)
    else:
        return '''The number of times combination {} has occurred in the past is {}.
Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, n_occurrences, user_numbers)

st.title("Canadian 6/49 Lottery Number Checker")

lottery_data = pd.read_csv('649.csv')

winning_numbers = lottery_data.apply(extract_numbers, axis=1)

st.header("Enter Your Lottery Numbers")

user_number1 = st.number_input("Number 1", min_value=1, max_value=49, step=1)
user_number2 = st.number_input("Number 2", min_value=1, max_value=49, step=1)
user_number3 = st.number_input("Number 3", min_value=1, max_value=49, step=1)
user_number4 = st.number_input("Number 4", min_value=1, max_value=49, step=1)
user_number5 = st.number_input("Number 5", min_value=1, max_value=49, step=1)
user_number6 = st.number_input("Number 6", min_value=1, max_value=49, step=1)

user_numbers = [user_number1, user_number2, user_number3, user_number4, user_number5, user_number6]

if st.button("Check Lottery Numbers"):
    result = check_historical_occurrence(user_numbers, winning_numbers)
    st.write(result)
