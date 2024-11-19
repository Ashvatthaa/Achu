import streamlit as st
import random

# Set the title of the app
st.title("Number Guessing Game")

# Initialize session state to store the random number and attempts
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0

# Get user input (a guess)
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

# Button to submit the guess
if st.button('Submit Guess'):
    st.session_state.attempts += 1  # Increment the attempts
    # Check if the guess is correct
    if guess < st.session_state.number_to_guess:
        st.write("Your guess is too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Your guess is too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the correct number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        # Reset the game after guessing correctly
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0
            st.write("Game reset! Try again.")

# Show the number of attempts
if st.session_state.attempts > 0 and guess != st.session_state.number_to_guess:
    st.write(f"Attempts so far: {st.session_state.attempts}")
