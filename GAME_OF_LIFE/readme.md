# Conway's Game of Life

Conway's Game of Life is a famous cellular automaton, implemented here in Python using the Pygame library. This simulation demonstrates the evolution of patterns based on specific rules.

## Usage

1. **Initialization:**

   - Ensure you have Python and Pygame installed.
   - Run the script `main.py` to start the simulation.

2. **Controls:**

   - **Mouse Clicks:** Toggle cells on/off.
   - **Space Key:** Pause/Resume the game.
   - **'C' Key:** Clear the grid.
   - **'G' Key:** Generate a new random initial state.

3. **Game Rules:**

   - Each cell can be alive or dead.
   - **Live Cell:**
     - Dies if it has fewer than 2 or more than 3 live neighbors.
     - Survives if it has 2 or 3 live neighbors.
     - New cell is born if it has exactly 3 live neighbors.

## Code Explanation

1. **Setting Up the Grid:**

   - Define grid size and cell dimensions.
   - Generate a random initial state.

2. **Drawing the Grid:**

   - Draw live cells and grid lines using Pygame.

3. **Updating the Grid:**

   - Implement Conway's Game of Life rules to update the cell states.

4. **Handling User Input:**

   - Mouse clicks and keyboard keys control the simulation.

## Example

The code creates a grid of cells where each cell can be either alive or dead. The state of the cells is updated in each iteration of the game loop based on specific rules, creating interesting patterns and behaviors. Users can interact with the grid by toggling cells, pausing the simulation, clearing the grid, and generating new random patterns.

## Useful Links

- [Learn More about Conway's Game of Life](https://playgameoflife.com/info)

Have fun experimenting with different initial patterns and observing how they evolve over time!

## Requirements

- Python 3.x
- Pygame

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
