```diff
! If you found yourself here from my poster consider looking at the python noebook
```
---
# Final Year Project: Distirbuted Colour Concept Learning in Swarms
---

Five learning models, and agent-based update rules, are developed for populations of agents to find concepts through repeatedly playing the discimination language games. Each show emergent convergence for random concepts, and those grounded colour concepts from a dataset. Computational results find promising performance from quantum- mechanical agents. Data-streaming algorithms are introduced for agents to reason with infinite potential labels, and finite focal labels.

Produced in efforts towards a final year project towards a MEng in Engineering Mathematics from the university of Bristol.

Feel free to send questions my way with regard to any part of this project.

## Further Abstract

Quantum-inspired learning models differ from those suggested in the literature, and are proposed with local update rules. Their interpretations are discussed, and projection operator's subspaces appear to best model colour concepts.

Data-streaming algorithms are introduced for agents to reason with infinite potential labels, and finite focal labels. The Misra-Gries frequency estimation algorithm is adapted to enforce a degree of agreeability between agents before accepting new concepts. Focal colours are reliably learnt while agents use bounded space, and concept representation learning computation is limited to core categories.

Topics from quantum information theory and data-streaming algorithms infrequently used beyond their theoretic domains are explored to model colour concept learning in swarms on a dataset of natural language.



## Repository Layout

 - [`main.ipynb`](https://github.com/DanGorringe/distColConceptLearning_ematm5000) details all numerical experiments used in the final thesis, with running commentary nabbed from the report.
 - `agentClass.py` defines a class for a classical agent, and an Agreeable Misra-Gries agent. Both contrain a learningModel which is querier.
 - `learningModels.py` contains all the different learnig models used; exemplar, prototype, quantum vector exempalr, density matrix, and projection operator.
 - `discriminationGame.py` defines the language game played between agents.
 - `utilities.py` contains some quality-of-life functions, including; dict argmax, and rgb2qubit representation translations
 - `main.py` is a legacy file for how discrimination games and functions were intially trialled.


## Quantum Concepts
The similarity of prototype theory’s state ensembles and quantum density matrices, representing colour in a quantum-mechanical space (like the one we live in), and the literature proposing quantum probability to explain psychological evidence dissuading cognition using Kolomogov probability have all influenced the following quantum models.

The three quantum-inspired approaches explore qubit-colour representations and the utlilty of different operator types in modelling concepts - with the main focus on the relation between statistical description in-built to quantum states and that proposed by Rosch’s prototype theory of concepts. While models are introduced and their emergent convergence is observed in swarms, it is advocated that further study look at the inbuilt mathematical descriptions of quantum mechanics to, for example, explore; hedging, or conjunction, through the combination of density matrices, qubit collapse on measurement for consecutive questions, and entanglement in speaker-listener objects.

Implemented using [QuTiP](http://qutip.org/)'s quantum Python library.

Results found are not discouraging.

## Data Streaming algorithms
Although often obfuscated to graduate theoretical computer science classes, data streaming algorithms offer a dimension to reason and process large pools of noisy data with sparse focal points. Data streaming algorithms work on the premise that their data streams are so vast or costly that there is no looking back or querying. With the natural world, and the complexity of the human experience streaming algorithms become a useful constraint on modelling cognition and learning.

An adaptation of Misra-Gries, a frequency estimation algorithm, is given that enforces a degree of agreeability in concept representation in swarms. Which introduces a sense of meaning into learning, or reference in the Fregen sense. Agreeable Misra-Gries prioritises shared concepts rather than frequency, or so it is hoped.

## Contact Details:
Email: `dg17129@bristol.ac.uk`
