import requests, zipfile, os, pickle, json, sqlite3

def get_manifest(apiKey):
    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'

    #get the manifest location from the json
    r = requests.get(manifest_url, headers={
        "X-API-Key": apiKey
        })
    manifest = r.json()
    mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']

    #Download the file, write it to 'MANZIP'
    r = requests.get(mani_url)
    with open("MANZIP", "wb") as zip:
        zip.write(r.content)
    print("Download Complete!")

    #Extract the file contents, and rename the extracted file
    # to 'Manifest.content'
    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    os.rename(name[0], 'Manifest.content')
    print('Unzipped!')
    os.remove("MANZIP")


apiKey = input("Enter your api key (If you don't know what Im talking about go to https://www.github.com/TheLLaw/A.-A. and read the readme file):")
get_manifest(apiKey)
