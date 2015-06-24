# -*- coding: utf-8 -*-

import json
import inspect

# Python version-dependent imports
try:
	import urllib.request as urllib2
	from urllib.parse import urlencode
except ImportError:
	import urllib2
	from urllib import urlencode

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
		
		# Encode parameters, convert to binary, and send request
		api_parameters = urlencode(api_parameters)
		encoded_api_params = api_parameters.encode('utf-8')
		
		db_req = urllib2.Request('http://xbiod.osu.edu/OJ_Break/' + api_call, encoded_api_params)
		db_resp = urllib2.urlopen(db_req)
		
		json_resp = db_resp.read()
		json_resp = json_resp.decode('utf-8')
		
		# Decode the JSON response
		try:
			dict_resp = json.loads(json_resp)
		except:
			raise ValueError('The OJ_Break API response could not be converted into local dictionary!')
		
		# Return the response
		return dict_resp
