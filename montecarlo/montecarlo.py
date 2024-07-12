from random import sample
import numpy as np
import pandas as pd
class Die():
    
    def __init__(self, sides):
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
        if side not in self._die['side'].values:
            raise IndexError("The side does not exist")
        if weight < 0:
            raise ValueError("The weight must be greater than or equal to zero")
        if not np.issubdtype(type(weight), np.number):
            raise TypeError("The weight must be a number")
        self._die.loc[self._die['side'] == side, 'weight'] = weight
        self.weights = self._die['weight'].values
    
    def roll(self, nrolls):
        self.nrolls = 1
        total_weight = sum(self.weights)
        normalized_weights = [w / total_weight for w in self.weights]
        outcomes = np.random.choice(self._die['side'].values, size=nrolls, replace=True, p=normalized_weights)
        return list(outcomes)
    
    def current_state(self):
        return self._die  
class Game():
    
    def __init__(self, dice):
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
        if self._nrolls is None:
            self._nrolls = nrolls
        elif self._nrolls != nrolls:
            raise ValueError(f"Incompatible number of rolls: {nrolls} provided, but {self._nrolls} expected")
        
        spec_die = self.dice[die_number - 1]  # Access the specific die by index (adjusting for 1-based indexing)
        rolls = spec_die.roll(nrolls)
        
        # Create a DataFrame to store the results in wide format
        roll_df = pd.DataFrame({
            'roll_number': range(1, nrolls + 1),
            f'die_{die_number}': rolls
        }).set_index('roll_number')
        
        # Combine with existing _gamedf
        if self._gamedf.empty:
            self._gamedf = roll_df
        else:
            self._gamedf = self._gamedf.join(roll_df, how='outer')
        
        return self._gamedf
        
    def results(self, form = 'wide'):
        self.form = form
        if self.form == 'wide':
            return self._gamedf
        elif self.form == 'narrow':
            return self._gamedf.melt(ignore_index=False)
        else:
            raise ValueError("Invalid option for form")   
class Analyzer():
    
    def __init__(self, game):
        if type(game) != Game:
            raise TypeError("The input must be a Game object")
        self.game = game
        self._gamedf = game._gamedf
        self.nrolls = len(game._gamedf) 
        self.jackpot_counter = 0
        self.die_sides = self.game.dice[0].sides

    def jackpot(self):
        for index, row in self._gamedf.iterrows():
            if len(set(row)) == 1:  # Check if all non-NaN values in the row are the same
                self.jackpot_counter += 1
        return self.jackpot_counter
    
    def face_count(self):
        counts = []
        for _, row in self.game._gamedf.iterrows():
            count = row.value_counts().reindex(self.die_sides, fill_value=0)
            counts.append(count)
        counts_df = pd.DataFrame(counts, index=self.game._gamedf.index).reset_index(drop=True)
        return counts_df
        
    def combo_count(self):
        #computes distinct combinations of faces rolled
        combos = []
        for _, row in self.game._gamedf.iterrows():
            combo = tuple(sorted(row.dropna()))
            combos.append(combo)
        combo_counts = pd.Series(combos).value_counts().reset_index()
        combo_counts.columns = ['combination', 'count']
        combo_counts.set_index('combination', inplace=True)
        return combo_counts
    
    def perm_count(self):
        #computes distinct permutations of faces rolled
        perms = []
        for _, row in self.game._gamedf.iterrows():
            perm = tuple(row.dropna())
            perms.append(perm)
        perm_counts = pd.Series(perms).value_counts().reset_index()
        perm_counts.columns = ['permutation', 'count']
        perm_counts.set_index('permutation', inplace=True)
        return perm_counts
    
    

