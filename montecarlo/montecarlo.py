from random import sample
import numpy as np
import pandas as pd
class Die():
    """
    A class representing a die with customizable sides and weights.
    
    Attributes:
        sides (numpy.ndarray): An array containing the sides of the die.
        weights (numpy.ndarray): An array containing the weights of each side.
        _die (pandas.DataFrame): A dataframe representing the die with sides and weights.
    """
    
    def __init__(self, sides):
        """
        Initializes a Die object with the given sides.
        
        Args:
            sides (numpy.ndarray): An array containing the sides of the die.
        
        Raises:
            TypeError: If the input is not a numpy array.
            ValueError: If the array values are not unique.
            TypeError: If the input array does not have a data type of strings or numbers.
        """
        if type(sides) != np.ndarray:
            raise TypeError("The input must be a numpy array")
        if len(sides) != len(set(sides)):
            raise ValueError("Array values are not unique")
        if not np.issubdtype(sides.dtype, np.number) and not np.issubdtype(sides.dtype, np.str_):
            raise TypeError("The input array must have a data type of strings or numbers")
        self.sides = sides
        self.weights = np.ones(len(self.sides))
        self._die = pd.DataFrame({'side': self.sides, 'weight': self.weights/len(sides)})
    
    def side_weight_change(self, side, weight):
        """
        Changes the weight of a specific side of the die.
        
        Args:
            side: The side of the die to change the weight for.
            weight: The new weight for the side.
        
        Raises:
            IndexError: If the side does not exist.
            ValueError: If the weight is less than zero.
            TypeError: If the weight is not a number.
        """
        if side not in self._die['side'].values:
            raise IndexError("The side does not exist")
        if weight < 0:
            raise ValueError("The weight must be greater than or equal to zero")
        if not np.issubdtype(type(weight), np.number):
            raise TypeError("The weight must be a number")
        self._die.loc[self._die['side'] == side, 'weight'] = weight
        self.weights = self._die['weight'].values
    
    def roll(self, nrolls):
        """
        Rolls the die a specified number of times and returns the outcomes.
        
        Args:
            nrolls: The number of times to roll the die.
        
        Returns:
            list: A list of outcomes from the rolls.
        """
        self.nrolls = 1
        total_weight = sum(self.weights)
        normalized_weights = [w / total_weight for w in self.weights]
        outcomes = np.random.choice(self._die['side'].values, size=nrolls, replace=True, p=normalized_weights)
        return list(outcomes)
    
    def current_state(self):
        """
        Returns the current state of the die.
        
        Returns:
            pandas.DataFrame: A dataframe representing the die with sides and weights.
        """
        return self._die  
class Game():
    """
    A class representing a game with multiple dice.

    Parameters:
    dice (list): A list of dice objects representing the different dice in the game.

    Attributes:
    dice (list): A list of dice objects representing the different dice in the game.
    dice_df (pandas.DataFrame): A DataFrame containing information about the dice.
    _nrolls (int): The number of rolls for the game.
    _gamedf (pandas.DataFrame): A DataFrame containing the game results.

    Methods:
    play(die_number, nrolls): Plays the game with the specified die number and number of rolls.
    results(form='wide'): Returns the game results in the specified form.

    """
    def __init__(self, dice):
        """
        Initializes a Game object.

        Parameters:
        dice (list): A list of dice objects representing the different dice in the game.

        Raises:
        TypeError: If the input is not a list.

        """
        if type(dice) != list:
            raise TypeError("The input must be a list")
        self.dice = dice
        self.dice_df = pd.DataFrame({
            'dice_num': range(1, len(dice) + 1),
            'die': dice
        })
        self._nrolls = None
        self._gamedf = pd.DataFrame()
    
    def play(self, die_number, nrolls):
        """
        Plays the game with the specified die number and number of rolls.

        Parameters:
        die_number (int): The number of the die to play with.
        nrolls (int): The number of rolls for the game.

        Raises:
        ValueError: If the number of rolls is incompatible with previous rolls.

        Returns:
        pandas.DataFrame: The game results.

        """
        if self._nrolls is None:
            self._nrolls = nrolls
        elif self._nrolls != nrolls:
            raise ValueError(f"Incompatible number of rolls: {nrolls} provided, but {self._nrolls} expected")
        
        spec_die = self.dice[die_number - 1]
        rolls = spec_die.roll(nrolls)
        
        roll_df = pd.DataFrame({
            'roll_number': range(1, nrolls + 1),
            f'die_{die_number}': rolls
        }).set_index('roll_number')
        
        if self._gamedf.empty:
            self._gamedf = roll_df
        else:
            self._gamedf = self._gamedf.join(roll_df, how='outer')
        
        return self._gamedf
        
    def results(self, form = 'wide'):
        """
        Returns the game results in the specified form.

        Parameters:
        form (str): The form of the game results. Defaults to 'wide'.

        Raises:
        ValueError: If the form is not a valid option.

        Returns:
        pandas.DataFrame: The game results.

        """
        self.form = form
        if self.form == 'wide':
            return self._gamedf
        elif self.form == 'narrow':
            return self._gamedf.melt(ignore_index=False)
        else:
            raise ValueError("Invalid option for form")   
