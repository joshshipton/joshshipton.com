ID="30993"
TITLE="Small Shapes go brrr, dipping my toes into the world of Cellular Automata"
LINK="cellular-automata-disease-simulation"
IS_DRAFT=F
IS_POPULAR=F
----------

### [Simulation Link](https://www.joshshipton.com/projects/cellular-automata-disease.html)
I was watching this [video](https://www.youtube.com/watch?v=p3lsYlod5OU&t=3889s) when the guest started talking about [Cellular Automata](https://en.wikipedia.org/wiki/Cellular_automaton). Earlier in the year I wasted quite a few hours on [this site](https://playgameoflife.com/) playing around with guns, spaceships and other kinds of automata. 

With more time on my hands I decided I wanted to play around and learn more about cellular automata. I have no idea why I find them so fascinating but I could watch them for hours. During the course of development for this project I lost a lot of time starting and re-running the simulation. There's something about such simple rules being able to create such vivid patterns that creates a psychedelic experience. 

After researching practical applications for cellular automata I can upon [this](https://link.springer.com/article/10.1140/epjs/s11734-022-00619-1) paper. Where someone used cellular automata to model the spread of COVID. 

This didn't seem as sophisticated as other ideas that I was interested in like [traffic flow](https://uu.diva-portal.org/smash/get/diva2:483914/FULLTEXT01.pdf) (I'm coming for this later) so I decided to tackle it. 


Here's an example run through

<div class="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Cga37Bg91Lo?si=qYNbxxLu1n8p9bZh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<br/>
<br/>

#### How it Works

The Simulation runs as a 750x750 grid in which each cell represents a person. There are four states represented by different colors as seen in the key on the right hand side of the simulation.

Each cell at any time can either be infected, recovered (but not immune), immune or normal (no state)

The simulation begins with the amount of *"initial infected"* being randomly distributed in the grid and then the days begin incrementing. 

On each consecutive day infected cells can either recover with or without immunity, or infect their neighbors, as a neighbor to an infected cell your probability of being infected increased exponentially based on how many infected neighbors you have

Once a cell has been sick for the length of infection then they "recover" with a probability p of becoming immune for n days (all variables are adjustable by the user)


If you want to play around with the disease simulation yourself I'm hosting it [here](https://www.joshshipton.com/projects/cellular-automata-disease.html), plug in whatever values you want and go crazy. 

If you're interested in the code and how everything works you can find that [here](https://github.com/joshshipton/cellular_automata_disease). Any obvious bugs/huge errors feel free to make a PR or contact me. 

### Next steps

I enjoyed/am enjoying this project. But I don't know how far I can push it. I'm going to start reading [*"Designing Beauty: The Art of Cellular Automata"*](https://www.goodreads.com/work/quotes/47988064-designing-beauty-the-art-of-cellular-automata-emergence-complexity-an) by Andrew Adamatzky and see what I learn/what inspiration I get. More Cellular Automata art/simulations are definitely on the cards. 

