import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QMessageBox, QMainWindow, QWidget,
    QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsScene,
    QGraphicsView, QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem)
from PyQt6.QtGui import QPixmap, QFontDatabase, QFont, QColor, QPainter
from PyQt6.QtCore import Qt, QTimer, QSize, pyqtSignal
from mnkforGUI import Game, Board, Player, Bot_random, Bot_simple, Bot_simple_v2, Bot_complex
from copy import deepcopy


class ChalkboardButton(QPushButton):
    def __init__(self, text, value):
        super(ChalkboardButton, self).__init__(text)
        self.value = value
        self.setStyleSheet("color: white; font: bold 16px;")


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # chalk font
        font_path = "EraserRegular.ttf"
        chalk_font = QFontDatabase.addApplicationFont(font_path)
        chalk_font = QFont("Eraser", 20)

        # # check if font is loaded
        if chalk_font == -1:
            print(f"Error loading font from path: {font_path}")
        else:
            print("Font loaded successfully!")

        # background
        chalkboard_image_path = "chalkboard4.jpg"
        chalkboard_image = QPixmap(chalkboard_image_path).scaled(self.size())
        self.setStyleSheet(f"background-image: url({chalkboard_image_path});")

        # central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # headline
        headline_label = QLabel("Main Menu", self)
        headline_label.setFont(QFont("Eraser", 40, QFont.Weight.Bold))
        headline_label.setStyleSheet("color: white;")
        main_layout.addWidget(headline_label)

        # input boxes for m, n, k
        input_layout = QHBoxLayout()

        input_mnk_label = QLabel("Enter gameboard parameters:", self)
        input_mnk_label.setFont(chalk_font)
        input_mnk_label.setStyleSheet("color: white;")

        m_input = QLineEdit(self)
        m_input.setPlaceholderText("height")
        m_input.setFont(chalk_font)
        m_input.setStyleSheet("color: white; margin-bottom: 0px;")
        input_layout.addWidget(m_input)

        n_input = QLineEdit(self)
        n_input.setPlaceholderText("width")
        n_input.setFont(chalk_font)
        n_input.setStyleSheet("color: white; margin-bottom: 5px;")
        input_layout.addWidget(n_input)

        k_input = QLineEdit(self)
        k_input.setPlaceholderText("winning length")
        k_input.setFont(chalk_font)
        k_input.setStyleSheet("color: white; margin-bottom: 5px;")
        input_layout.addWidget(k_input)

        # Player 1
        player1_label = QLabel("Player 1", self)
        player1_label.setFont(chalk_font)
        player1_label.setStyleSheet("color: white;")

        player1_name_layout = QHBoxLayout()
        player1_name_label = QLabel("Enter player name:", self)
        player1_name_label.setFont(chalk_font)
        player1_name_label.setStyleSheet("color: white;")

        self.player1_name_input = QLineEdit(self)
        self.player1_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player1_name_input.setFont(chalk_font)
        player1_name_layout.addWidget(player1_name_label)
        player1_name_layout.addWidget(self.player1_name_input)

        # Buttons
        player1_type_label = QLabel("Select your player type", self)
        player1_type_label.setFont(chalk_font)
        player1_type_label.setStyleSheet("color: white;")
        player1_buttons_layout = QHBoxLayout()

        self.player1_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Simple V2", 4),
            ChalkboardButton("Bot Complex", 5),
        ]

        # Player 2
        player2_label = QLabel("Player 2", self)
        player2_label.setFont(chalk_font)
        player2_label.setStyleSheet("color: white;")

        player2_name_layout = QHBoxLayout()
        player2_name_label = QLabel("Enter player name:", self)
        player2_name_label.setFont(chalk_font)
        player2_name_label.setStyleSheet("color: white;")

        self.player2_name_input = QLineEdit(self)
        self.player2_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player2_name_input.setFont(chalk_font)
        player2_name_layout.addWidget(player2_name_label)
        player2_name_layout.addWidget(self.player2_name_input)

        # Buttons
        player2_type_label = QLabel("Select your player type", self)
        player2_type_label.setFont(chalk_font)
        player2_type_label.setStyleSheet("color: white;")
        player2_buttons_layout = QHBoxLayout()

        self.player2_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Simple V2", 4),
            ChalkboardButton("Bot Complex", 5),
        ]

        # m,n,k
        main_layout.addWidget(input_mnk_label)
        main_layout.addLayout(input_layout)

        # Player 1
        main_layout.addWidget(player1_label)
        main_layout.addLayout(player1_name_layout)
        main_layout.addWidget(player1_type_label)

        # player type buttons
        for button in self.player1_buttons:
            button.setFont(chalk_font)
            player1_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player1_button_click)
        main_layout.addLayout(player1_buttons_layout)

        # start game button
        start_button = ChalkboardButton("Start Game", 0)
        start_button.setFont(chalk_font)
        start_button.setStyleSheet("color: white;")
        start_button.clicked.connect(self.on_start_button_click)

        # Player 2
        main_layout.addWidget(player2_label)
        main_layout.addLayout(player2_name_layout)
        main_layout.addWidget(player2_type_label)

        # player type buttons
        for button in self.player2_buttons:
            button.setFont(chalk_font)
            player2_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player2_button_click)
        main_layout.addLayout(player2_buttons_layout)

        main_layout.addWidget(start_button)

        self.m_input = m_input
        self.n_input = n_input
        self.k_input = k_input

        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 800, 600)

    def on_player1_button_click(self):
        self.handle_player_button_click(self.player1_buttons)

    def on_player2_button_click(self):
        self.handle_player_button_click(self.player2_buttons)

    def handle_player_button_click(self, buttons):
        font_path = "EraserRegular.ttf"  # path
        chalk_font = QFontDatabase.addApplicationFont(font_path)
        chalk_font = QFont("Eraser", 20)

        # Clear any previous selection
        for button in buttons:
            button.setFont(chalk_font)
            button.setStyleSheet("background-color: transparent; color: white;")

        # Highlight the clicked button
        sender_button = self.sender()
        sender_button.setFont(chalk_font)
        sender_button.setStyleSheet("background-color: blue; color: white;")

    def get_selected_button_value(self, buttons):
        for button in buttons:
            if "background-color: blue;" in button.styleSheet():
                return button.value
        return None

    def on_start_button_click(self):
        # Get the chosen options
        try:
            m = int(self.m_input.text())
            n = int(self.n_input.text())
            k = int(self.k_input.text())
        except ValueError:
            # Display an error message if the conversion fails
            QMessageBox.critical(
                self,
                "Invalid Input",
                "Please enter valid integer values for m, n, and k.",
            )
            return

        player1_name = self.player1_name_input.text()
        player2_name = self.player2_name_input.text()

        player1_type = self.get_selected_button_value(self.player1_buttons)
        player2_type = self.get_selected_button_value(self.player2_buttons)

        current_game = Game(m, n, k)
        current_game.start(player1_type, player1_name, player2_type, player2_name)
        game_board_window = GameBoardWindow(current_game)
        game_board_window.show()
        self.hide()

