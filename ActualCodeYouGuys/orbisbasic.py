from pattern.web import URL, Node, DOM

url = URL( string='http://orbis.library.yale.edu/vwebv/search', method='GET', query={'searchArg1':'new+haven','argType1':'all','searchCode1':'SKEY','year':'2012-2013','location':'all','place':'all','type':'all','medium':'all','language':'all','recCount':'50','searchType':'2','page.search.search.button':'Search'} )

if ( url.exists ):
	print url.querystring

thePage = DOM( url.download() )
# print DOM( url.download() )

for input in thePage.by_tag( 'input' ):
	if ( input.attributes.get( 'type' ) == 'hidden' ):
		print 'hidden input content = '+input.attributes.get( 'value' )


newUrl = URL( string='http://orbexpress.library.yale.edu/vwebv/holdingsInfo', method='GET', query={'bibid':'8394320'} )
print newUrl.headers
theNewPage = DOM( newUrl.download() )
print theNewPage.title
