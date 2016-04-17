In this assignment you will use the aggregation framework to find the most frequent author of comments on your blog. We will be using a data set similar to ones we've used before. 

Now use the aggregation framework to calculate the author with the greatest number of comments. 

To help you verify your work before submitting, the author with the fewest comments is Mariela Sherer and she commented 387 times. 

db.posts.aggregate([ {$unwind: "$comments"}, {$group :{"_id" : "$comments.author", count: {$sum:1}}}, {$sort: {count:1}} ])

