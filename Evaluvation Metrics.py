#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#I take a random sample of 2 cartoon characters, 2 real persons, 1 pronoun, which is a total of 5. Of these persons, 4 actually are real. I predicted 5 total real persons, 4 of which are actually persons.
#I predicted 5 persons so our “predicted persons row” should add up to 5. We know that 4 of the 5 were indeed persons, so we can put 4 in the predicted Person actual person spot, aka a True Positive.
#1.	Accuracy (all correct / all) = TP + TN / TP + TN + FP + FN
#(2 + 1) / (2+1+1+1) = 3 / 5 = 0.60 or 60% Accuracy
#2.	Precision (true positives / predicted positives) = TP / TP + FP
#2 / (2 + 1) = 2 / 3 = 0.66 or 66% Precision
#3.	Recall (true positives / all actual positives) = TP / TP + FN
#2 / (2 + 1) = 2 / 3 = 0.66 or 66% Recall
#4.	F1 Score = 2*(Recall * Precision) / (Recall + Precision)
#F1 Score = 2*(0.66*0.66)/(0.66+0.66)= 0.4356/1.32= 0.33 or 33%


# In[10]:


#program a functions that calculates and displays all 4 metrics (accuracy,precision, recall,f-measure) . 
#The functions should accept TP,TN,FP,FN and spit out the results 

#TP=TruePositive
#TP = 2
#FP=FalsePositive
#FP = 1
#FN=FalseNegative
#FN = 1
#TN= TrueNegative
#TN = 1

def MetricDisplays (TP, FP, FN, TN):

    Accuracy = (TP + TN) / (TP + TN + FP + FN)
    print(f"Accuracy is {Accuracy}")
    Accuracy_percentage = Accuracy*100
    print(f"Accuracy % is {Accuracy_percentage}%")

    Precision = TP / (TP + FP)
    print(f"Precision is {Precision}")
    Precision_percentage = Precision*100
    print(f"Precision % is {Precision_percentage}%")

    Recall = TP / (TP + FN)
    print(f"Recall is {Recall}")
    Recall_percentage = Recall*100
    print(f"Recall % is {Recall_percentage}%")

    F1Score = (2 *(Recall * Precision)) / (Recall + Precision)
    print(f"F1Score is {F1Score}")
    F1Score_percentage = F1Score*100
    print(f"F1Score % is {F1Score_percentage}%")

MetricDisplays(2,1,1,1)



# In[ ]:




