# Pygame 2d Cartesian coordinates system
This project creates a 2d Cartesian coordinates system in Pygame. The objective is to offer a base for further development of interactive mathematics.

The project architecture separates the computation of the pixel coordinates of the axes components from their drawing by Pygame. This has two advantages:

- Unit testing of computation logic is easier and more efficient.  
- It will be possible to replace Pygame by another interactive app framework.

The target platforms are both Windows and Android tablets or smartphones.

## Current development state
xR and yR mean x and y range respectively. The values are displayed as coord system titles.

<p align="center">
  <img src="images/09062020.jpg" width="650" title="Current development state">
</p>

### Currently, the Cartesian coord system parameters are

- Origin coordinates. This positions the axes on the screen.
- X and Y axes length
- X and Y axes value range
- X and Y axes labels
- axes color and thickness
- Cartesian coord system multilines title

Will be added

- X and Y axes tick size
- Grid option
