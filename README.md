# Extract RDF from my dissertation XML (which was built with MSWord)

FYI: notebooks in notebooks directory are not up-to-date; used as scratch/experimentation. 

As of 16 September 2026, the latest working code in the package does this by parsing the original XML and constructing triples, which are then serialized to TTL using rdflib:

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


## Pytests

```
⌘ pytest --log-cli-level DEBUG
============================================================ test session starts =============================================================
platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/paregorios/Documents/files/D/demarc_graph
configfile: pyproject.toml
plugins: anyio-4.15.1
collected 8 items                                                                                                                            

tests/test_entities.py::TestLabel::test_label PASSED                                                                                   [ 12%]
tests/test_entities.py::TestLabel::test_label_fr PASSED                                                                                [ 25%]
tests/test_entities.py::TestLabel::test_label_bad_lang PASSED                                                                          [ 37%]
tests/test_entities.py::TestEntity::test_init PASSED                                                                                   [ 50%]
tests/test_entities.py::TestEntity::test_id_bad PASSED                                                                                 [ 62%]
tests/test_entities.py::TestEntity::test_label PASSED                                                                                  [ 75%]
tests/test_entities.py::TestEntity::test_labels PASSED                                                                                 [ 87%]
tests/test_extractor.py::TestExtractor::test_init 
--------------------------------------------------------------- live log call ----------------------------------------------------------------
DEBUG    TestExtractor:test_extractor.py:27 extracted 106 instances
DEBUG    TestExtractor:test_extractor.py:30 INST157: Q. Articuleius Regulus Adjudicates a Boundary Dispute in Lusitania
DEBUG    TestExtractor:test_extractor.py:30 INST115: The Koinon of Thessaly Assists a Roman Proconsul
DEBUG    TestExtractor:test_extractor.py:30 INST17: Restoration of Boundaries or Boundary Markers between Corinium and Nedinum
DEBUG    TestExtractor:test_extractor.py:30 INST147: Boundary Dispute between Vegium and Ortopla
DEBUG    TestExtractor:test_extractor.py:30 INST155: Verdict of P. Cornelius Dolabella
DEBUG    TestExtractor:test_extractor.py:30 INST186: Boundary Dispute Involving the Sal(tus) te(rritorii) Ta(rionae)
DEBUG    TestExtractor:test_extractor.py:30 INST60: Boundary Dispute between Nerate and Oneum
DEBUG    TestExtractor:test_extractor.py:30 INST151: Boundary Dispute between Nedinum and an Unknown Party
DEBUG    TestExtractor:test_extractor.py:30 INST61: Iudices dati in Dalmatia
DEBUG    TestExtractor:test_extractor.py:30 INST76: Disputes Related to the Temple of Artemis Limnatis
DEBUG    TestExtractor:test_extractor.py:30 INST166: Boundary Dispute between Damascus and Sidon
DEBUG    TestExtractor:test_extractor.py:30 INST154: Restoration of Boundaries between Nerate and Pituntium
DEBUG    TestExtractor:test_extractor.py:30 INST63: Boundary dispute between the Sapuates and Aemate
DEBUG    TestExtractor:test_extractor.py:30 INST165: Boundary Dispute between Peraia and Philadelphia
DEBUG    TestExtractor:test_extractor.py:30 INST54: Dispute between the Comenses and Bergalei
DEBUG    TestExtractor:test_extractor.py:30 INST21: Horothesia of Histria
DEBUG    TestExtractor:test_extractor.py:30 INST141: Negotiated Settlement between Corinium and Ansium(?)
DEBUG    TestExtractor:test_extractor.py:30 INST112: Boundary Disputes between Thasos and Philippi?
DEBUG    TestExtractor:test_extractor.py:30 INST142: Boundary Dispute between Asseria and Alveria
DEBUG    TestExtractor:test_extractor.py:30 INST95: Iudex datus in Dalmatia
DEBUG    TestExtractor:test_extractor.py:30 INST6: Violent Boundary Dispute between Oea and Lepcis Magna
DEBUG    TestExtractor:test_extractor.py:30 INST62: Dispute between the Patulcenses and Galillenses
DEBUG    TestExtractor:test_extractor.py:30 INST86: Boundary Dispute between Mopsouestia and Aegae
DEBUG    TestExtractor:test_extractor.py:30 INST99: Boundary Dispute between Histonium and Tillius Sassius
DEBUG    TestExtractor:test_extractor.py:30 INST52: Dispute between the Vanacini and the Mariani
DEBUG    TestExtractor:test_extractor.py:30 INST158: Boundary Dispute Involving Cisimbrium
DEBUG    TestExtractor:test_extractor.py:30 INST57: Boundary Dispute between Capua and Plotius Plebeius on Crete
DEBUG    TestExtractor:test_extractor.py:30 INST9: A Negotiated Boundary between the Zamucci and the Muduciuvi
DEBUG    TestExtractor:test_extractor.py:30 INST114: Restoration of Boundary Established by King Philip between the Bragylai, Tiberioi and Kissynioi
DEBUG    TestExtractor:test_extractor.py:30 INST108: Casting a Spell on the Governor in Hispania
DEBUG    TestExtractor:test_extractor.py:30 INST156: Restoration Following the Map of Dolabella
DEBUG    TestExtractor:test_extractor.py:30 INST148: Boundary Dispute between the Barizaniates and the Lizaviates
DEBUG    TestExtractor:test_extractor.py:30 INST98: Negotiated Settlement of a Boundary Dispute between Olooson and Dion
DEBUG    TestExtractor:test_extractor.py:30 INST118: Boundary Dispute between Doliche and Elimeia
DEBUG    TestExtractor:test_extractor.py:30 INST79: Restoration of boundaries of the Regio Palmyrena
DEBUG    TestExtractor:test_extractor.py:30 INST160: Boundary Dispute Involving Two Villages of Heraclea
DEBUG    TestExtractor:test_extractor.py:30 INST159: Legate Appointed by Proconsul as iudex in a Boundary Dispute in Macedonia
DEBUG    TestExtractor:test_extractor.py:30 INST55: Dispute between the Lamienses and Hypataei
DEBUG    TestExtractor:test_extractor.py:30 INST16: Verdicts of Avidius Nigrinus in Boundary Disputes Concerning Delphi and Neighboring Communities
DEBUG    TestExtractor:test_extractor.py:30 INST56: Dispute between the Sacilienses, Eporenses and Solienses
DEBUG    TestExtractor:test_extractor.py:30 INST29: Possible Boundary Dispute between the Aunobari and Iulius Regillus
DEBUG    TestExtractor:test_extractor.py:30 INST138: Dispute about Site between Daulis and Memmios, son of Antiochos
DEBUG    TestExtractor:test_extractor.py:30 INST66: Disputes Attested on an ‘Archive Wall’ from Coronea
DEBUG    TestExtractor:test_extractor.py:30 INST135: Boundary Dispute between Delphi and Ambryssos
DEBUG    TestExtractor:test_extractor.py:30 INST100: Boundary Dispute Involving Ardea
DEBUG    TestExtractor:test_extractor.py:30 INST14: An Official Demarcation of the Territorial Boundaries of Musti
DEBUG    TestExtractor:test_extractor.py:30 INST113: Boundary Dispute Involving the Pastureland of the Phyle Rodopeis at Philippopolis
DEBUG    TestExtractor:test_extractor.py:30 INST93: Restoration of a Boundary Marker at Smilec
DEBUG    TestExtractor:test_extractor.py:30 INST143: An Altar to Hercules
DEBUG    TestExtractor:test_extractor.py:30 INST119: Possible Boundary Dispute between Valeria Faventina and the Compagani rivi Larensis
DEBUG    TestExtractor:test_extractor.py:30 INST22: Messia Pudentilla and the Vicani Buteridavenses
DEBUG    TestExtractor:test_extractor.py:30 INST64: Boundary markers of the fields of the Bendiparoi
DEBUG    TestExtractor:test_extractor.py:30 INST45: Dispute in vicinity of Calama
DEBUG    TestExtractor:test_extractor.py:30 INST162: Boundary Dispute between the Tiktaenoi and the Sporenoi
DEBUG    TestExtractor:test_extractor.py:30 INST144: Boundary Dispute between Salvia and Stridon
DEBUG    TestExtractor:test_extractor.py:30 INST46: Possible Boundary Dispute between the Thabborenses and the Thimisuenses
DEBUG    TestExtractor:test_extractor.py:30 INST43: Fragmentary Verdict involving Thyateira
DEBUG    TestExtractor:test_extractor.py:30 INST145: Boundary Dispute between Ortopla and Parentium
DEBUG    TestExtractor:test_extractor.py:30 INST150: Unpublished Marker from Dalmatia
DEBUG    TestExtractor:test_extractor.py:30 INST101: Dispute over Site, Ownership and Boundaries between Ostia and Volussius Crocus
DEBUG    TestExtractor:test_extractor.py:30 INST116: Multiple Authoritative Demarcations Involving the Sacred Land of Artemis at Ephesus
DEBUG    TestExtractor:test_extractor.py:30 INST183: Restoration of Roman Public Lands in Cyrenaica
DEBUG    TestExtractor:test_extractor.py:30 INST182: Restoration of Land to Cretan Sanctuary of Aesculapius
DEBUG    TestExtractor:test_extractor.py:30 INST94: Restoration of the praedia publica of Gortyn
DEBUG    TestExtractor:test_extractor.py:30 INST23: Restoration of Public Places at Pompeii
DEBUG    TestExtractor:test_extractor.py:30 INST59: Restoration of Public Lands of the Municipium Canusinum
DEBUG    TestExtractor:test_extractor.py:30 INST103: Restoration of the Boundaries of the Fields Consecrated to Diana Tifatina
DEBUG    TestExtractor:test_extractor.py:30 INST69: Dispute Over Lands Attributed to Zeus the Founder at Aizanoi
DEBUG    TestExtractor:test_extractor.py:30 INST53: Dispute between the Falerienses and the Firmani concerning subseciva
DEBUG    TestExtractor:test_extractor.py:30 INST137: Dispute between Delphi and Thessalia over a harbor
DEBUG    TestExtractor:test_extractor.py:30 INST40: Boundaries assigned to the Suburbures
DEBUG    TestExtractor:test_extractor.py:30 INST72: A Hadrianic Benefaction to Thracian Abdera
DEBUG    TestExtractor:test_extractor.py:30 INST78: Boundaries Assigned to the gens Numidarum
DEBUG    TestExtractor:test_extractor.py:30 INST117: Assignment of Fields, Pastures and Springs in North Africa
DEBUG    TestExtractor:test_extractor.py:30 INST51: Restoration of Boundaries and Immunity of the Thudedenses by the Severi
DEBUG    TestExtractor:test_extractor.py:30 INST77: Field boundaries assigned to the Kasturenses
DEBUG    TestExtractor:test_extractor.py:30 INST185: Authoritative Demarcation of the Boundaries of the regio Palmyrena
DEBUG    TestExtractor:test_extractor.py:30 INST121: Restoration and Renovation of Boundary Markers at Ostippo
DEBUG    TestExtractor:test_extractor.py:30 INST24: Boundary Demarcation Between Sagalassos and Tymbrianassos
DEBUG    TestExtractor:test_extractor.py:30 INST146: Authoritative Demarcation between Asseria and Sidrona
DEBUG    TestExtractor:test_extractor.py:30 INST87: Boundary Demarcations between Cirta and its Neighbors
DEBUG    TestExtractor:test_extractor.py:30 INST120: Demarcations of a praefectura of Ucubis
DEBUG    TestExtractor:test_extractor.py:30 INST25: Redemarcation of the Fossa Regia
DEBUG    TestExtractor:test_extractor.py:30 INST109: Authoritative Demarcation between the Viennenses and the Ceutrones
DEBUG    TestExtractor:test_extractor.py:30 INST39: Re-establishment of Boundary Markers between the Suppenses and Vofricenses
DEBUG    TestExtractor:test_extractor.py:30 INST88: Demarcation between the Public Lands of Philippi and a Private Individual
DEBUG    TestExtractor:test_extractor.py:30 INST8: Restoration of Boundaries between the Nybgenii and the Tacapitani
DEBUG    TestExtractor:test_extractor.py:30 INST97: A Demarcation of the Thracian peraea of Thasos
DEBUG    TestExtractor:test_extractor.py:30 INST4: Demarcations between the Musulamii and their neighbors
DEBUG    TestExtractor:test_extractor.py:30 INST26: Boundary Demarcation between Madauros and Another Party
DEBUG    TestExtractor:test_extractor.py:30 INST168: Authoritative Demarcation between Dorylaion and Another City
DEBUG    TestExtractor:test_extractor.py:30 INST175: Demarcation between Public Land of Philippi and Private Landholders
DEBUG    TestExtractor:test_extractor.py:30 INST83: A Demarcation in Macedonia by D. Terentius Gentianus
DEBUG    TestExtractor:test_extractor.py:30 INST36: Boundary Markers Placed between the Igilgilitani and the Zimizes
DEBUG    TestExtractor:test_extractor.py:30 INST89: Demarcation Between the Moesi and Thraces
DEBUG    TestExtractor:test_extractor.py:30 INST50: inter Regienses et saltum Cu[---]
DEBUG    TestExtractor:test_extractor.py:30 INST163: A Proconsul Demarcates the City of Arykanda
DEBUG    TestExtractor:test_extractor.py:30 INST85: Boundary markers of the territory of the Ausdecenses placed against the Dacians
DEBUG    TestExtractor:test_extractor.py:30 INST90: Procuratorial Demarcation of the agri B[l]aes(iani)
DEBUG    TestExtractor:test_extractor.py:30 INST161: An Authoritative Demarcation in Asia Brings Honor to the Severi
DEBUG    TestExtractor:test_extractor.py:30 INST82: Boundary Demarcation between Unnamed Parties in the Area of Capidava
DEBUG    TestExtractor:test_extractor.py:30 INST180: Authoritative Demarcation on a North African Imperial Estate?INST180
DEBUG    TestExtractor:test_extractor.py:30 INST48: Demarcation between a castellum and the ratio privataINST48
DEBUG    TestExtractor:test_extractor.py:30 INST84: Boundaries Placed between Caesarea ad Libanum and the Gigarteni of the Vicus Sidoniorum
DEBUG    TestExtractor:test_extractor.py:30 INST174: Markers placed by a Freedman Procurator on an Imperial Estate in Phrygia
DEBUG    TestExtractor:test_extractor.py:30 INST184: Authoritative Demarcation of the Balari in Sardinia
PASSED                                                                                                                                 [100%]

============================================================= 8 passed in 0.12s ==============================================================
```