<strong>Music Classification</strong></br>
</br>
In this project our task is to sort music files according to the genre into different folders such as jazz, classical, country and metal. We use the GTZAN dataset, which is frequently used to benchmark music genre classification tasks. It is organized into 10 distinct genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, and rock. The dataset contains the first 30 seconds of 100 songs per genre.</br>
We plot the spectrogram for these first 30 seconds of diverse wave files, we can see that there are commonalities between songs of the same genre:</br>
<img width="546" alt="123" src="https://user-images.githubusercontent.com/10619083/37260939-d5c1464c-255d-11e8-982c-bc06823bf1da.png"></br>
</br>
We tried feature extraction techniques like Fast Fourier Transform, Mel Frequency Cepstral Coefficients and Descrete Wavelet Transform. We used Gaussian Naive Bayes and Support Vector Machine as the classifiers.</br>
</br>
The libraries we used are: scikits.talkbox, sklearn and matplotlib. Weka and Orange are also applied to help testing the data.








