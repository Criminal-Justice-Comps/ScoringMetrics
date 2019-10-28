
# Calcuate the ROC and AUC for a given classifier's recividism predictions 
def get_Values_at_Threshold(threshold,predicted_recividism):
    threshold_vals = []
    for val in predicted_recividism:
        if threshold <= val:
            threshold_vals.append(1)
        else:
            threshold_vals.append(0)
    return threshold_vals


# False Positive Rate = (False Pos) / ((False Pos) + (True Neg))
# predicted = a list of predicted recividism (0 or 1), at a specific threshold val
# actual = a list of actual recividism (0 or 1)
def calculateFPR(predicted, actual):
    fp = 0
    tn = 0
    if len(predicted) != len(actual): return 0
    for i in range(0,len(predicted)):
        if predicted[i] == 1 and actual[i] == 0:
            fp += 1
        elif predicted[i] == 0 and actual[i] == 0:
            tn += 1
    if fp+tn == 0:
        return 0
    else:
        return fp/(fp+tn)

# True Positive Rate = (True Pos) / ((True Pos) + (False Neg))
# predicted = a list of predicted recividism (0 or 1), at a specific threshold val
# actual = a list of actual recividism (0 or 1)
def calculateTPR(predicted, actual):
    tp = 0
    fn = 0
    if len(predicted) != len(actual): return 0
    for i in range(0,len(predicted)):
        if predicted[i] == 1 and actual[i] == 1:
            tp += 1
        elif predicted[i] == 0 and actual[i] == 1:
            fn += 1
    if tp+fn == 0:
        return 0
    else:
        return tp/(tp+fn)

# threshold_vals = a list of all values to be used as threshold values
# Lowering the classification threshold classifies more items as positive,
# thus increasing both False Positives and True Positives.
def calculateROC(predicted_recividism,actual_recividism,threshold_vals):
    # list of tuples (x,y)
    roc_data = []
    for val in threshold_vals:
        th_vals = get_Values_at_Threshold(val, predicted_recividism)
        fpr = calculateFPR(th_vals, actual_recividism)
        tpr = calculateTPR(th_vals, actual_recividism)
        data_point = (fpr, tpr)
        roc_data.append(data_point)
    return roc_data

# Ask layla: do we have to implement calculating AUC on our own ?
def calculateAUC(roc_data):
    return -1


def main():
  youtube_actual = [1,0,1,0]
  youtube_predicted = [0.8,0.6,0.4,0.2]
  youtube_threshold = [0,0.2,0.4,0.6,0.8,1]
  print(calculateROC(youtube_predicted,youtube_actual,youtube_threshold))

  # where the numbers are P(person | commitsCrime)
  predicted_recividism = [0.5, 0.2, 0.7, 0.1, 0.9,0.4]
  actual_recividism = [0, 1, 1, 0, 1,0] # 0 = false, 1 = true
  thresholdVals = [0,0.2,0.4,0.6,0.8,1]
  print(calculateROC(predicted_recividism,actual_recividism,thresholdVals))

if __name__== "__main__":
  main()
