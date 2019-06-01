## Environment Setup:
This project uses the PySpark Python library, which requires Java 8 to run. Most machines have a newer version of Java installed. To set up your environment to run this application, you must install an open source version of JDK 8. From there, you must reference the JDK 8 path within the .ipynb file:
1. ! apt-get install openjdk-8-jdk-headless
2. ! sudo update-alternatives --config javac 
3. ! sudo update-java-alternatives --set /path/to/your/JDK8/install

## Project Description:
My project incorporated a dataset of 4 Million random Amazon reviews used to train and test my algorithm's accuracy at predicting whether a user review is positive or negative. The algorithm was trained no a dataset of 3.6 Million reviews and tested on a dataset of 400,000 reviews. Both datasets excluded 3-star reviews since they are considered 'neutral' in sentiment. Both files consisted therefore of either negative 1-2 star reviews, or positive 4-5 star reviews. 
The first step required that I convert the .txt files into .csv files. I read in the text files using Jupyter Notebooks and used the Pandas Library. I then uploaded the clean .csv files to AWS cloud storage for faster processing. Using Google Colab python notebooks, I read in the files from AWS using the python PySpark library, which is a python version of spark. Spark is a distributed data processing engine, as well as a machine learning library. I decided to use Google Colab rather than Jupyter Notebooks because you can modify the notebook’s environment without potentially modifying your whole computer's environment. This was crucial to being able to work with PySpark because this library is compatible with Java 8, and not Java 11, which is currently installed on my computer. 
 
 
##### To build my sentiment analysis algorithm, I needed to preprocess the data by:
 
- Tokenizing the words in each comment; in other words, creating a list of words for each comment.
- Removing stop words such as "and" or "the".
- Performing NLP hashing to create an index for each word and each word's frequency.
- Term Frequency / Inverse Document Frequency to get the tf-idf weight/importance of each word to the training document.
- Separate the comments class (negative as 1, positive as 2) from the comments column, into its own 'label' column. The 'label' column is necessary to implement the Naive Bayes model.
- Using PySpark's Naive Bayes Machine Learning Classification Model on the training data.
 
The final step was transforming the model onto the test data, to evaluate its accuracy. The accuracy of the model at predicting review sentiment was 82.782%.



## Challenges:

I learned a lot from this project. The first thing I will do next time I start a project is to check for compatibility.  Whether it’s between python libraries, between libraries and Operating Systems, or between libraries and integrated software like Java. This step could have saved me many headaches. 

```
Unsupported class file major version 55 error 
```

It turns out that PySpark is incompatible with Java 8. If I tried to install Java 8 from Oracle, it would not let me since it would detect a higher version already installed on my machine. I tried to brew cask install Java 8, but there was no Java 8 cask. I searched high and low until I found an open source version of a JDK 8 cask which performed exactly like Java 8. By working with a Google Colab notebook, I was able to set the Java version to Java 8 specifically for that notebook. This resolved my issues with PySpark and Java. 

```
Unable to load native-hadoop library for your platform
```

Spark’s native hadoop library is supported on *nix platforms only. The platform does not work with the Mac OS X Platform. 
*Essentially whenever I tried to combine PySpark with my FLASK app, it produced this error. Building the ML Algorithm with PySpark worked fine. Passing it into a button ‘on-click’ event through flask proved impossible.*

> https://stackoverflow.com/questions/52201242/apache-spark-unable-to-load-native-hadoop-library-for-your-platform-using-bu


## Datasets:

Training Data
Link TBD (Current uploading to Google Drive)

Test Data
https://drive.google.com/file/d/1YPFlEDj2gG7ImYQ1rGQApW9bxq4UT9Wp