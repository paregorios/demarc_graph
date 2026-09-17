# Extract RDF from my dissertation XML (which was built with MSWord)

FYI: notebooks in notebooks directory are not up-to-date; used as scratch/experimentation. 

## What it does

As of 17 September 2026, the latest working code in the package does the following by parsing the original XML and constructing triples, which are then serialized to TTL using rdflib:

### Demarcation instances

These are cases where we know there was some kind of formal demarcation of boundaries.

```turtle
demarc:INST100 a demarc:DemarcationInstance ;
    rdfs:label "Boundary Dispute Involving Ardea"@en .

demarc:INST101 a demarc:DemarcationInstance ;
    rdfs:label "Dispute over Site, Ownership and Boundaries between Ostia and Volussius Crocus"@en .

demarc:INST103 a demarc:DemarcationInstance ;
    rdfs:label "Restoration of the Boundaries of the Fields Consecrated to Diana Tifatina"@en .

demarc:INST108 a demarc:DemarcationInstance ;
    rdfs:label "Casting a Spell on the Governor in Hispania"@en ;
    dcterms:references demarc:INST108-ref-1 .
```

### References

Note the addition of a reference on `INST108` in the preceding example. The only references currently being generated are those that relate `Instances` to numbered items discussed in Burton 2000. Additional triples are produced for each reference.

```turtle
demarc:INST108-ref-1 a demarc:Reference ;
    bibo:locator "number 7" ;
    cito:citesAsRelated demarc:work-burton-2000 .
```

### Works Cited

Additional triples for each work cited in one or more references are also written, e.g.:

```turtle
<urn:issn:2510-5396> a bib:Journal ;
    dc:identifier "ISSN 2510-5396" ;
    dc:title "Chiron" .

demarc:work-burton-2000 a bib:Article ;
    prism:volume "30" ;
    dc:date "2000" ;
    dc:title "The Resolution of Territorial Disputes in the Provinces of the Roman Empire" ;
    dcterms:isPartOf <urn:issn:2510-5396> ;
    bib:authors [ a rdf:Seq ;
            rdf:_1 [ a foaf:Person ;
                    foaf:givenName "G.P." ;
                    foaf:surname "Burton" ] ] ;
    bib:pages "195-215" ;
    z:itemType "journalArticle" ;
    z:shortTitle "Burton 2000" .
```

## Roadmap

- [x] entities (base class)
- [x] rdfs:labels
- [x] references
- [x] bibliography / works cited
- [x] instances
    - [x] parse & serialize identifiers
    - [x] parse & serialize labels
    - [x] related Burton references
    - [ ] date ranges
    - [ ] prose descriptions/discussion
- [ ] documents
- [ ] people
- [ ] places
- [ ] technical and legal terminology


## Tests

```
⌘ pytest --log-cli-level DEBUG
```