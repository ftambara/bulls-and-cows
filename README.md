# bulls-and-cows

A slight variation of the bulls and cows game, numerical version. Terminal based.

## Task list
- [x] Write initial specs
- [x] Basic functionality with terminal interface
- [ ] Computer player
- [ ] Game modes
- [ ] (Optional) Improved GUI

## Game Rules

- The game can be player against the machine, or by any number of human players plus one optional computer player.
- In the first turn of every round, the machine generates a hidden number for each player. The player tries to [guess](#possible-hidden-numbers) it. Once the guess is sent, the machine returns the number of bulls (digits present in the hidden number in the exact same position) and the number of cows (digits present in the hidden number in a different position).
- The players keeps taking turns until they either discover their number or exhaust the number of turns for that round (10 turns in most game modes)
- Points are calculated according to the [scores](#scores) section

### Possible Hidden Numbers

The number's only constraint are: 
  - Any digit may be present only once;
  - Number length and digit range (0 to n) depend on the [game mode](#game-modes).

### Scores

- If the player discovered the number, he adds 1 point to his score per round taken, -1 point for each digit in the number. The player's score cannot go below zero, but can be decreased by a negative score round.
- If the player doesn't discover the number, he gets the corresponding [mode](#game-modes) penalty.

### Game settings

#### Game modes

| Mode        | Number length | Digits | Max turns | Max points |
| ----------- | ------------- | ------ | --------- | ---------- |
| Pointless   | 5             | 0 - F  | 12        | 35         |
| Hard        | 5             | 0 - 9  | 7         | 30         |
| Normal      | 4             | 0 - 9  | 10        | 30         |
| Quick       | 3             | 1 - 3  | 5         | 10         |

#### Other settings

- Turn timeout: If, enabled, if the time is excedeed, the turn is lost. The maximum time is 15 seconds for every game moude except for quick, for which it is 8 seconds.
- Collate turns. If enabled, players play their turn and pass the control over to the next. If disabled, players play every turn until the round is finished.
