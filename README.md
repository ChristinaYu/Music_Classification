</strong>Music Classification</strong></br>
</br>
In this project our task is to sort music files according to the genre into different folders such as jazz, classical, country and metal. We use the GTZAN dataset, which is frequently used to benchmark music genre classification tasks. It is organized into 10 distinct genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, and rock. The dataset contains the first 30 seconds of 100 songs per genre.</br>
If we plot the spectrogram for these first 30 seconds of diverse wave files, we can see that there are commonalities between songs of the same genre:
![plot](Desktop/123.png)


1.Preprocessing.py may take up to 20 minutes as the training file is large. It will generate 6 csv files for classification using FFT, MFCC and DWT as the feature extraction methods.The outputs are training1, 2, 3 and testing1, 2, 3. Then run classify.py with those outputs for classification.</br>
</br>
2. The libraries we used are: scikits.talkbox, sklearn and matplotlib. Weka and Orange are also applied to help testing the data.