class Analyzer():
    """
    A class that analyzes game data.
    
    Attributes:
        game (Game): The game object to be analyzed.
        _gamedf (DataFrame): The game data as a pandas DataFrame.
        nrolls (int): The number of rolls in the game.
        jackpot_counter (int): The count of jackpot rolls.
        die_sides (int): The number of sides on each die.
    """
    def __init__(self, game):
        """
        Initializes an Analyzer object.
        
        Args:
            game (Game): The game object to be analyzed.
        
        Raises:
            TypeError: If the input is not a Game object.
        """
        if type(game) != Game:
            raise TypeError("The input must be a Game object")
        self.game = game
        self._gamedf = game._gamedf
        self.nrolls = len(game._gamedf) 
        self.jackpot_counter = 0
        self.die_sides = self.game.dice[0].sides

    def jackpot(self):
        """
        Counts the number of jackpot rolls in the game.
        
        Returns:
            int: The count of jackpot rolls.
        """
        for index, row in self._gamedf.iterrows():
            if len(set(row)) == 1:  
                self.jackpot_counter += 1
        return self.jackpot_counter
    
    def face_count(self):
        """
        Computes the count of each face rolled in the game.
        
        Returns:
            DataFrame: A pandas DataFrame with the count of each face rolled for each roll.
        """
        counts = []
        for _, row in self.game._gamedf.iterrows():
            count = row.value_counts().reindex(self.die_sides, fill_value=0)
            counts.append(count)
        counts_df = pd.DataFrame(counts, index=self.game._gamedf.index).reset_index(drop=True)
        return counts_df
        
    def combo_count(self):
        """
        Computes the count of distinct combinations of faces rolled in the game.
        
        Returns:
            DataFrame: A pandas DataFrame with the count of each combination of faces rolled.
        """
        combos = []
        for _, row in self.game._gamedf.iterrows():
            combo = tuple(sorted(row.dropna()))
            combos.append(combo)
        combo_counts = pd.Series(combos).value_counts().reset_index()
        combo_counts.columns = ['combination', 'count']
        combo_counts.set_index('combination', inplace=True)
        return combo_counts
    
    def perm_count(self):
        """
        Computes the count of distinct permutations of faces rolled in the game.
        
        Returns:
            DataFrame: A pandas DataFrame with the count of each permutation of faces rolled.
        """
        perms = []
        for _, row in self.game._gamedf.iterrows():
            perm = tuple(row.dropna())
            perms.append(perm)
        perm_counts = pd.Series(perms).value_counts().reset_index()
        perm_counts.columns = ['permutation', 'count']
        perm_counts.set_index('permutation', inplace=True)
        return perm_counts
    
    

