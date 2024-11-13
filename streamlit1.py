import streamlit as st
import pandas as pd
import numpy as np

def extract_numbers(row):
    row = row.iloc[4:10]
    return set(row.tolist())

def check_historical_occurrence(user_numbers, historical_numbers):
    user_numbers_set = set(user_numbers)
    historical_matches = historical_numbers.apply(lambda x: user_numbers_set == x)
    n_occurrences = historical_matches.sum()
    
    if n_occurrences == 0:
        return (False, f"The combination {user_numbers} has never occurred.\n"
                "Your chances of winning with this combination are 0.0000072%, or 1 in 13,983,816.")
    else:
        return (True, f"The number of times combination {user_numbers} has occurred in the past is {n_occurrences}.\n"
                "Your chances of winning with this combination remain 0.0000072%, or 1 in 13,983,816.")

def calculate_multiple_tickets_probability(num_tickets):
    probability = 1 - ((13983815 / 13983816) ** num_tickets)
    return probability * 100

st.title("🎟️ Canadian 6/49 Lottery Awareness Project")


lottery_data = pd.read_csv('649.csv')
st.header("Data Preview")
st.write("Here are the first five rows of the dataset:")
st.write(lottery_data.head())


winning_numbers = lottery_data.apply(extract_numbers, axis=1)


st.header("Check a Single Lottery Ticket")
user_number1 = st.number_input("Number 1", min_value=1, max_value=49, step=1, key="single1")
user_number2 = st.number_input("Number 2", min_value=1, max_value=49, step=1, key="single2")
user_number3 = st.number_input("Number 3", min_value=1, max_value=49, step=1, key="single3")
user_number4 = st.number_input("Number 4", min_value=1, max_value=49, step=1, key="single4")
user_number5 = st.number_input("Number 5", min_value=1, max_value=49, step=1, key="single5")
user_number6 = st.number_input("Number 6", min_value=1, max_value=49, step=1, key="single6")

user_numbers = sorted(set([user_number1, user_number2, user_number3, user_number4, user_number5, user_number6]))

if len(user_numbers) < 6:
    st.warning("Please enter six unique numbers.")
elif st.button("Check Single Ticket"):
    match_found, result = check_historical_occurrence(user_numbers, winning_numbers)
    if match_found:
        st.success(result)
    else:
        st.warning(result)


st.header("Multiple Tickets Probability Checker")
num_tickets = st.number_input("Enter the number of tickets you plan to buy", min_value=1, step=1, key="multi_ticket")

if st.button("Check Probability for Multiple Tickets"):
    probability = calculate_multiple_tickets_probability(num_tickets)
    st.write(f"With {num_tickets} tickets, your chance of winning is approximately {probability:.8f}%.")
    st.write("However, even with multiple tickets, the odds remain very low due to the nature of lottery probability.")


st.header("Understanding Lottery Odds")
st.write(
    """
    Lottery games are designed to generate revenue, often at the expense of players. 
    With extremely low chances of winning, regular participation can have financial drawbacks.
    
    ### Alternatives to Playing the Lottery
    - **Savings & Investments**: Saving the money you’d spend on tickets may yield better long-term benefits.
    - **Financial Education**: Learning effective financial management can lead to more security.
    - **Affordable Fun**: Look for ways to enjoy your free time without risking money on slim chances.
    """
)
