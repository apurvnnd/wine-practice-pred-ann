# wine-practice-pred-ann
Simple Practice of ANN using wine dataset collected from http://archive.ics.uci.edu/ml/datasets.html
Description of the Dataset 

-- These data are the results of a chemical analysis of
      wines grown in the same region in Italy but derived from three
      different cultivars.
      The analysis determined the quantities of 13 constituents
      found in each of the three types of wines. 
 
-- The attributes are (dontated by Riccardo Leardi, 
	riclea@anchem.unige.it )
 	1) Alcohol
 	2) Malic acid
 	3) Ash
	4) Alcalinity of ash  
 	5) Magnesium
	6) Total phenols
 	7) Flavanoids
 	8) Nonflavanoid phenols
 	9) Proanthocyanins
	10)Color intensity
 	11)Hue
 	12)OD280/OD315 of diluted wines
 	13)Proline            

Number of Instances

      	class 1 59
	class 2 71
	class 3 48

 Number of Attributes 
	
	13

 For Each Attribute:

	All attributes are continuous
	
	No statistics available, but suggest to standardise
	variables for certain uses (e.g. for us with classifiers
	which are NOT scale invariant)

	NOTE: 1st attribute is class identifier (1-3)

 Missing Attribute Values:

	None

 Class Distribution: number of instances per class

      	class 1 59
	class 2 71
	class 3 48
  
  
  
  
Code:
The python code uses the following libraries:
Keras
scikit-learn
pandas
matplotlib

Execution:
Execution was done on spyder using python 3.5

Feature Scaling:
Feature Scaling has been applied to the inputs using standard scaler

Artificial Neural Network used:
Input layer
Hidden layer
Output layer
