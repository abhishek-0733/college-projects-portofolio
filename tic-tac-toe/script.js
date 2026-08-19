const cells = document.querySelectorAll(".cell");
const statusText = document.getElementById("status");

let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameActive = true;

const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

cells.forEach((cell, index) => {
    cell.addEventListener("click", () => {

        // Don't allow clicking an already filled cell
        // or playing after the game has ended
        if (board[index] !== "" || !gameActive) {
            return;
        }

        // Put X or O in the selected cell
        board[index] = currentPlayer;
        cell.textContent = currentPlayer;

        // Check for winner
        if (checkWinner()) {
            statusText.textContent = `Player ${currentPlayer} wins!`;
            gameActive = false;
            return;
        }

        // Check for draw ONLY when all 9 cells are filled
        if (!board.includes("")) {
            statusText.textContent = "It's a draw!";
            gameActive = false;
            return;
        }

        // Change player
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        statusText.textContent = `Player ${currentPlayer}'s turn`;
    });
});

function checkWinner() {
    for (let combination of winningCombinations) {
        const [a, b, c] = combination;

        if (
            board[a] !== "" &&
            board[a] === board[b] &&
            board[a] === board[c]
        ) {
            return true;
        }
    }

    return false;
}

// Restart Game
const restartButton = document.getElementById("restart");

restartButton.addEventListener("click", () => {
    board = ["", "", "", "", "", "", "", "", ""];
    currentPlayer = "X";
    gameActive = true;

    cells.forEach((cell) => {
        cell.textContent = "";
    });

    statusText.textContent = "Player X's turn";
});