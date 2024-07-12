import unittest
import pandas as pd
import numpy as np
from montecarlo.montecarlo import *
from pandas.testing import assert_frame_equal

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_die_init(self):
        my_test = Die(np.array([1,2,3,4,5,6]))
        expected = pd.DataFrame({'side': my_test.sides, 'weight': my_test.weights/len(my_test.sides)})
        # if true we have the correct data structure
        self.assertTrue(type(my_test._die) == type(expected))

    def test_die_side_weight_change(self):
        my_test = Die(np.array([1,2,3,4,5,6]))
        my_test.side_weight_change(1, 0.5)
        # if test is all good, the df was appropriately changed
        self.assertTrue(my_test._die.weight[0] == .5)

    def test_die_roll(self):
        my_test = Die(np.array([1,2,3,4,5,6]))
        my_test.roll(10)
        #if true, the output is a list of 10 rolls
        self.assertTrue(type(my_test.roll(10)) == list)
        self.assertTrue(len(my_test.roll(10)) == 10)

    def test_die_current_state(self):
        my_test = Die(np.array([1,2,3,4,5,6]))
        my_test.side_weight_change(2, 0.5)
        current_state = my_test.current_state()
        # if true, current state outputs the modified _die dataframe
        pd.testing.assert_frame_equal(current_state, my_test._die)
        
    def test_game_init(self):
        my_list = [Die(np.array([1,2,3,4,5,6])), Die(np.array([1,2,3,4,5,6]))]
        game = Game(my_list)
        # If true the created df has dice objects as the die column
        self.assertTrue(type(game.dice_df.die[0]) == Die)
        
    def test_game_play(self):
        my_list = [Die(np.array([1,2,3,4,5,6])), Die(np.array([1,2,3,4,5,6]))]
        game = Game(my_list)
        game.play(1, 5)
        # if true, the _gamedf has been modified once w/ appropriate number of rolls
        self.assertTrue(game._gamedf.shape[0] == 5)

    def test_game_results(self):
        my_list = [Die(np.array([1,2,3,4,5,6])), Die(np.array([1,2,3,4,5,6]))]
        game = Game(my_list)
        game.play(1, 5)
        game.play(2, 5)
        game.results()
        # if true, the game results df has the correct number of columns
        self.assertTrue(game.results().shape[1] == game._gamedf.shape[1])

    def test_analyzer_init(self):
        Die1 = Die(np.array([1,2,3,4,5,6]))
        Die2 = Die(np.array([1,2,3,4,5,6]))
        Die2.side_weight_change(1, 0.3)
        game = Game([Die1, Die2])
        game.play(1, 50)
        game.play(2, 50)
        analyzer = Analyzer(game)
        self.assertTrue(type(analyzer) == Analyzer)
        
    def test_analyzer_jackpot(self):
        Die1 = Die(np.array([1,2,3,4,5,6]))
        Die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([Die1, Die2])
        game.play(1, 50)
        game.play(2, 50)
        analyzer = Analyzer(game)
        analyzer.jackpot()
        self.assertTrue(type(analyzer.jackpot()) == int)

    def test_analyzer_face_count(self):
        Die1 = Die(np.array([1,2,3,4,5,6]))
        Die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([Die1, Die2])
        game.play(1, 50)
        game.play(2, 50)
        analyzer = Analyzer(game)
        faces = analyzer.face_count()
        self.assertTrue(len(faces.columns)==len(Die1.sides))

    def test_analyzer_combo_count(self):
        Die1 = Die(np.array([1,2,3,4,5,6]))
        Die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([Die1, Die2])
        game.play(1, 50)
        game.play(2, 50)
        analyzer = Analyzer(game)
        var1 = analyzer.combo_count()
        self.assertEqual(sum(var1['count']), game._nrolls)
        
    def test_analyzer_perm_count(self):
        Die1 = Die(np.array([1,2,3,4,5,6]))
        Die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([Die1, Die2])
        game.play(1, 50)
        game.play(2, 50)
        analyzer = Analyzer(game)
        var1 = analyzer.perm_count()
        self.assertEqual(sum(var1['count']), game._nrolls)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)