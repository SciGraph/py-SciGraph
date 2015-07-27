Python API and Command Line Client for [SciGraph](https://github.com/SciGraph/SciGraph/)

This API works off of a SciGraph REST service. Consult SciGraph docs for details.

This API is generic and will work off of any SciGraph instance,
regardless of whether it is used to store genotype-phenotype data,
neuroanatomy or pizzas.

Alpha software: API may change

## Python Examples

### Neighbour Query

```
from scigraph.api.SciGraph import SciGraph

sg = SciGraph("http://datagraph.monarchitiative.org/")
g = sg.neighbors('OMIM:118300',{'depth':1})
for n in g.nodes:
  print(n.id +" " + n.label)
for e in g.edges:
  print(n.subject +" " + e.predicate + " " + e.target)
```
    
## Command Line Examples

For up to date help, always use:

    ./run-scigr.py -h

The most useful global parameter is `-u` which sets the base URL

### Autocomplete

    ./run-scigr.py  a Parkinson

### Search

    ./run-scigr.py  s Parkinson

### Annotation

    ./run-scigr.py ann "the big ears and the hippocampus neurons"

### Neighbors

    ./run-scigr.py -t tsv  n OMIM:118300

### Graph Visualization

    ./run-scigr.py -t png  g OMIM:118300


