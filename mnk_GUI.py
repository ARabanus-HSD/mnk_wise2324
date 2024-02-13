import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem
from PyQt6.QtGui import QPixmap, QFontDatabase, QFont, QColor, QPainter
from PyQt6.QtCore import Qt
from mnkforGUI import Game, Board, Player, Bot_random, Bot_simple, Bot_complex

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap, QFont, QColor, QFontDatabase
from PyQt6.QtCore import Qt, QSize


class ChalkboardButton(QPushButton):
    def __init__(self, text, value):
        super(ChalkboardButton, self).__init__(text)
        self.value = value
        self.setStyleSheet("color: white; font: bold 16px;")
        

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load chalk font
        font_path = "EraserRegular.ttf"  # path
        chalk_font = QFontDatabase.addApplicationFont(font_path)
        chalk_font = QFont("Eraser", 20)
        
        # # check if font is loaded
        if chalk_font == -1:
            print(f"Error loading font from path: {font_path}")
        else:
            print("Font loaded successfully!")

        # Set up background
        chalkboard_image_path = "chalkboard4.jpg" 
        chalkboard_image = QPixmap(chalkboard_image_path).scaled(self.size())

        self.setStyleSheet(f"background-image: url({chalkboard_image_path});")

        # Set up central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set up main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        #headline
        headline_label = QLabel("Main Menu", self)
        headline_label.setFont(QFont("Eraser", 40, QFont.Weight.Bold))  # Set a larger font size and bold style
        headline_label.setStyleSheet("color: white;")  # Set font color to white
        main_layout.addWidget(headline_label)
        
        # Create input boxes for m, n, k
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
        

        
        
        #Player 1

        # Create labels and buttons
        player1_label = QLabel("Player 1", self)
        player1_label.setFont(chalk_font)
        player1_label.setStyleSheet("color: white;")  # Set font color to white

        # Create a horizontal layout for "Enter player name" label and text box
        player1_name_layout = QHBoxLayout()  
        player1_name_label = QLabel("Enter player name:", self)
        player1_name_label.setFont(chalk_font)
        player1_name_label.setStyleSheet("color: white;")  # Set font color to white
        
        self.player1_name_input = QLineEdit(self)
        self.player1_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player1_name_input.setFont(chalk_font)
        player1_name_layout.addWidget(player1_name_label)
        player1_name_layout.addWidget(self.player1_name_input)

        
       #  Buttons
        player1_type_label = QLabel("Select your player type", self)
        player1_type_label.setFont(chalk_font)
        player1_type_label.setStyleSheet("color: white;")
        player1_buttons_layout = QHBoxLayout()

        self.player1_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Complex", 4),
        ]
        

        # Player 2
       
        # Create labels and buttons
        player2_label = QLabel("Player 2", self)
        player2_label.setFont(chalk_font)
        player2_label.setStyleSheet("color: white;")  # Set font color to white

        # Create a horizontal layout for "Enter player name" label and text box
        player2_name_layout = QHBoxLayout()  
        player2_name_label = QLabel("Enter player name:", self)
        player2_name_label.setFont(chalk_font)
        player2_name_label.setStyleSheet("color: white;")  # Set font color to white
        
        self.player2_name_input = QLineEdit(self)
        self.player2_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player2_name_input.setFont(chalk_font)
        player2_name_layout.addWidget(player2_name_label)
        player2_name_layout.addWidget(self.player2_name_input)

        
       #  #Buttons
       
        player2_type_label = QLabel("Select your player type", self)
        player2_type_label.setFont(chalk_font)
        player2_type_label.setStyleSheet("color: white;")
        player2_buttons_layout = QHBoxLayout()
        
        self.player2_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Complex", 4),
        ]
        


        
        # Add widgets to layout
        #m,n,k
        main_layout.addWidget(input_mnk_label)
        main_layout.addLayout(input_layout)
        
        # Player 1
        main_layout.addWidget(player1_label)
        main_layout.addLayout(player1_name_layout)
        main_layout.addWidget(player1_type_label)
        # Add player type buttons to layout
        for button in self.player1_buttons:
            button.setFont(chalk_font)
            player1_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player1_button_click)
        main_layout.addLayout(player1_buttons_layout)
        
        # Create start game button
        start_button = ChalkboardButton("Start Game", 0)
        start_button.setFont(chalk_font)
        start_button.setStyleSheet("color: white;")
        start_button.clicked.connect(self.on_start_button_click)
        
        # Player 2
        main_layout.addWidget(player2_label)
        main_layout.addLayout(player2_name_layout)  # Use the corrected layout here
        main_layout.addWidget(player2_type_label)
        # Add player type buttons to layout
        for button in self.player2_buttons:
            player2_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player2_button_click)
        main_layout.addLayout(player2_buttons_layout)

        main_layout.addWidget(start_button)


        # Store input boxes
        self.m_input = m_input
        self.n_input = n_input
        self.k_input = k_input

        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 800, 600)  # Set your preferred window size
        
        
        
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
        m = int(self.m_input.text())
        n = int(self.n_input.text())
        k = int(self.k_input.text())


        # Get name 
        player1_name = self.player1_name_input.text()
        player2_name = self.player2_name_input.text()
        # Get the selected player types
        player1_type = self.get_selected_button_value(self.player1_buttons)
        player2_type = self.get_selected_button_value(self.player2_buttons)
        # print(player1_type)
        # print(player2_type)

        # Create MNK game instance and start the game with the chosen options
        current_game = Game(m, n, k)
        # player1 = current_game.choose_player(1, player1_name, player1_type)
        # player2 = current_game.choose_player(2, player2_name, player2_type)
        current_game.start(player1_type, player1_name, player2_type, player2_name)
        current_game.game_loop()
        
        # Show the game board window
        game_board_window = GameBoardWindow(m, n)
        game_board_window.show()
        self.hide()
        
        
