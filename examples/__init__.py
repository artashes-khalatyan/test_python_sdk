from lib.sharedcount_api import SharedCountApi
sharedCountApiInstance = SharedCountApi('YOUR_API_KEY')


# Return share counts for a URL.
var urlGetResponse = sharedCountApiInstance.get(url)

#Post a large number of URLs all at once to calculate bulk social counts.
#Get bulk_id from bulk post response, then using bulkGet to get result
urls = ["urls", "url2"]

bulkPostResponse=sharedCountApiInstance.bulkPost(urls)

bulkId=bulkPostResponse['bulk_id']

bulkResponse=sharedCountApiInstance.bulkGet(bulkId)

#Return historical quota usage information.
usage = sharedCountApiInstance.usage()

#Return information about your quota allocation for the day.
quota = sharedCountApiInstance.quota()

#Return a list of domains added to your domain whitelist, and whether the domain whitelist is currently being enforced.
domainWhiteList = sharedCountApiInstance.getDomainWhiteList()

#Check to see if the SharedCount API is currently up.
status = sharedCountApiInstance.status()

