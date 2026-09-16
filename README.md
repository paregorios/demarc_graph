# Extract RDF from my dissertation XML (which was built with MSWord)

FYI: notebooks in notebooks directory are not up-to-date; used as scratch/experimentation. 

As of 16 September 2026, the latest working code in the package does this:
```
⌘ python scripts/generate.py
@prefix demarc: <https://paregorios.org/demarc/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

demarc:INST100 a demarc:DemarcationInstance ;
    rdfs:label "Boundary Dispute Involving Ardea"@en .

demarc:INST101 a demarc:DemarcationInstance ;
    rdfs:label "Dispute over Site, Ownership and Boundaries between Ostia and Volussius Crocus"@en .

demarc:INST103 a demarc:DemarcationInstance ;
    rdfs:label "Restoration of the Boundaries of the Fields Consecrated to Diana Tifatina"@en .

...
```

and

```
⌘ pytest
=================================== test session starts ====================================
platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/paregorios/Documents/files/D/demarc_graph
configfile: pyproject.toml
plugins: anyio-4.15.1
collected 8 items                                                                          

tests/test_entities.py .......                                                       [ 87%]
tests/test_extractor.py .                                                            [100%]

==================================== 8 passed in 0.13s =====================================
``` 

## Roadmap

- [x] instances
    - [x] parse & serialize identifiers
    - [x] parse & serialize labels
    - [ ] date ranges
    - [ ] prose descriptions/discussion
- [ ] documents
- [ ] people
- [ ] places
- [ ] technical and legal terminology
