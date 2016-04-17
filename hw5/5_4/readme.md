In this problem you will calculate the number of people who live in a zip code in the US where the city starts with a digit. We will take that to mean they don't really live in a city. Once again, you will be using the zip code collection, which you will find in the 'handouts' link in this page. 

Using the aggregation framework, calculate the sum total of people who are living in a zip code where the city starts with a digit.

You will need to probably change your projection to send more info through than just that first character. Also, you will need a filtering step to get rid of all documents where the city does not start with a digital (0-9).

Note: When you mongoimport the data, you will probably see a few duplicate key errors; this is to be expected, and will not prevent the mongoimport from working. There is also an issue with some versions of MongoDB 3.0 where it claims that 0 documents were mongoimported, when in fact there were 29,467 documents imported. You can verify this for yourself by going into the shell and counting the documents in the "test.zips" collection.

```
db.zips.aggregate([{$project:{_id:1,first_char:{$substr:["$city",0,1]},city:1,state:1,pop:1}},{$match:{first_char:{$in:["0","1","2","3","4","5","6","7","8","9"]}}},{$group:{_id:"random",pop:{$sum:"$pop"}}}])
```
