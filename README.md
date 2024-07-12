# DS5100-finalproject-ljn5yms

# Metadata
  Author: Luke Napolitano
  Project Name: Monte Carlo Simulator

# Synopsis
1. Locally clone this repo
# API Description
    CLASSES
    builtins.object
    |   Analyzer
    |   Die
    |   Game
    |
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  A class that analyzes game data.
     |  
     |  Attributes:
     |      game (Game): The game object to be analyzed.
     |      _gamedf (DataFrame): The game data as a pandas DataFrame.
     |      nrolls (int): The number of rolls in the game.
     |      jackpot_counter (int): The count of jackpot rolls.
     |      die_sides (int): The number of sides on each die.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      Initializes an Analyzer object.
     |      
     |      Args:
     |          game (Game): The game object to be analyzed.
     |      
     |      Raises:
     |          TypeError: If the input is not a Game object.
     |  
     |  combo_count(self)
     |      Computes the count of distinct combinations of faces rolled in the game.
     |      
     |      Returns:
     |          DataFrame: A pandas DataFrame with the count of each combination of faces rolled.
     |  
     |  face_count(self)
     |      Computes the count of each face rolled in the game.
     |      
     |      Returns:
     |          DataFrame: A pandas DataFrame with the count of each face rolled for each roll.
     |  
     |  jackpot(self)
     |      Counts the number of jackpot rolls in the game.
     |      
     |      Returns:
     |          int: The count of jackpot rolls.
     |  
     |  perm_count(self)
     |      Computes the count of distinct permutations of faces rolled in the game.
     |      
     |      Returns:
     |          DataFrame: A pandas DataFrame with the count of each permutation of faces rolled.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(sides)
     |  
     |  A class representing a die with customizable sides and weights.
     |  
     |  Attributes:
     |      sides (numpy.ndarray): An array containing the sides of the die.
     |      weights (numpy.ndarray): An array containing the weights of each side.
     |      _die (pandas.DataFrame): A dataframe representing the die with sides and weights.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, sides)
     |      Initializes a Die object with the given sides.
     |      
     |      Args:
     |          sides (numpy.ndarray): An array containing the sides of the die.
     |      
     |      Raises:
     |          TypeError: If the input is not a numpy array.
     |          ValueError: If the array values are not unique.
     |          TypeError: If the input array does not have a data type of strings or numbers.
     |  
     |  current_state(self)
     |      Returns the current state of the die.
     |      
     |      Returns:
     |          pandas.DataFrame: A dataframe representing the die with sides and weights.
     |  
     |  roll(self, nrolls)
     |      Rolls the die a specified number of times and returns the outcomes.
     |      
     |      Args:
     |          nrolls: The number of times to roll the die.
     |      
     |      Returns:
     |          list: A list of outcomes from the rolls.
     |  
     |  side_weight_change(self, side, weight)
     |      Changes the weight of a specific side of the die.
     |      
     |      Args:
     |          side: The side of the die to change the weight for.
     |          weight: The new weight for the side.
     |      
     |      Raises:
     |          IndexError: If the side does not exist.
     |          ValueError: If the weight is less than zero.
     |          TypeError: If the weight is not a number.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(dice)
     |  
     |  A class representing a game with multiple dice.
     |  
     |  Parameters:
     |  dice (list): A list of dice objects representing the different dice in the game.
     |  
     |  Attributes:
     |  dice (list): A list of dice objects representing the different dice in the game.
     |  dice_df (pandas.DataFrame): A DataFrame containing information about the dice.
     |  _nrolls (int): The number of rolls for the game.
     |  _gamedf (pandas.DataFrame): A DataFrame containing the game results.
     |  
     |  Methods:
     |  play(die_number, nrolls): Plays the game with the specified die number and number of rolls.
     |  results(form='wide'): Returns the game results in the specified form.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, dice)
     |      Initializes a Game object.
     |      
     |      Parameters:
     |      dice (list): A list of dice objects representing the different dice in the game.
     |      
     |      Raises:
     |      TypeError: If the input is not a list.
     |  
     |  play(self, die_number, nrolls)
     |      Plays the game with the specified die number and number of rolls.
     |      
     |      Parameters:
     |      die_number (int): The number of the die to play with.
     |      nrolls (int): The number of rolls for the game.
     |      
     |      Raises:
     |      ValueError: If the number of rolls is incompatible with previous rolls.
     |      
     |      Returns:
     |      pandas.DataFrame: The game results.
     |  
     |  results(self, form='wide')
     |      Returns the game results in the specified form.
     |      
     |      Parameters:
     |      form (str): The form of the game results. Defaults to 'wide'.
     |      
     |      Raises:
     |      ValueError: If the form is not a valid option.
     |      
     |      Returns:
     |      pandas.DataFrame: The game results.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
