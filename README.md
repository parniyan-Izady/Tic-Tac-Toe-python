<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Tic-Tac-Toe Game - CS50 python Final Project</h1>
    <h2>Project Overview</h2>
    <p>
        This project is a Python-based implementation of the classic game "Tic-Tac-Toe." It was developed as the final project for the CS50x course offered by Harvard University. The game is designed to be played on a 4x4 grid, adding an extra layer of complexity compared to the traditional 3x3 version. The game offers two modes: single-player (against the computer) and two-player (against another human).
    </p>
    <h2>Features</h2>
    <h3>1. Main Menu</h3>
    <ul>
        <li>Play against the computer: Engage in a single-player game where the player competes against a basic computer opponent.</li>
        <li>Play against a friend: Enjoy a two-player game, where each player takes turns.</li>
        <li>Exit: Quit the game.</li>
    </ul>
    <h3>2. Locked Positions</h3>
    <p>At the start of each game, three random positions on the board are "locked." These positions cannot be selected by either player or the computer, adding an extra strategic challenge to the game.</p>
    <h3>3. Single-Player Mode</h3>
    <p>In this mode, the player competes against the computer. The player uses the "X" symbol, and the computer uses the "O" symbol. The computer's moves are chosen randomly from the available positions on the board, making it an unpredictable but simple opponent. The game alternates turns between the player and the computer, with each turn checking for a winner or a tie.</p>
    <h3>4. Two-Player Mode</h3>
    <p>In two-player mode, two human players compete against each other. Player 1 uses the "X" symbol, and Player 2 uses the "O" symbol. Players take turns making moves until one wins or the game ends in a tie.</p>
    <h3>5. Winner and Tie Detection</h3>
    <p>The game includes logic to check for a winner after each turn. If three of the same symbols align horizontally, vertically, or diagonally, that player is declared the winner. If the board fills up without a winner, the game ends in a tie.</p>
    <h2>How to Run</h2>
    <ol>
        <li><strong>Prerequisites</strong>: Python 3.x installed on your machine.</li>
        <li><strong>Running the Game</strong>:
            <pre><code>python tic_tac_toe.py</code></pre>
        </li>
        <li><strong>Gameplay</strong>: 
            <p>Upon starting, you'll be presented with the main menu. Enter the corresponding number to select an option. Follow the prompts to play the game. When asked for input, enter a number corresponding to the position on the board where you wish to place your symbol.</p>
        </li>
    </ol>
    <h2>Code Structure</h2>
    <ul>
        <li><code>main()</code>: The entry point of the game. It controls the main loop and the game mode selection.</li>
        <li><code>display_main_menu()</code>: Displays the main menu with options to start the game or exit.</li>
        <li><code>display_game_menu()</code>: Displays the menu after a game ends, allowing the player to return to the main menu or restart the game.</li>
        <li><code>play_single_player(board)</code>: Contains the logic for the single-player mode.</li>
        <li><code>play_two_players(board)</code>: Contains the logic for the two-player mode.</li>
        <li><code>lock_random_positions(board)</code>: Locks three random positions on the board at the start of each game.</li>
        <li><code>computer_move(board)</code>: Handles the computer's moves in single-player mode.</li>
        <li><code>check_winner(board, message, symbol, turn_count)</code>: Checks if there's a winner after each move.</li>
        <li><code>display_board(board)</code>: Displays the current state of the board.</li>
        <li><code>player_move(board, prompt, symbol)</code>: Handles player moves by updating the board.</li>
    </ul>
    <h2>Challenges and Learnings</h2>
    <p>Handling Randomness: One of the key challenges was ensuring that the random moves made by the computer did not negatively impact the gameplay experience, especially considering the locked positions on the board.</p>
    <p>Input Validation: Ensuring that user inputs were correctly handled to avoid crashes or invalid moves required careful consideration and testing.</p>
    <p>Edge Cases: Handling cases like locked positions, and ensuring the game flow was smooth in all scenarios, was a significant part of the development process.</p>
    <h2>Future Improvements</h2>
    <ul>
        <li><strong>Enhanced AI</strong>: Implementing a more sophisticated AI using techniques like Minimax to make the computer a tougher opponent.</li>
        <li><strong>GUI Version</strong>: Developing a graphical version of the game using a library like <code>tkinter</code> to improve the user experience.</li>
    </ul>
    <h2>Conclusion</h2>
    <p>This project was a valuable learning experience that combined many aspects of programming taught in the CS50p course. From handling user inputs to implementing game logic, this project reinforced fundamental concepts and provided a solid foundation for further exploration in game development.</p>
</body>
</html>
