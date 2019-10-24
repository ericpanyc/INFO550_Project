# INFO550_Project
## address_retriever.py usage
- Input the latitude and longitude of the place of interest to the program, to generate 100 house records (if Zillow has the data on that location, otherwise you will see 'wrong address' in the output file). 
- Sample command line code: 'python3 address_retriever.py --lati 34.050010 --longi -118.184630' . Please be aware of the numbers of digit of two geometry number.
- If codes run successfully, you will find a file named 'test_zillow_data.txt' appears in your working directory. The data in it is delimited by comma, and each column is corresponding to item number, street address, city, latitude, longitude, number of bedrooms, price, region name respectively.
- I ran some small tests and the results seemed to be fine, but in actual use, because not all addresses generated in the program are recorded by Zillow, so the output data may be ugly.
- I use two apis in the codes. I strongly recommend you that when you are running tests, you can substitute the two api keys with yours.
- The codes are extremely fragile and may cause tons of bugs, so if you run into some of them, just let me know and I will try to fix it.
