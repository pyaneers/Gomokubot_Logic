# GOMOKUBOT

```python
Team  = 'Pyaneers'
Members = ['Andrew Baik', 'Jason Burns', 'Christopher Chapman', 'Alexander Stone']
```

---

### About
Gomokubot learns the game of [gomoku](https://en.wikipedia.org/wiki/Gomoku) using 
Google [tensorflow](https://www.tensorflow.org/).

---

### Development

- As a player, I like to be able to play against a computer
- As a player, I like to see computer learning
- As a player, I like to display the board on the web application while I play against computer
- As a developer, I like to access to play against computer
- As a developer, I like to transfer server data using json format
- As a developer, I like to store results to the database so that computer can learn from previous games

##### Workflow

Fractalkine workflow;  major level: squad, minor level: pairs, patch level: single.
Conflict will be handled in the thunderdome, AKA the whiteboard.

##### Branching:

Deployment: final product<br>
:arrow_up:<br>
Master: successful development commits<br>
:arrow_up:<br>
Developlemt: feature integration, code merging, and testing<br>
:arrow_up::arrow_up::arrow_up:<br>
f_feature_specific_branches: feature development<br>

wireframe:
![wireframe](https://github.com/GoTeam5/Gomokubot/blob/master/assets/GOMOKU.jpg) <br>

training flow:
![wireframe](https://github.com/GoTeam5/Gomokubot/blob/master/assets/training_flow.jpg) <br>

06SEP18:
Design

Game logic (Controller)
- validation of the victory
- Validation move

RESTful endpoints (Server/APIView)
- Post (new game)
- Put (send new point)
- Get (front-end for user)

ML(tensorflow, itertools)

Front-end
- Bare minimum of yellow background with black outlines, black and white rocks. text block
