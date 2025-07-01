import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

file_name = "output/" #add filename to evaluate without .csv extension on string

results = pd.read_csv(file_name+".csv")

f = open(file_name+".txt", "w")

#calculate overall accuracy and F1 Score
total_accuracy = round(accuracy_score(results.Gold, results.Prediction),2)
print(total_accuracy)
f.write("Overall metrics" + "\nnumber: " + str(len(results)) + "\naccuracy: " + str(total_accuracy) + "\nF1 Score for each label: " + str(f1_score(results.Gold, results.Prediction, average=None)))

#calculate accuracy and F1 score for each for each schematicity type
for item in results.schematicity.unique().tolist():
    subset = results.where(results.schematicity==item).dropna()
    subset_accuracy = round(accuracy_score(subset.Gold, subset.Prediction),2)
    f.write("\n\nschematicity: " + item + "\nnumber: " + str(len(subset)) + "\naccuracy: " + str(subset_accuracy) + "\nF1 Score for each label: " + str(f1_score(subset.Gold, subset.Prediction, average=None)))

#calculate accuracy and F1 score for each for each CxG type
for type in results.CxG.unique().tolist():
    subset = results.where(results.CxG==type).dropna()
    subset_accuracy = round(accuracy_score(subset.Gold, subset.Prediction), 2)
    f.write("\n\nCxG: " + type + "\nschematicity: " + subset.schematicity.iloc[0] + "\nnumber: " + str(len(subset)) + "\naccuracy: " + str(subset_accuracy) + "\nF1 Scorefor each label: " + str(f1_score(subset.Gold, subset.Prediction, average=None)))

f.close()

