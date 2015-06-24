OJ_Break API Python Wrapper
===================

A Python wrapper for uses the OJ_Break API. The OJ_Break API provides all of the
granular biodiversity data from the xBio:D database for applications connected to
the xBio:D ecosystem. The wrapper converts the API result into a Python
dictionary that has the same structure and naming as the original data.

# Version
0.1.1	*released 24-Jun-2015*

# Requirements
- Python 2.7+
- xBio:D user account w/ API key activated

# Installation
The easiest way to install the OJ_Break API wrapper is through the *pip* package
management system for Python.

```
pip install oj_break
```

# Usage
To use the python wrapper for the API, load the OJ_Break API wrapper and instantiate
an object with the xBio:D API key for the user, which can be obtained by following
the instructions on the [xBio:D wiki](http://xbiod.osu.edu/wiki/OJ_Break_API_Access).

```python
from oj_break.api import OJ_Break
api = OJ_Break(api_key) # api_key must be replaced with actual key 
```

The OJ_Break API wrapper is partitioned into separate data domains (taxon, literature,
locality, place, agent, journal, occurrence, institution, search) that handle the
respective API calls. Each API call and parameter name is exactly the same as the API
itself.

Here is an example to search for a species, *Eucoila hunteri*, retrieve the taxonomic
hierarchy, then get five occurrence records for the tribe in which the species belongs.

```python
search_results = api.search.getTaxaFromText('Eucoila hunteri')
taxon_hier = api.taxon.getTaxonHierarchy(search_results['data']['taxa'][0]['tnuid'])
taxon_spms = api.taxon.getTaxonOccurrences(taxon_hier['data']['hier']['Tribe']['tnuid'],
		limit=5, show_children=True)
```

The *taxon_spms* variable would look like this:
```python
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(taxon_spms)

'''Pretty Print Output
{   u'code': 100,
    u'data': {   u'general': {   u'guid': u'http://bioguid.osu.edu/xbiod_concepts/307515',
                                 u'taxon': u'Diglyphosematini',
                                 u'taxon_author': u'Belizin',
                                 u'tcid': 204894,
                                 u'tnuid': 307515},
                 u'occurrences': [   {   u'guid': u'http://bioguid.osu.edu/xbiod_occurrences/0EAE5D1A-E146-3AAA-E053-0100007F2CC9',
                                         u'occurrence_id': u'UCFC 0 016 020',
                                         u'unvouchered_coll': u'N',
                                         u'vouchered': u'Y'},
                                     {   u'guid': u'http://bioguid.osu.edu/xbiod_occurrences/0EAE5D1D-81DF-3AAA-E053-0100007F2CC9',
                                         u'occurrence_id': u'UCFC 0 018 672',
                                         u'unvouchered_coll': u'N',
                                         u'vouchered': u'Y'},
                                     {   u'guid': u'http://bioguid.osu.edu/xbiod_occurrences/0EAE5D1D-2218-3AAA-E053-0100007F2CC9',
                                         u'occurrence_id': u'UCFC 0 018 676',
                                         u'unvouchered_coll': u'N',
                                         u'vouchered': u'Y'},
                                     {   u'guid': u'http://bioguid.osu.edu/xbiod_occurrences/0EAE5D1C-63CA-3AAA-E053-0100007F2CC9',
                                         u'occurrence_id': u'UCFC 0 019 978',
                                         u'unvouchered_coll': u'N',
                                         u'vouchered': u'Y'},
                                     {   u'guid': u'http://bioguid.osu.edu/xbiod_occurrences/0EAE5D0A-C306-3AAA-E053-0100007F2CC9',
                                         u'occurrence_id': u'UCRC ENT 196933',
                                         u'unvouchered_coll': u'N',
                                         u'vouchered': u'Y'}]},
    u'message': u'API resource successfully retrieved'}
'''
```

For a list of all of the API calls and return class structure of the data, visit the
[OJ_Break API reference](http://xbiod.osu.edu/wiki/OJ_Break_Version_2_API_Reference)
on the xBio:D wiki.

# Bug Reporting
If you find any bugs with this package or the underlying API, please submit a bug report
to the [GitHub project](http://google.com) or contact Joe Cora <cora.1@osu.edu>.
