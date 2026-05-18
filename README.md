# Shadow Mini Game

A simple dodge-and-survive game built with Pygame.

## Description

Control a blue player character and avoid a red enemy that chases you. Survive as long as possible by dodging collisions. Each collision reduces your health by 1 HP.

## How to Play

- **Arrow Keys**: Move up, down, left, right
- **Start Screen**: Press any key to begin
- **Game Over**: Press any key to restart

## Game Features

- Enemy AI that chases the player
- Health system (starts at 100 HP)
- Boundary checking to keep player and enemy on-screen
- Smooth 60 FPS gameplay

## Requirements

- Python 3.x
- Pygame

## Installation

```bash
pip install pygame
```

## Running the Game

```bash
python main.py
```

## Game Details

- **Screen Size**: 800x600 pixels
- **Player**: Blue square (50x50), moves at 5 pixels/frame
- **Enemy**: Red square (50x50), chases player at 3 pixels/frame
- **Mechanics**: Avoid the enemy to keep your health intact
