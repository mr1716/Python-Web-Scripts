#!/usr/bin/env python
#Author: Mike R
#Download Chrome Extensions using Chrome API
import urllib

#Can also ask the user to provide with data, or read in from file
extension="chlffgpmiacpedhhbkiomidkjlcfhogd"

#URL to download from
url="https://clients2.google.com/service/update2/crx?response=redirect&prodversion=38.0&x=id%3D" + extension +"%26installsource%3Dondemand%26uc" 

#downloading using urllib and naming the file after the extension downloaded
urllib.urlretrieve(url, extension + ".crx")

#Next steps would be to rename the extension from the ID.crx to extensionName.zip and examine files.
