"""from giphypop import search
g = giphypop.Giphy(api_key=ArJf7WEbSsinMVRarXZoXn97gZhvsAau)
img = translate('foo')
img.url"""
import urllib.request as ur
import json
data = json.loads(ur.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=ArJf7WEbSsinMVRarXZoXn97gZhvsAau&limit=5").read())
print(json.dumps(data, sort_keys=True, indent=4))
