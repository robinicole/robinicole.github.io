---
title: Log loss of Logistic regression with SparkMLlib 
layout: single
header: 
   image: /assets/images/header.jpg
author_profile: true
--- 

Evaluation is the crucial step in a machine learning project and, if you want it to be successful, it is important to choose an evaluation metric which is consistent with your business objectives. For classification (e.g. logistic regression) problems, you could use the accuracy, the precision or the recall but those metrics only evaluate the goodness of the *final classification choice* (binary) and not the accuracy of the *probability* predicted by the algorithm (continuous value between 0 and 1). To evaluate the goodness of the probability  predicted by the Logistic regression, you could use the *ROC-AUC score* or the *log-loss* . Unfortunately there is no implementation of the log-loss shipped with the spark ML library. The snippet of code below does this job: it takes a model prediction dataframe (returned by `model.transform` ) as an input and returns the corresponding log loss. 

```python
from pyspark.sql.functions import udf
from pyspark.ml.feature import SQLTransformer

@udf('float')
def first_element(v): 
    return float(v[1])

log_lossTransformer = SQLTransformer(statement="""SELECT AVG(log(first_element(probability)) *  success  +  
                            log(1 - first_element(probability)) * (1 -success)) as log_loss 
                            FROM __THIS__""") 

model_output = model.fit(train_set) # first fit the model 
log_lossTransformer.transform(model_output.transform(test_set)).show()
```

