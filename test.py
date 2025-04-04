from search import getUrl

results = getUrl("thunder saga epic")

if results:
    print(results[0]["url"])
