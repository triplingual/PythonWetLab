from pattern.web import URL, Node, DOM
import requests
import re

def get_bibids_from_xml(xml_body):
    """ Returns a list of all pubmed ids for articles in an API response,
        like those that follow:
        <Id>17564794</Id>
        <Id>17550787</Id>
        <Id>17544337</Id>
    """
    id_re = re.compile('<input\s+value\="([^"]+)" type="hidden" name="pageIds">')
    match = id_re.search(xml_body)
    if match:
        values = match.group( 1 ).split( "," )
    else:
        values = []

    return values


""" Main routine, fetches single record from Orbis. Currently hardcoded for http://hdl.handle.net/10079/bibid/4916240
"""
# Works directly -->
# orbis_url = "http://hdl.handle.net/10079/bibid/4916240"
"""
Note that using orbis_url = "http://orbexpress.library.yale.edu/vwebv/holdingsInfo" and adding a payload parm of 	"bibid": "4916240" returns a page claiming that "The Orbis OPAC is unavailable . . ."
"""
# Returning results of a search
orbis_url = "http://orbexpress.library.yale.edu/vwebv/search"

# Construct GET query parameters
#
payload = {
	"searchArg": "trainspotting",
	"searchCode": "GKEY^*",
	"limitTo": "none",
	"recCount": "50",
	"searchType": "1",
	"page.search.search.button": "Search"
#	"searchArg1": "New+Haven",
#	"argType1": "phrase",
#	"searchCode1": "SKEY",
#	"year": "2012-2013",
#	"location": "all",
#	"place": "all",
#	"type": "all",
#	"medium": "all",
#	"language": "all",
#	"recCount": "50",
#	"searchType": "2",
#	"page.search.search.button": "Search"
}

response = requests.get( orbis_url, params=payload )
# For testing, gets just one record
# response = requests.get( orbis_url )

# print response.text

print get_bibids_from_xml( response.text )
