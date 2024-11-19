import streamlit as st
import random
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1,100)
    
    st.session_state.attempts = 0


st.title("User Guessing")
st.write("Guess the number I'm thinking of between 1 to 100")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)



if st.button("Submit Guess"):
    st.session_state.attempts += 1
    diff = abs(guess - st.session_state.target_number)
    st.write(diff)
    
    if guess == st.session_state.target_number:
        st.write(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.write("New game started! Try to guess the new number.")
    elif diff <= 10 or diff < 5:
        if st.session_state.target_number>guess:
            st.write("That's almost it, just a little more")

        elif guess>st.session_state.target_number:
            st.write("That's almost it, just a little less")

    elif guess > st.session_state.target_number:
        st.write("Too high! Try again.")

    elif guess < st.session_state.target_number:
        st.write("Too low! Try again.")



st.write("Attempts:",st.session_state.attempts)