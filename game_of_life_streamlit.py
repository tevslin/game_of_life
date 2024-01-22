# filename: game_of_life_streamlit.py
import streamlit as st
import numpy as np
import time
from scipy.signal import convolve2d

# Function to compute the next state of the game
def next_board_state(board):
    # Define the kernel for counting neighbors
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    # Count neighbors using 2D convolution
    neighbor_count = convolve2d(board, kernel, mode='same', boundary='wrap')
    # Apply the rules of the game
    new_board = (neighbor_count == 3) | ((board == 1) & (neighbor_count == 2))
    return new_board.astype(int)

# Function to apply the additional random rule every five frames
def apply_random_rule(board, frame_count):
    if frame_count % 5 == 0:
        i, j = np.random.randint(board.shape[0]), np.random.randint(board.shape[1])
        if np.random.rand() > 0.5:
            board[i, j] = 1  # Set a random cell on
        else:
            board[i, j] = 0  # Set a random cell off
    return board

# Initialize the Streamlit app
st.title("Game of Life with Additional Rule")

# Set up the initial board
board_size = st.slider("Board size", 10, 400, 200)
initial_board = np.random.choice([0, 1], size=(board_size, board_size))
board = initial_board

# Placeholder for the image display
image_placeholder = st.empty()

# Run the simulation
frame_count = 0
while True:
    # Display the board as an image
    image = (board * 255).astype(np.uint8)
    image_placeholder.image(image, use_column_width=True)
    
    # Compute the next state
    board = next_board_state(board)
    
    # Apply the additional random rule
    board = apply_random_rule(board, frame_count)
    
    # Increment the frame count
    frame_count += 1
    
    # Sleep for a short interval to control the speed of the animation
    time.sleep(0.1)