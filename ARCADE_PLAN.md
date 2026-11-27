# My arcade plan

Use this template to draft your plan, then commit your plan and upload it as
one PDF, `arcade-plan.pdf`, by Friday November 13 at 23:59:59 PT. Paste this
markdown into a browser converter such as dillinger.io and export a PDF, or
export from a markdown editor like VS Code. Hand-drawn pages, scanned or
photographed, are just as good. See `example-plan.md` and `example-plan.pdf`
for what a filled-in plan looks like. Commit message: `Add arcade plan`

## Games I chose

(Two required games from the list, with at least one medium or spicy. The
example game does not count. A third game is optional bonus. If you pitch a
game of your own design, list it in the slot it would fill and write "assigned
by instructor" for its difficulty.)

- Game 1: Rock-paper-scissors — difficulty: easy
- Game 2: Hangman — difficulty: medium
- Game 3 (optional bonus): Tic-tac-toe — difficulty: spicy

Write each Game section so another student could implement the game without
asking you a question.

## Game 1: Rock-Paper-Scissors

- Rules, in a few sentences: The player chooses rock, paper, or scissors. The computer
randomly chooses one of the options. Rock beats scissors, scissors beats
paper, and paper beats rock. same options will result in tie. Invalid inputs receive a friendly
message and the player is asked again until they enter the correct input
- What one turn looks like: First, the program will print the available choices. It will first ask the user how many rounds thay want to play. And let the user enter rock, paper or scissors. The program should accept both uppercase and lowercase. After the user enter the input. It will print the user's choice and the computer's randomly generated choice. Based on that it will decide the winner for that round and will print the score as well until all the rounds are completed
- How it ends (win, lose, or out of turns): The game will end after all the rounds is completed. It will decide the winner based on the rounds. 
- How a score is earned (the formula or rule, and why higher is better): Score is the number of rounds won by the player. Each round win is worth one point. Higher scores mean the player won more rounds.
- Game settings (the fixed numbers or choices that define the game, such as
  grid size, number of guesses, word length, or question count): Valid choices are rock, paper, scissors. Target: first to (how many rounds the user input) round wins. Choices are case-insensitive and  whitespace is ignored. The computer selects randomly from the three choices.

## Game 2: Hangman

- Rules, in a few sentences: The program will randomly choose a word from a list of words. The player has to guess the word by entering one letter at a time. If the letter is in the word, the program will reveal the letter in the correct position. If the letter is not in the word, the player will lose one attempt. The player has to guess the word before running out of attempts. Invalid inputs will receive a friendly message and the player will be asked again until they enter a valid input.
- What one turn looks like: First, the program will randomly select a word and display blanks based on the number of letters in the word. It will also show how many wrong guesses the player has left. The player will be asked to enter one letter. The program should accept both uppercase and lowercase. After the player enters the letter, the program will check whether the letter is in the word. If it is correct, the program will reveal  the position containing that letter. If it is incorrect, the remaining attempts will decrease by one. The program will also display the letters that have already been guessed. This will continue until the player guesses the whole word or runs out of attempts.
- How it ends (win, lose, or out of turns):The game will end when the player successfully guesses all the letters in the word or when the player runs out of wrong guesses. If the player guesses the word, the program will display a winning message. Otherwise, it will display a losing message and reveal the correct word.
- How a score is earned (the formula or rule, and why higher is better): The score is the number of wrong guesses the player has left when the game ends. The player starts with 6 wrong guesses. Each incorrect guess decreases the remaining attempts by one. Higher scores mean the player guessed the word with fewer mistakes. If the player loses, the score will be 0.
- Game settings (the fixed numbers or choices that define the game, such as
  grid size, number of guesses, word length, or question count): The player will have 6 wrong guesses. Words will be randomly selected from a predefined list of words containing 4 to 8 letters. The player can only enter one alphabetical letter at a time. Inputs are case-insensitive and whitespace is ignored. Repeated guesses will not reduce the remaining attempts, and the player will be asked to choose another letter.

## Game 3: Tic-Tac-Toe

(Delete this section if you are not doing a bonus game.)

- Rules, in a few sentences:The player will play Tic-Tac-Toe against the computer. The player will use X, and the computer will use O. Both will take turns placing their symbols on a 3x3 grid. The first player to get three of their symbols in a row, column, or diagonal wins the game. The computer will randomly choose from the available positions. Invalid inputs or positions that are already taken will receive a friendly message, and the player will be asked again.
- What one turn looks like: First, the program will display an empty 3x3 grid with positions numbered from 1 to 9. The player will be asked to choose a position to place X. After the player enters a valid position, the program will update the grid and display it. The program will then check whether the player has won. If the game is not finished, the computer will randomly select an available position and place O. The program will display the updated grid and check whether the computer has won. This process will continue until either the player or the computer wins, or the grid is full.
- How it ends (win, lose, or out of turns): The game will end when either the player or the computer gets three symbols in a row, column, or diagonal. If the player gets three Xs in a row, the player wins. If the computer gets three Os in a row, the player loses. If all 9 positions are filled and neither player has won, the game will end in a draw. The program will display the final grid and announce the result.
- How a score is earned (the formula or rule, and why higher is better): The score will depend on the outcome of the game. If the player wins, they will receive 2 points. If the game ends in a draw, they will receive 1 point. If the player loses, they will receive 0 points. Higher scores mean the player achieved a better result against the computer.
- Game settings (the fixed numbers or choices that define the game, such as
  grid size, number of guesses, word length, or question count): The game will use a 3x3 grid with positions numbered from 1 to 9. The player will always use X and play first, while the computer will use O. The computer will randomly choose from the remaining available positions. The player can only enter numbers between 1 and 9. Invalid inputs and occupied positions will not count as a turn. The game will continue until there is a winner or all 9 positions are filled.

## Scoreboard fields

Use the default project layout: the module name identifies the game (rock_paper_scissors, hangman,
or tic_tac_toe). For every completed session, store one JSON record containing the game module,
outcome (win, lose, or draw), nonnegative integer score, and completion timestamp. These fields make it
possible to show game-specific scores and recognize the outcome of each session.

{
"game": "hangman",
"outcome": "win",
"score": 4,
"completed_at": "2026-11-13T18:00:00-08:00"
}

## My own game (optional)

(Pitch a game of your own design if you want to replace a list pick or serve
as your bonus game. Give its name, which slot it fills, and why it fits the
contract. Put its full rules, turn, ending, scoring, and game settings in the
matching Game section. I assign its difficulty if it fills a required slot. A
bonus game may be any difficulty. I approve these through the plan.)
