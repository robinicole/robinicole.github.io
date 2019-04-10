---
title: One hot encoding for categories encoded with strings with SparlMLlib
layout: single

author_profile: true
--- 

## The Spark machine learning library

I recently discovered the machine learning library shipped with spark and was really love it. In the same manner as scikit learn, you can chain transformers with Pipeline and end up with your preprocessing as well as your model prediction wrapped in the same object. A special mention to the [SQLTransformer](https://spark.apache.org/docs/latest/ml-features.html#sqltransformer) which was a game changer in my workflow.  

## An example of encoders chaining with pipelines

I just wanted to share this "trick" I came accross in the [Spark's MLlib documentation](https://spark.apache.org/docs/2.1.0/ml-classification-regression.html) to do one hot encoding with **categories encoded by string**. The trick is to **first index strings with numbers** with `StringIndexer`  and then perform the one hot encoding. 

Below is a snippet of a one hot encoder for categories encoded by strings using  `StringIndexer` and  `OneHotEncoder`   chained with a pipeline

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder

def StringOneHotEncoder(inputCol, outputCol): 
	labelIndexer = StringIndexer(inputCol=iputCol, outputCol="indexed_{}".format(outputCol))
	one_hot_encoder = OneHotEncoder(inputCol="indexed_{}".format(outputCol), outputCol=outputCol)
    return Pipeline(stages=[labelIndexer, one_hot_encoder]) 

```

