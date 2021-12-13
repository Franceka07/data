import csv
import pandas

class Question:
  def __init__(self,location = " ", filename="questions.csv"):
    self.fcsv=pandas.read_csv(location + '/' + filename)
    print(self.fcsv)

  def get(self, category=1, level= None, qid=None):
    if qid:
      filter=self.fcsv['qid']==qid
      row_data=self.fcsv[filter]
      if row_data.empty:
        return{}
      else:
        return row_data.to_dict(orient= 'records')[0]

    if level:
      filter=self.fcsv['level']==level
      row_data=self.fcsv[filter]
      if row_data.empty:
        return{}
      else:
        print(row_data)
    else:
      return{}

    if category:
      filter=self.fcsv['category']==category
      row_data=self.fcsv[filter]
      if row_data.empty:
        return{}
      else:
        print(row_data)
    else:
      return{}

    if level and category:
      filter1 = self.fcsv['level']==level
      row_data=self.fcsv[filter]


    

q1= Question ("https://raw.githubusercontent.com/bfilin/data/main/programming_assignments/part0/questions.csv")
print (q1.get())
print (q1.get(qid=60))
print (q1.get(qid=2))
print(q1.get(level=10))