class GameBoardWindow(QMainWindow):
    # def __init__(self, m, n):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.mainMenu = mainMenu
        self.initUI()

        self.move_timer = QTimer(self)  # Create a QTimer instance
        self.move_timer.timeout.connect(self.handle_bot_move)  # Connect to the handler
        self.move_timer.start(1000)

    def initUI(self):
        # Setup window
        self.setWindowTitle("MNK Game")
        self.setGeometry(100, 100, 800, 600)

        # Load and set up font and background
        self.setStyleSheet("background-image: url('chalkboard4.jpg');")
        QFontDatabase.addApplicationFont("EraserRegular.ttf")
        self.chalk_font = QFont("Eraser", 20)

        # Set up central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        central_widget.setStyleSheet("background-color: white;")

        # Game Name Heading
        game_name_label = QLabel("JADE-GAMING")
        game_name_label.setFont(QFont("Eraser", 48, QFont.Weight.Bold))
        game_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # game_name_label.setStyleSheet("color: white;")
        game_name_label.setStyleSheet(
            """
                    color: white; 
                    text-shadow: 2px 2px 4px #000000; 
                    letter-spacing: 2px;
                    """
        )
        main_layout.addWidget(game_name_label)

        # Setup players layout
        self.players_layout = QHBoxLayout()
        self.player1_label = QLabel(f"X {self.game.player1.name}")
        self.player1_label.setFont(self.chalk_font)
        self.player1_label.setStyleSheet("color: white;")

        self.player2_label = QLabel(f"{self.game.player2.name} O")
        self.player2_label.setFont(self.chalk_font)
        self.player2_label.setStyleSheet("color: white;")

        self.players_layout.addWidget(self.player1_label)
        self.players_layout.addWidget(self.player2_label)

        main_layout.addLayout(self.players_layout)

        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(1)  # adjust spacing
        grid_layout.setVerticalSpacing(1)
        main_layout.addLayout(grid_layout)
        self.buttons = []
        for i in range(self.game.board.m):
            row_buttons = []
            for j in range(self.game.board.n):
                button = QPushButton()
                button.setFont(self.chalk_font)
                button.setStyleSheet("color: white; background-color: transparent;")
                button.setFixedSize(QSize(100, 100))
                button.clicked.connect(
                    lambda checked, x=i, y=j: self.on_button_clicked(x, y)
                )
                grid_layout.addWidget(button, i, j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def clearBoardUI(self):
        for row in self.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)

    def game_loop(self):
        current_player = self.game.get_current_player()

        if self.game.board.has_won(current_player.player_number):
            self.display_winner(current_player.player_number)
            self.disable_board()
            return

        if self.game.board.full_board():
            self.display_winner(None)
            self.disable_board()
            return

        self.game.switch_player()
        self.update_ui()

    def on_button_clicked(self, i, j):
        current_player = self.game.get_current_player()
        if not isinstance(
            current_player, (Bot_random, Bot_simple, Bot_simple_v2, Bot_complex)
        ):
            if self.game.place_move((i, j)):
                self.game_loop()
                self.update_ui()
            else:
                print("Invalid move.")

    def handle_bot_move(self):
        current_player = self.game.get_current_player()
        # if the current player is a bot, generate and place its move
        if isinstance(
            current_player, (Bot_random, Bot_simple, Bot_simple_v2, Bot_complex)
        ):
            move = current_player.make_move()
            if move:
                row, col = move
                if self.game.place_move((row, col)):
                    self.update_ui()
                    self.game_loop()
                else:
                    print("Bot move failed", move)

    def display_winner(self, player_number=None):
        if player_number == 1:
            winner_message = f"Congratulations, {self.game.player1.name} wins!"
        elif player_number == 2:
            winner_message = f"Congratulations, {self.game.player2.name} wins!"
        elif player_number == None:
            # If player_number is None, it's a draw
            winner_message = "It's a draw!"

        dialog = GameOverDialog(winner=winner_message, parent=self)
        dialog.mainMenuRequested.connect(self.open_main_menu)
        dialog.restartGameRequested.connect(self.restart_game)
        dialog.exec()

    def update_ui(self):
        current_player = self.game.get_current_player()
        for i, row in enumerate(self.game.board.board):
            for j, cell in enumerate(row):
                button = self.buttons[i][j]
                if cell == 0:
                    button.setText("")
                    button.setEnabled(True)
                elif cell == 1:
                    print(f"Button should be X: {current_player}")
                    button.setText("X")
                    button.setEnabled(False)
                elif cell == 2:
                    print(f"Button should be O:{current_player}")
                    button.setText("O")
                    button.setEnabled(False)
        self.update_player_ui()

    def update_player_ui(self):
        if self.game.current_player == self.game.player1:
            self.player1_label.setStyleSheet("color: red;")
            self.player2_label.setStyleSheet("color: white;")
        else:
            self.player1_label.setStyleSheet("color: white;")
            self.player2_label.setStyleSheet("color: red;")

    def disable_board(self):
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setEnabled(False)

    def open_main_menu(self):
        self.close() 
        self.mainMenu.show()

    def restart_game(self):
        self.game.restart_game()
        self.clearBoardUI()
        self.initUI()
        self.update_ui()


