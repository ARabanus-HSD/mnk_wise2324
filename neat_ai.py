# This file handles setup, training and evaluation of the NEAT AI.
# This module will interact with mnk_projekt.py where the AI makes decisions based on the game state.
# This AI will be trained for 5x5 games with a winning lenght of 5

import pickle
import neat
import os
from mnk_projekt import Game
import numpy as np

def play_a_game(genome, config):
    """
    Simulate a single game, where NEAT trained AI makes decisions based on the game state
    genome: The genome for the AI player being evaluated
    config: NEAT config from config.txt

    returns the fitness score of the genome for this game sim
    """
    net = neat.nn.FeedForwardNetwork.create(genome, config)  # Create a neural network for the genome

    m = 5
    n = 5
    k = 4
    game = Game(m, n, k)  # Initialize your game here; ensure Game class has necessary methods for AI integration
    
    # Initial setup
    current_player = 1
    game_over = False
    while not game_over:
        game_state = np.array(game.board.board)  # Assuming this is how you access the board
        game_state_flat = game_state.flatten()
        inputs = game_state_flat / 2.0  # Example: normalize game state for inputs, adjust as necessary
        
        # Additional inputs could be included here based on your setup
        # For instance: inputs = np.append(inputs, [additional_game_info])

        output = net.activate(inputs)  # Get output from neural network (decision)
        chosen_move = (int(output[0]), int(output[1]))  # Example: transforming output to a game move
        
        # Implement move and check result
        try:
            valid_move = game.attempt_move(chosen_move, current_player)  # Implement this in your game logic
            if valid_move:
                game_over = game.check_win_condition() or game.check_draw_condition()  # Implement these checks
                current_player = 2 if current_player == 1 else 1  # Switch player as example
        except Exception as e:
            game_over = True  # End game if invalid action
        
    # Example fitness calculation criteria
    fitness = 100.0 if game.winner == 1 else 0.0  # Example: Assigning fitness based on win/lose, adjust as needed
    return fitness

def eval_genomes(genomes, config):
    """
    Evaluate genomes using the game simulation by playing each genome (agent) in the game.
    
    :param genomes: A list of genomes to evaluate.
    :param config: The NEAT configuration.
    """
    for genome_id, genome in genomes:
        genome.fitness = play_a_game(genome, config)  # Assign fitness to genome based on game outcome

def run_neat(config_file):
    """
    Run NEAT algorithm to train an AI to play the game.
    
    :param config_file: Path to the NEAT configuration file.
    """
    # Load configuration.
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)
    
    # Create the population, which is the top-level object for a NEAT run.
    population = neat.Population(config)
    
    # Add a stdout reporter to show progress in the terminal.
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    
    # Run for up to N generations.
    winner = population.run(eval_genomes, 50)
    
    # Save the winner.
    with open('best_genome.pkl', 'wb') as output:
        pickle.dump(winner, output, 1)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config_neat.txt')
    run_neat(config_path)