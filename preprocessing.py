#the purpose of the script is to generate 6 csv files for classification.
#3 training and 3 testing.

from sklearn.preprocessing import normalize
from scikits.talkbox.features import mfcc
from matplotlib.pyplot import specgram
from sklearn.decomposition import PCA
import scipy.io.wavfile as wv
import soundfile as sf
import numpy as np
import scipy
import pywt
import csv
import os

#processing training file
outfile = open("training1.csv", 'wb')
outputWriter = csv.writer(outfile)
outfile2 = open("training2.csv", 'wb')
outputWriter2 = csv.writer(outfile2)
outfile3 = open("training3.csv", 'wb')
outputWriter3 = csv.writer(outfile3)

# read training music files
feature3data=[]
labels=[]
current, dirs, files = os.walk('./genres/').next()
for dir in dirs:
	current, dirs2, files2 = os.walk('./genres/'+dir).next()
	print dir
	for f in files2:
		if f !='.DS_Store':
			print f
			labels.append(dir)
			data, samplerate = sf.read('./genres/'+dir+'/'+f)
			data=normalize(data[:,np.newaxis],axis=1).ravel()
			
			#feature 1: fft
			x=abs(scipy.fft(data)[:1000])
			outputWriter.writerow(np.append(x[:1000],dir))
			
			#feature 2: MFCC
			ceps,mspec,spec=mfcc(data)
			num_ceps=ceps.shape[0]
			y=np.mean(ceps[int(num_ceps/10): int(num_ceps*9/10)],axis=0)
			y=np.nan_to_num(y)
			outputWriter2.writerow(np.append(y,dir))
			
			# feature 3: DWT
			(cA, cD) = pywt.dwt(data,'haar')
			feature3data.append(abs(cA[:10000]))
			#outputWriter3.writerow(np.append(abs(cA)[:1000],dir))
feature3data=np.array(feature3data)
pca = PCA(n_components=500)
feature3data = pca.fit_transform(feature3data);		
for i in range(feature3data.shape[0]):
	outputWriter3.writerow(np.append(feature3data[i],labels[i]))



#processing testing file
outfile = open("testing1.csv", 'wb')
outputWriter = csv.writer(outfile) 
outfile2 = open("testing2.csv", 'wb')
outputWriter2 = csv.writer(outfile2)
outfile3 = open("testing3.csv", 'wb')
outputWriter3 = csv.writer(outfile3)


#read testing music files
feature3datatest=[]
path = "./validate/"
dirs = os.listdir(path)
for f in dirs:
	if f !='.DS_Store':
		data, samplerate = sf.read(path+f)

		# testing file using FFT
		data=normalize(data[:,np.newaxis],axis=1).ravel()
		x=abs(scipy.fft(data)[:1000])
		outputWriter.writerow(x[:1000])

		# testing file using MFCC
		ceps,mspec,spec=mfcc(data)
		num_ceps=ceps.shape[0]
		y=np.mean(ceps[int(num_ceps/10): int(num_ceps*9/10)],axis=0)
		y=np.nan_to_num(y)
		outputWriter2.writerow(y)

		# testing file to be used for DWT & PCA
		compressed, (a, b, c) = pywt.dwt2(data,'haar')
		feature3datatest.append(abs(compressed[:10000]))
		#outputWriter3.writerow(np.abs(cA[:1000]))
feature3datatest=np.array(feature3datatest)
print feature3datatest.shape
feature3datatest = pca.transform(feature3datatest)
print feature3datatest.shape
for i in range(feature3datatest.shape[0]):
	outputWriter3.writerow(feature3datatest[i])
