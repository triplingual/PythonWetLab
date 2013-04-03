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
    	id_list = match.group( 1 ).strip( ',' )
        values = id_list.split( "," )
    else:
        values = []

    return values


""" Main routine, fetches single record from Orbis. Currently hardcoded for http://hdl.handle.net/10079/bibid/4916240
"""
# Works directly -->
# orbis_url = "http://hdl.handle.net/10079/bibid/4916240"
"""
Notes:
Using orbis_url = "http://orbexpress.library.yale.edu/vwebv/holdingsInfo" and adding a payload parm of "bibid": "4916240" returns a page claiming that "The Orbis OPAC is unavailable . . ."
I've left in the original searchArg of new+haven to show that this difference (removing the +) was crucial in actually returning results. My guess is that the requests library re-encoded the + as %2b so that Orbis thought it was looking for the phrase 'new+haven' rather than 'new haven'.
"""
# Returning results of a search
orbis_url = "http://orbexpress.library.yale.edu/vwebv/search"

# Construct GET query parameters
#
payload = {
#	"searchArg": "new+haven",
	"searchArg1": "new haven",
	"argType1": "phrase",
	"searchCode1": "SKEY",
	"combine2": "and",
	"searchArg2": "",
	"argType2": "all",
	"searchCode2": "GKEY",
	"combine3": "and",
	"searchArg3": "",
	"argType3": "all",
	"searchCode3": "GKEY",
	"year": "2012-2013",
	"fromYear": "",
	"toYear": "",
	"location": "all",
	"place": "all",
	"type": "all",
	"medium": "all",
	"language": "all",
	"recCount": "500",
	"searchType": "2",
	"page.search.search.button": "Search"
}

response = requests.get( orbis_url, params=payload )
# For testing, gets just one record
# response = requests.get( orbis_url )

# print response.text
# print response.url

# store bibids
bibid_list = get_bibids_from_xml( response.text )

# next steps:
# - how to get the next set of results? (Orbis fails somewhere between 500 and 1000 records requested, so we'll have to page through them)
# - what to do after that? We'll have to iterate through the collection, building handle.net URIs to then scrape for location of publication
# - how to handle bad data? Many of the subjects with "new haven" in them refer to mss in Beinecke rather than a text that is about New Haven.
