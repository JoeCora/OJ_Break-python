# -*- coding: utf-8 -*-

from __future__ import print_function

import urllib
import urllib2
import json
import inspect

# OJ_Break class
class OJ_Break(object):
	'''
		The OJ_Break API wrapper for handling OJ_Break API interactions with the xBio:D database
		
		An xBio:D API key is required to use this API. More information on the xBio:D wiki: http://xbiod.osu.edu/wiki/OJ_Break_Version_2_API_Reference
	'''
	# Attributes ################
	taxon = None
	literature = None
	locality = None
	place = None
	agent = None
	journal = None
	occurrence = None
	institution = None
	search = None
	
	_api_key = None
	_limit = 1000
	
	# Functions #################
	## Constructor / Destructor / Etc. ##
	def __unicode__(self):
		return 'OJ_Break API; Key: ' + str(self._api_key)
	
	def __init__(self, api_key=None, limit=None):
		# Make sure that an API key to specified
		if api_key is None:
			raise ValueError('An API key must be defined!')
		
		if limit is not None:
			self._limit = limit
		
		# Set public and protected class variables
		self.taxon = self.__Taxon(self)
		self.literature = self.__Literature(self)
		self.locality = self.__Locality(self)
		self.place = self.__Place(self)
		self.agent = self.__Agent(self)
		self.journal = self.__Journal(self)
		self.occurrence = self.__Occurrence(self)
		self.institution = self.__Institution(self)
		self.search = self.__Search(self)
		
		self._api_key = api_key
	
	## Private Domain Classes ##
	### Base ###
	class __Base(object):
		# Attributes ################
		_parent = None
		
		def __init__(self, parent=None):
			# Make sure a parent class is specified
			if parent is None:
				raise ValueError('An OJ_Break Base class must have an OJ_Break parent object defined!')
			
			self._parent = parent
	
	### Taxon ###
	class __Taxon(__Base):
		def getTaxonInfo(self, tnuid, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonHierarchy(self, tnuid):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonIncludedTaxa(self, tnuid, offset=0, limit=None, show_syns=False, show_fossils=True, rank=None, inst_id=None, types_only=False):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonSynonyms(self, tnuid, offset=0, limit=None, show_fossils=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonAssociations(self, tnuid, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonLiteratureCitations(self, tnuid, offset=0, limit=None, show_children=False):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonOccurrences(self, tnuid, offset=0, limit=None, basic_only=True, show_children=False, inst_id=None, place_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonTypes(self, tnuid, offset=0, limit=None, basic_only=True, show_children=False, inst_id=None, primary_only=False):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonLocalities(self, tnuid, offset=0, limit=None, show_children=False, inst_id=None, place_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonDeterminers(self, tnuid, offset=0, limit=None, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonInstitutions(self, tnuid, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonHabitats(self, tnuid, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxonMedia(self, tnuid, offset=0, limit=None, media_type=None, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Literature ###
	class __Literature(__Base):
		def getLiteratureInfo(self, pub_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getLiteratureParts(self, pub_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getLiteratureTaxonCitations(self, pub_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getLiteratureAssocCitations(self, pub_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getCitationInfo(self, citation_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Locality ###
	class __Locality(__Base):
		def getLocalityInfo(self, loc_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getLocalityOccurrences(self, loc_id, offset=0, limit=None, basic_only=True, tnuid=None, show_children=False, inst_id=None, place_id=None, agent_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Place ###
	class __Place(__Base):
		def getPlaceInfo(self, place_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getPlaceSubdivisions(self, place_id, offset=0, limit=None, pol_level=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getPlaceTaxa(self, place_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getPlaceOccurrences(self, place_id, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getPlaceInstitutions(self, place_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Agent ###
	class __Agent(__Base):
		def getAgentInfo(self, agent_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getAgentLiterature(self, agent_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getAgentTaxa(self, agent_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getAgentOccurrences(self, agent_id, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Journal ###
	class __Journal(__Base):
		def getJournalInfo(self, journal_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getJournalLiterature(self, journal_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getJournalTaxa(self, journal_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Occurrence ###
	class __Occurrence(__Base):
		def getOccurrenceInfo(self, occurrence_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getOccurrencesInfo(self, occurrence_ids):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Institution ###
	class __Institution(__Base):
		def getInstitutionInfo(self, inst_id):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionLiterature(self, inst_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionTaxa(self, inst_id, offset=0, limit=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionOccurrences(self, inst_id, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionPrimaryTypes(self, inst_id, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionSecondaryTypes(self, inst_id, offset=0, limit=None, basic_only=True):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	### Search ###
	class __Search(__Base):
		def getSearchResults(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, domains=None, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getTaxaFromText(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getOccurrencesFromText(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getAgentsFromText(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, include_party=True, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getInstitutionsFromText(self, search, offset=0, limit=None, case_sensitive=False):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getJournalsFromText(self, search, offset=0, limit=None, case_sensitive=False):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getPlacesFromText(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
		
		def getLocalitiesFromText(self, search, offset=0, limit=None, basic_only=True, case_sensitive=False, inst_id=None):
			# Process and send off call, then return results in dictionary (all parameters and values are sent to process)
			return self._parent._process_api(inspect.currentframe())
	
	## Protected Functions ##
	def _process_api(self, frame):
		# Get the API call name
		api_call = inspect.getframeinfo(frame)[2]
		
		# Get the parameters and parameter values
		params, _, _, param_values = inspect.getargvalues(frame)
		
		# Place the parameters into a parameter dictionary (skip 1st parameter => self)
		api_parameters = dict()
		
		for param_key in params[1:]:
			api_parameters[param_key] = param_values[param_key]
		
		# Send off call and return results in dictionary
		return self._send_api(api_call, api_parameters)
	
	def _send_api(self, api_call, api_parameters):
		# Add API key and explicitly add format and version to the parameters
		api_parameters['key'] = self._api_key
		api_parameters['format'] = 'json'
		api_parameters['version'] = 2
		
		# Replace limit variable with default if undefined
		if 'limit' in api_parameters and api_parameters['limit'] is None:
			api_parameters['limit'] = self._limit
		
		# Go through each parameter and replace Python values with OJ_Break expected values
		##	None => ''; True => 'Y'; False => 'N'
		for param_key, param_value in list(api_parameters.items()):
			# Reformat values for API
			if param_value is None:
				api_parameters[param_key] = ''
			elif param_value is True:
				api_parameters[param_key] = 'Y'
			elif param_value is False:
				api_parameters[param_key] = 'N'
		
		# Encode parameters and send request
		api_parameters = urllib.urlencode(api_parameters)
		
		db_req = urllib2.Request('http://xbiod.osu.edu/OJ_Break/' + api_call, api_parameters)
		db_resp = urllib2.urlopen(db_req)
		
		json_resp = db_resp.read()
		
		# Decode the JSON response
		try:
			dict_resp = json.loads(json_resp)
		except:
			return None
		
		# Return the response
		return dict_resp
	
# Test code from command line with user API key (python api.py api_key)
if __name__ == '__main__':
	# Get API key from the command line
	import sys
	
	api_key = None
	
	try:
		api_key = sys.argv[1:2][0]
	except:
		print('Failure getting command line argument')
	
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
			print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + call.func_name + __ColorChars.END, __ColorChars.RED + 'FAILED [' + str(e) + ']' + __ColorChars.END, str(call_count) + '/' + str(len(testing))))
			
			error_count += 1
		else:
			if test_data['code'] > 100:
				# API failure
				print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + call.func_name + __ColorChars.END, __ColorChars.RED + 'FAILED [API Code: ' + str(test_data['code']) + ']' + __ColorChars.END, str(call_count) + '/' + str(len(testing))))
				
				error_count += 1
			else:
				# Success
				print('{2:<7} {0:<50}{1}'.format(__ColorChars.BOLD + call.func_name + __ColorChars.END, 'PASSED', str(call_count) + '/' + str(len(testing))))
				
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
