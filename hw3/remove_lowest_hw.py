import pymongo
import sys

connection = pymongo.MongoClient('localhost', 27017)
db = connection.school
students = db.students

def remove_lowest_hw_score():
	try:
		cur = students.find()
	except Exception as e:
		print 'Unexpected error:', type(e), e

	for doc in cur:
		scores_hw = []
		scores = []
		for _score in doc['scores']:
			if(_score['type'] != 'homework'):
				scores.append({"type":_score['type'],"score":_score['score']})
			else:
				scores_hw.append(_score['score'])

		scores.append({"type":"homework","score":max(scores_hw)})
		students.update({"_id":doc['_id']},{'$set':{"scores":scores}})
		
		print scores

remove_lowest_hw_score()
