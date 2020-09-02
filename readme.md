# World Generation Prototype

A small tool for randomly generating landmasses, from islands to continents.

This is merely meant to be an inspiration for parts of a fictional map, not a drop-in replacement.

## TODO

- [X] Refactor Terrain to be more consistent
  - [X] Finish the terrain generation strategy
  - [X] Remove mutators from Terrain
- [X] Add a new generation strategy (only longest edge is broken up)
- [X] Set initial triangle randomly
  - [X] Finish CircleBasedTriangleStrategy (needs to set relative to center, and scale appropriately)
  - [X] Find a way to tell that strategy that window was resized (without window having to know the strategy)
- [X] Add an exponential version of NSplits
- [X] Helpful labels for non-me users
