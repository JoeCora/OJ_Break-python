# -*- coding: utf-8 -*-

from __future__ import print_function

from api import OJ_Break

# Test code from command line with user API key (python oj_break/tests.py api_key)
if __name__ == '__main__':
	# Get API key from the command line
	import sys
	
	api_key = None
	
	try:
		api_key = sys.argv[1:2][0]
	except:
		print('Failure getting command line argument')
		
		sys.exit(1)
	
	# Function to retrieve function name (different in Python 3 from Python 2)
	def __get_func_name(func_in):
		func_name = None
		
		try:
			func_name = func_in.func_name
		except:
			func_name = func_in.__name__
		
		return func_name
	
	# Create local color class for testing
	class __ColorChars:
		PURPLE = '\033[95m'
		CYAN = '\033[96m'
		DARKCYAN = '\033[36m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		END = '\033[0m'
	
	# Show testing preamble
	print()
	print()
	print('=== OJ_BREAK API TEST ===')
	print()
	
	# Create OJ_Break object using API key from command line
	api = OJ_Break(api_key)
	
	# Setup testing input
	testing = {
		api.taxon.getTaxonInfo: {'tnuid': 451},
		api.taxon.getTaxonHierarchy: {'tnuid': 451},
		api.taxon.getTaxonIncludedTaxa: {'tnuid': 451},
		api.taxon.getTaxonSynonyms: {'tnuid': 451},
		api.taxon.getTaxonAssociations: {'tnuid': 451},
		api.taxon.getTaxonLiteratureCitations: {'tnuid': 451},
		api.taxon.getTaxonOccurrences: {'tnuid': 451},
		api.taxon.getTaxonTypes: {'tnuid': 451},
		api.taxon.getTaxonLocalities: {'tnuid': 451},
		api.taxon.getTaxonDeterminers: {'tnuid': 451},
		api.taxon.getTaxonInstitutions: {'tnuid': 451},
		api.taxon.getTaxonHabitats: {'tnuid': 451},
		api.taxon.getTaxonMedia: {'tnuid': 451},
		api.literature.getLiteratureInfo: {'pub_id': 95},
		api.literature.getLiteratureParts: {'pub_id': 95},
		api.literature.getLiteratureTaxonCitations: {'pub_id': 95},
		api.literature.getLiteratureAssocCitations: {'pub_id': 95},
		api.literature.getCitationInfo: {'citation_id': 18763},
		api.locality.getLocalityInfo: {'loc_id': 57815},
		api.locality.getLocalityOccurrences: {'loc_id': 57815},
		api.place.getPlaceInfo: {'place_id': 3769},
		api.place.getPlaceSubdivisions: {'place_id': 3769},
		api.place.getPlaceTaxa: {'place_id': 3769},
		api.place.getPlaceOccurrences: {'place_id': 3769},
		api.place.getPlaceInstitutions: {'place_id': 3769},
		api.agent.getAgentInfo: {'agent_id': 15631},
		api.agent.getAgentLiterature: {'agent_id': 15631},
		api.agent.getAgentTaxa: {'agent_id': 15631},
		api.agent.getAgentOccurrences: {'agent_id': 15631},
		api.journal.getJournalInfo: {'journal_id': 23},
		api.journal.getJournalLiterature: {'journal_id': 23},
		api.journal.getJournalTaxa: {'journal_id': 23},
		api.occurrence.getOccurrenceInfo: {'occurrence_id': 'OSUC 181529'},
		api.occurrence.getOccurrencesInfo: {'occurrence_ids': 'OSUC 181529,OSUC 181412,OSUC 148294'},
		api.institution.getInstitutionInfo: {'inst_id': 323},
		api.institution.getInstitutionLiterature: {'inst_id': 323},
		api.institution.getInstitutionTaxa: {'inst_id': 323},
		api.institution.getInstitutionOccurrences: {'inst_id': 323},
		api.institution.getInstitutionPrimaryTypes: {'inst_id': 323},
		api.institution.getInstitutionSecondaryTypes: {'inst_id': 323},
		api.search.getSearchResults: {'search': 'Masner%'},
		api.search.getTaxaFromText: {'search': 'Masner%'},
		api.search.getOccurrencesFromText: {'search': 'Masner%'},
		api.search.getAgentsFromText: {'search': 'Masner%'},
		api.search.getInstitutionsFromText: {'search': 'Masner%'},
		api.search.getJournalsFromText: {'search': 'Masner%'},
		api.search.getPlacesFromText: {'search': 'Masner%'},
		api.search.getLocalitiesFromText: {'search': 'Masner%'},
	}
	
	# Loop through each test case and test API call
	call_count = 1
	passed_count = 0
	error_count = 0
	
	for call, params in list(testing.items()):
		try:
			test_data = call(**params)
		except BaseException as e:
			# Execution failure
			print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + __get_func_name(call) + __ColorChars.END, __ColorChars.RED + 'FAILED [' + str(e) + ']' + __ColorChars.END, str(call_count) + '/' + str(len(testing))))
			
			error_count += 1
		else:
			if test_data['code'] > 100:
				# API failure
				print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + __get_func_name(call) + __ColorChars.END, __ColorChars.RED + 'FAILED [API Code: ' + str(test_data['code']) + ']' + __ColorChars.END, str(call_count) + '/' + str(len(testing))))
				
				error_count += 1
			else:
				# Success
				print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + __get_func_name(call) + __ColorChars.END, 'PASSED', str(call_count) + '/' + str(len(testing))))
				
				passed_count += 1
		
		call_count += 1
	
	print()
	
	# Output the final testing results
	if error_count > 0:
		print('Testing Results: ' + __ColorChars.RED + __ColorChars.BOLD + 'FAILED' + __ColorChars.END + ' (' + str(error_count) + ' calls)' + __ColorChars.END)
		print()
		
		# Error exit
		sys.exit(1)
	else:
		print('Testing Results: ' + __ColorChars.BOLD + 'PASSED' + __ColorChars.END)
		print()
		
		# Success exit
		sys.exit()