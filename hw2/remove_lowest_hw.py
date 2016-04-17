import pymongo
import sys

connection = pymongo.MongoClient('localhost', 27017)

def remove_lowest_hw_score():
	db = connection.students
	scores = db.grades
	try:
		cur = scores.find({},{'student_id' : 1,'_id':0}).distinct('student_id');
	except Exception as e:
		print 'Unexpected error:', type(e), e
	
	sanity = 0
	for student_id in cur:
		print(student_id)
		cur = scores.find({'student_id':student_id,'type':'homework'},{'_id':1});
		cur.sort('score',1).limit(1); 
		nextup = cur.next()
		print(nextup['_id'])
		result = scores.delete_one({'student_id':student_id,'_id':nextup['_id']})
	print(result.deleted_count)
remove_lowest_hw_score()
