import nltk
import numpy
import scipy
import sklearn


import urllib
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.request.urlretrieve(url, filename="../enron_mail_20150507.tar.gz") 

import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print("you're ready to go!")