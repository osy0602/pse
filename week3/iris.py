from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

print("total number of records in the file")
print(len(X))
flower_types = set(y["class"])
print("total number of different flower available")
print(len(flower_types))
print("the names of all different flowers in the dataset")
print(flower_types)