class GameBoardWindow(QMainWindow):
    # def __init__(self, m, n):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initUI()

    def initUI(self):
        # Setup window
        self.setWindowTitle("MNK Game")
        self.setGeometry(100, 100, 800, 600)
        
        # Load and set up font and background
        self.setStyleSheet("background-image: url('chalkboard4.jpg');")
        QFontDatabase.addApplicationFont("EraserRegular.ttf")
        chalk_font = QFont("Eraser", 20)
        
        # Set up central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        central_widget.setStyleSheet("background-color: white;")  # Choose a color that simulates the spaces (grid lines) effect

        # Game Name Heading
        game_name_label = QLabel("MNHURE")
        game_name_label.setFont(QFont("Eraser", 48, QFont.Weight.Bold))
        game_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
       # game_name_label.setStyleSheet("color: white;")
        game_name_label.setStyleSheet("""
                    color: white; 
                    text-shadow: 2px 2px 4px #000000; 
                    letter-spacing: 2px;
                    """)
        main_layout.addWidget(game_name_label)

        # Setup players layout
        self.players_layout = QHBoxLayout()
        self.player1_label = QLabel(f"Player 1: {self.game.player1.name}")
        self.player1_label.setFont(chalk_font)
        self.player1_label.setStyleSheet("color: white;")
        self.player2_label = QLabel(f"Player 2: {self.game.player2.name}")
        self.player2_label.setFont(chalk_font)
        self.player2_label.setStyleSheet("color: white;")
        self.players_layout.addWidget(self.player1_label)
        #players_layout.addStretch()
        self.players_layout.addWidget(self.player2_label)
        main_layout.addLayout(self.players_layout)
        
        # Setup game board layout
      #  board_layout = QGridLayout()
        
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(1)  # Adjust spacing as needed
        grid_layout.setVerticalSpacing(1)  
        main_layout.addLayout(grid_layout)
        self.buttons = []
        for i in range(self.game.board.m):
            row_buttons = []
            for j in range(self.game.board.n):
                button = QPushButton()
                button.setFont(chalk_font)
                button.setStyleSheet("color: white; background-color: transparent;")
                button.setFixedSize(QSize(60, 60))
                button.clicked.connect(lambda checked, x=i, y=j: self.on_button_clicked(x, y))
                grid_layout.addWidget(button, i, j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_clicked(self, i, j):
        currentPlayer = self.game.get_current_player()
        if self.game.place_move((i, j)):
            self.update_ui()

            # This block simulates the 'game loop' logic for each move
            if self.game.board.has_won(currentPlayer):
                self.display_winner(currentPlayer)
                self.disable_board()
            elif self.game.full_board():
                self.display_winner(None)
                self.disable_board()
            else:
                self.game.switch_player()
                self.update_player_ui()
        else:
            print("Invalid move.")
        
    def update_ui(self):
        for i in range(self.game.board.m):
            for j in range(self.game.board.n):
                if self.game.board.board[i, j] == 1:
                    self.buttons[i][j].setText("X")
                elif self.game.board.board[i, j] == 2:
                    self.buttons[i][j].setText("O")
                    
    def update_player_ui(self):
        # Reset label styles to default
        self.player1_label.setStyleSheet("")
        self.player2_label.setStyleSheet("")
        if self.game.current_player == 1:
            self.player1_label.setStyleSheet("color: red;")  # Highlight current player
        else:
            self.player2_label.setStyleSheet("color: red;")
            
    def disable_board(self):
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setEnabled(False) 
        
    def highlight_current_player(self):
        current_player = self.game.get_current_player()
        for item in self.scene.items():
            if isinstance(item, QGraphicsTextItem):
                if current_player == 1 and item.toPlainText() == "X":
                    item.setDefaultTextColor(QColor("yellow"))
                elif current_player == 2 and item.toPlainText() == "O":
                    item.setDefaultTextColor(QColor("yellow"))

    def display_winner(self, player):
        winner_message = ""
        if player == 1:
            winner_message = f"Congratulations, {self.game.player1.name} wins!"
        elif player == 2:
            winner_message = f"Congratulations, {self.game.player2.name} wins!"
        else:
            winner_message = "It's a draw!"
            
        #QMessageBox.information(self, "Game Over", winner_message)

        # Use a QLabel as a simple way to show the winner or a draw
        winner_label = QLabel(winner_message, self)
        winner_label.setFont(QFont("Eraser", 30))
        winner_label.setStyleSheet("color: white;")
        winner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(winner_label)
        
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            # get coordinates
            pos = event.pos()
            print("Mouse position:", pos)  # Debugging print
            # transform into scene coordinates
            scene_pos = self.view.mapToScene(pos)
            print("Scene position:", scene_pos)  # Debugging print
            # check if it's on the rectangle
            items = self.scene.items(scene_pos)
            print("Items under mouse cursor:", items)  # Debugging print
            for item in items:
                if isinstance(item, QGraphicsRectItem):
                    col = int(item.rect().x() / self.cell_size)
                    row = int(item.rect().y() / self.cell_size)
                    print("Clicked cell coordinates:", row, col)  # Debugging print
                    current_player = self.game.get_current_player()
                    print("Current player:", current_player)  # Debugging print
                    if current_player is not None:
                        print("Placing move...")  # Debugging print
                        if self.game.place_move((row, col)):
                            print('Move placed')  # Debugging print
                            self.handle_move(row, col)
                            print('Stone placed')  # Debugging print
                        else:
                            print("Invalid move from mousePressEvent")
                    break
                
        
    def handle_move(self, row, col):
        # Call place_move method of the Game object and update GUI accordingly
        if self.game.place_move((row, col)):
        # Update the scene with the new move
            self.update_gui()

    def update_gui(self):
        # Update GUI elements to reflect the current state of the game board
        # For example, highlight current player's turn, update labels, etc.
        self.highlight_current_player()
        self.draw_board()  # Redraw the game board with the latest moves
        # Add more GUI update logic as needed

    def draw_board(self):
        # Clear the scene
        self.scene.clear()

        # Calculate offset for centering the game board
        board_width = self.game.board.n * self.cell_size
        board_height = self.game.board.m * self.cell_size
        offset_x = (self.view.width() - board_width) / 2
        offset_y = (self.view.height() - board_height) / 2

        # Draw the game board with game stones
        for row in range(self.game.board.m):
            for col in range(self.game.board.n):
                cell_x = col * self.cell_size + offset_x
                cell_y = row * self.cell_size + offset_y
                if self.game.board.board[row][col] == 1:  # Player 1's stone
                    self.draw_game_stone(cell_x, cell_y, "X")
                elif self.game.board.board[row][col] == 2:  # Player 2's stone
                    self.draw_game_stone(cell_x, cell_y, "O")
                    
                    
    def draw_game_stone(self, row, col, symbol):
        # Draw a game stone on the specified cell
        rect_item = QGraphicsRectItem(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
        rect_item.setPen(QColor("white"))
        self.scene.addItem(rect_item)

        # Draw player moves using chalk_font
        text_item = QGraphicsTextItem(symbol, rect_item)
        text_item.setFont(self.view.font())  # Use the same font as the view
        text_item.setDefaultTextColor(QColor("white"))
        text_item.setPos(col * self.cell_size + self.cell_size / 4, row * self.cell_size + self.cell_size / 4) 


        # only for debugging purposes, delete later on
    def print_board(self):
        for row in self.game.board:
            print(row)
                    
        # super().__init__()

        # # Load chalk font
        # font_path = "EraserRegular.ttf"  # path
        # chalk_font = QFontDatabase.addApplicationFont(font_path)
        # chalk_font = QFont("Eraser", 20)

        # # Set up background
        # chalkboard_image_path = "chalkboard4.jpg"
        # # chalkboard_image = QPixmap(chalkboard_image_path).scaled(self.size())
        # self.setStyleSheet(f"background-image: url({chalkboard_image_path});")

        # # Set up central widget
        # central_widget = QWidget(self)
        # self.setCentralWidget(central_widget)

        # # Set up main layout
        # main_layout = QVBoxLayout(central_widget)
        # main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # # Create QGraphicsScene and QGraphicsView for the game board
        # scene = QGraphicsScene(self)
        # view = QGraphicsView(scene)
        # main_layout.addWidget(view)
        

        # # Set the font for the entire QGraphicsView
        # view.setFont(chalk_font)

        # # Draw m x n scratchboard
        # cell_size = 50
        # for row in range(m):
        #     for col in range(n):
        #         rect_item = QGraphicsRectItem(col * cell_size, row * cell_size, cell_size, cell_size)
        #         rect_item.setPen(QColor("white"))
        #         scene.addItem(rect_item)

        #         # Draw player moves using chalk_font
        #         text_item = QGraphicsTextItem("", rect_item)
        #         text_item.setFont(chalk_font)
        #         text_item.setDefaultTextColor(QColor("white"))
        #         text_item.setPos(col * cell_size + cell_size / 4, row * cell_size + cell_size / 4)

                
        # self.setWindowTitle("Game Board")
        # self.setGeometry(100, 100, n * cell_size + 40, m * cell_size + 40)  # Adj
        
    # def place_move(self, row, col, player_number):
    #     # Get the chalk_font symbol for the player
    #     symbol = "X" if player_number == 1 else "O"

    #     # Iterate through all items in the scene and find the correct QGraphicsRectItem
    #     for item in self.scene().items():
    #         if isinstance(item, QGraphicsRectItem):
    #             rect_item = item
    #             rect_row = int(rect_item.y() / cell_size)
    #             rect_col = int(rect_item.x() / cell_size)

    #         # Check if the current item corresponds to the specified row and col
    #         if rect_row == row and rect_col == col:
    #             # Draw the player's move using chalk_font
    #             text_item = QGraphicsTextItem(symbol, rect_item)
    #             text_item.setFont(chalk_font)
    #             text_item.setDefaultTextColor(QColor("white"))
    #             text_item.setPos(col * cell_size + cell_size / 4, row * cell_size + cell_size / 4)
    #             break


if __name__ == "__main__":
    app = QApplication(sys.argv)
   # main_menu = MainMenu()
    #main_menu.show()
    # 1. Initialize the Game Instance
    current_game = Game(5, 5, 4)
    
    # 2. Start the Game
    current_game.start(player1_type=1, player1_name="Dalia",
                       player2_type=1, player2_name="Anton")
    
    # 3. Run the Game Loop
    current_game.game_loop()
    
    # 4. Create and Show the GUI
    game_window = GameBoardWindow(current_game)
    game_window.show()
    
    # 5. Execute the Application
    sys.exit(app.exec())
    