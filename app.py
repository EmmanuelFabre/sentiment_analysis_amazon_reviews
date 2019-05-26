# based off the instructions on:
# https://stackoverflow.com/questions/43194635/passing-it-a-string-and-running-a-python-script-from-an-html-page






#tldr; create frontend client in JS, backend python server using python framework flask.
from flask import Flask, request, render_template
#below we import everything from the .py file
#from final_project_test_file import *
#from pyspark.sql import SQLContext
#from pyspark import SparkContext 
#do we need the above for flask/pyspark compat ? 
#import pandas as pd


#create an app, being sure to pass __name__ (which represents the name of the python file)
app = Flask(__name__)
#app.debug = True

#@app.route("/test")
#def testing():
#	var_test = "Please"
#	return render_template('test.html')
	#return render_template('test.html', var_test=var_test)

#@app.route("/result", methods=['POST'])
@app.route('/result/')
def script():
	input_string = request.form['data']
	#input_string is the variable that will hold your input string

	####all code below is from the final_project_test_file code regarding input text
	raw_data = {'comments': [input_string]}

#	input_df = pd.DataFrame(raw_data, columns=['comments'])
#	input_df.to_csv("user_input1.csv")

#	path = "user_input1.csv"
	#path = "/Users/emmanuelfabre/Desktop/sentiment_analysis/user_input.csv"
#	spark = SparkSession(sc)
#	spark.sparkContext.addFile(path)
#	spdf = spark.read.option('header', 'true').csv(SparkFiles.get("user_input1.csv"), inferSchema=True, sep=',')

	#tokenize the new spark df
#	tokenizer2 = Tokenizer(inputCol="comments", outputCol="token_words")
	# Transform and show DataFrame
#	tokenized2 = tokenizer2.transform(spdf)

	# Instantiate Remover
#	remover2 = StopWordsRemover(inputCol="token_words", outputCol="filtered")
	# Transform data
#	remover2.transform(tokenized2)
#	tk_stpwrds_df2 = remover2.transform(tokenized2)

	# now we can perform NLP hashing
#	hashing2 = HashingTF(inputCol="filtered", outputCol="hashedValues", numFeatures=pow(2,8))
	# Transform into a DF
#	hashed_df2 = hashing2.transform(tk_stpwrds_df2)

	# Term freq- inverse document frequency.
#	idf2 = IDF(inputCol="hashedValues", outputCol="features")
#	idfModel2 = idf2.fit(hashed_df2)
#	rescaledData2 = idfModel2.transform(hashed_df2)

	# Display the DataFrame w/ original 'comments' col and 'features' col
#	feat_df2 = rescaledData2.select(["comments","token_words", "filtered", "hashedValues", "features"])

	# sqaure brackets slicing method. Write finction on tokens . note in binary chr(34) for "
#	def array_chop(arry):
#		fstring = arry[0]
#		digit = fstring.replace(chr(34),'')
#		return int(digit)

#	chop2 = udf(array_chop, IntegerType())

#	final_df2 = feat_df2.select("token_words", "features").withColumn("label", chop2(col("token_words")))

#	input_result = predictor.transform(final_df2)

	test_var = "does this work?"

	
	#return render_template('result.html')
	return render_template('result.html', raw_data=raw_data)
	#return input_results in render_template('result.html')






@app.route('/')
def static_page():
	return render_template('index.html')


if __name__ == "__main__":
	app.run()
	#app.run(host='0.0.0.0', port=8080)

#now, create a folder called template and put index.html inside it. DONE
#now, I can run python server.py, got to http://localhost:5000.
	#the root will load index.html.
	#when I send a text, it will use /script endpoint. In there, you can insert your script code. The...
	#..response should be returned in that method. 

	#success/error functions are callbacks. They trigger when the server sends a response back. 
	#If server returns HTTP status 2xx, the success function will be called, error otherwise.

#note, I called server.py app.py instead because that is how we learned
