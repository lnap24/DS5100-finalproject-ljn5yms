# DS5100-finalproject-ljn5yms

# Metadata
  Author: Luke Napolitano
  Project Name: Monte Carlo Simulator

# Synopsis
1. Locally clone this repo by opening your terminal and following the steps below. Feel free to rename your package directory as desired.
```
bash-3.2$ pwd
/Users/Luke
bash-3.2$ git clone https://github.com/lnap24/DS5100-finalproject-ljn5yms.git
Cloning into 'DS5100-finalproject-ljn5yms'...
remote: Enumerating objects: 46, done.
remote: Counting objects: 100% (46/46), done.
remote: Compressing objects: 100% (36/36), done.
remote: Total 46 (delta 15), reused 28 (delta 6), pack-reused 0
Unpacking objects: 100% (46/46), done.
bash-3.2$ mv DS5100-finalproject-ljn5yms montecarlo_project
bash-3.2$
```
2. Enter into this directory by either typing cd [your project name] into the terminal or clicking into it on a GUI like Jupyter or VSCode.
3. Create a Jupyter notebook file and in the first line type:
```
!ls -lR
```
If you are in the right place, you should get a result that looks like this:
```
total 5896
-rw-r--r--@ 1 Luke  staff   144064 Jul 12 16:17 DS5100_FinalProject.ipynb
-rw-r--r--@ 1 Luke  staff     1072 Jul 12 16:17 LICENSE
drwxr-xr-x@ 3 Luke  staff       96 Jul 12 16:17 Project Files
-rw-r--r--@ 1 Luke  staff     6717 Jul 12 16:17 README.md
-rw-r--r--@ 1 Luke  staff       72 Jul 12 16:22 Untitled.ipynb
-rw-r--r--@ 1 Luke  staff      295 Jul 12 16:17 english_letters.txt
-rw-r--r--@ 1 Luke  staff    15522 Jul 12 16:17 finproj.ipynb
drwxr-xr-x@ 4 Luke  staff      128 Jul 12 16:17 montecarlo
-rw-r--r--@ 1 Luke  staff     4025 Jul 12 16:17 montecarlo_test.py
-rw-r--r--@ 1 Luke  staff  2824256 Jul 12 16:17 scrabble_words.txt
-rw-r--r--@ 1 Luke  staff      327 Jul 12 16:17 setup.py

./Project Files:
total 40
-rw-r--r--@ 1 Luke  staff  16481 Jul 12 16:17 DS5100_FinalProjectInstructions.ipynb

./montecarlo:
total 32
-rw-r--r--@ 1 Luke  staff    51 Jul 12 16:17 __init__.py
-rw-r--r--@ 1 Luke  staff  9141 Jul 12 16:17 montecarlo.py
```

4. Create a new code cell in your notebook and now type:
```
!pip install -e .
```
You should see something like this!
```
Obtaining file:///Users/Luke/montecarlo_project
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: montecarlo
  Building editable for montecarlo (pyproject.toml) ... done
  Created wheel for montecarlo: filename=montecarlo-0.1-0.editable-py3-none-any.whl size=3557 sha256=8cf203f4667d15a28ec25396dc2089b751213cd142e0ff1da31263e67754cdc3
  Stored in directory: /private/var/folders/ks/dtpzjwpd0zlcrpw8t81ybvrr0000gn/T/pip-ephem-wheel-cache-m20d82_d/wheels/15/30/7c/1d1a96114b2e5660e1afabc6590aa79398c9cdc1dc0371b6b5
Successfully built montecarlo
Installing collected packages: montecarlo
  Attempting uninstall: montecarlo
    Found existing installation: montecarlo 0.1
    Uninstalling montecarlo-0.1:
      Successfully uninstalled montecarlo-0.1
Successfully installed montecarlo-0.1
```
5. Congrats! You've installed the montecarlo package.
6. Create another notebook where we will import the package and all its dependencies. In the first line of that notebook type
```
from montecarlo.montecarlo import *

```
You should see So Far, So Good! outputted.

7. Below are examples of how to call the classes in the package.
```
fair = Die(np.array(['H', 'T']))
fair._die
```
Running this code will return the fair Die object, a dataframe, with its faces and weights set fairly. The array can have strings or numbers.

```
mylist = [fair,fair]
fairgame = Game(mylist)
fairgame.play(1, 1000)

```
Running this code will create a Game object, which takes in Die objects for the game to be played. Playing the game with the game method will return the results of rolling the die the specified number of times.

```
fairanalyzer = Analyzer(fairgame)
fairfreq = fairanalyzer.jackpot()
```
Creating the Analyzer class preps the created Game class for the methods of Analyzer to be called on it, like jackpot.

8.     
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
