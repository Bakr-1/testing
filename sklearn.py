import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.svm import SVC
#Program to hire employe
#         first person   second person  third person  forth person
#married=1 or single=0
stats =  [1,            1,              0,            1]

#         first person   second person  third person  forth person
#Previus Record/commited a crime=0 or clean=1
PR =     [1,            0,              0,             0]

#         first person   second person  third person  forth person
#Worked before in a company for 3 years or more =1 less or no =0
experince=[1,            0,             1,             1]

#         first person   second person  third person  forth person
#if the age is less than 30=1 if more than 30=0
age =     [1,            0,             1,             0]

interview_data = np.array([stats,PR,experince,age])
interview_target = np.array([1,0,1,0])
testing_data = np.array([[0, 0.4, 0.2], [0.3, 0.1, 0], [0.6, 0.2, 0.33], [0.21, 0.64, 0]])

classifier = SVC(gamma='auto')
classifier.fit(interview_data,interview_target)
predictions = classifier.predict(testing_data)

print("The accuracy score")
print(100*accuracy_score(testing_data, predictions))
print("The confusion matrix")
print(confusion_matrix(testing_data, predictions))
print("The classification report")
print(classification_report(testing_data, predictions))
print("The predictions")
print(predictions)
