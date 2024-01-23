#Modified Streamlit Game of Life (written by autogen)

Python code implementing a modified Game of Life as a Streamlit app. This works fine on localhost; but, because it contains a "while True:" loop, it is not suitable for cloud hosting.

Game of Lfe starts by randomly initializing its grid wuth 30% live cells and 70% dead ones. Them it loops modifying each cell according to these rules:

  1.	Birth: A cell that is dead at one step will be alive at the next step if exactly three of its neighboring cells were alive at the previous step.
  2.	Survival: A cell remains alive at the next step if two or three of its neighbors are alive at the previous step.
  3.	Death: A cell dies (or remains dead) if it has fewer than two live neighbors (due to underpopulation) or more than three live neighbors (due to overpopulation).

On a relatrively small grid, the simulation will usually reach a boring looping state pretty quickly so we added one more rule (think of it as a cosmic ray).

* every five frames, randomly either set one cell on or another cell off regardless of its current state or that of its neighbors.

There is a web page, also written by autogen, implementing the modified Game of Life [here](https://exceo.typepad.com/game_of_life.html).