class GameOverDialog(QDialog):
    mainMenuRequested = pyqtSignal()
    restartGameRequested = pyqtSignal()

    def __init__(self, winner, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Game Over")
        self.setStyleSheet("background-image: url('chalkboard4.jpg');")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()

        self.label = QLabel(winner)
        self.label.setStyleSheet("color: white; font-size: 24px;")
        self.label.setFont(QFont("Eraser", 20, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.menu_button = QPushButton("Main Menu")
        self.menu_button.setFont(QFont("Eraser", 16))
        self.menu_button.setStyleSheet("QPushButton { color: white; }")
        self.restart_button = QPushButton("Restart")
        self.restart_button.setFont(QFont("Eraser", 16))
        self.restart_button.setStyleSheet("QPushButton { color: white; }")
        self.close_button = QPushButton("Close")
        self.close_button.setFont(QFont("Eraser", 16))
        self.close_button.setStyleSheet("QPushButton { color: white; }")

        self.menu_button.clicked.connect(self.onMainMenuClicked)
        self.restart_button.clicked.connect(self.onRestartClicked)
        self.close_button.clicked.connect(self.onCloseClicked)

        layout.addWidget(self.menu_button)
        layout.addWidget(self.restart_button)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def display_winner(self, player_name=None):
        dialog = GameOverDialog(winner=player_name, parent=self)
        dialog.mainMenuRequested.connect(self.open_main_menu)
        dialog.restartGameRequested.connect(self.restart_game)
        dialog.exec()

    def onMainMenuClicked(self):
        self.mainMenuRequested.emit()
        self.close()

    def onRestartClicked(self):
        self.restartGameRequested.emit()
        self.close()

    def onCloseClicked(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMenu = MainMenu()
    mainMenu.show()
    sys.exit(app.exec())
