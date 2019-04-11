---
title: Machine learning with Spark MLlib
layout: single

author_profile: true
--- 

SarkMLlib is the distributed machine learning library shipped with Spark and it really stands out by its *simplicity* and the large number of prediction algorithms it implements (Logistic regression,  Randome Forests to name a few). If you are an intensive user of scikit-learn you will feel at home when chaining  transformers and predictors together with pipelines  *which will  allow to iterate quickly between models* . 

One special mention to the  [SQLTransformer](https://spark.apache.org/docs/latest/ml-features.html#sqltransformer) which allows to create a custom transformer with SQL queries and makes your code so much clearer than having to creat  *soo* many temporary view when you want to process dataframes.  

If you are not yet persuaded to adopt it, here is an example of how simple it is to use it which might stimulate your curiosity. 

## Example: chaining two transformers 

Here is a useful  "trick"  you can find in the [Spark's MLlib documentation](https://spark.apache.org/docs/2.1.0/ml-classification-regression.html) to do one hot encoding with **categories encoded by string**. Spark Machine learning doesn't have a transformer to do that but it has one `StringIndexer` to encode strings by integers and another one `OneHotEncoder` to do one hot encoding on integers. So using a `Pipeline` one can get the one hot encoder for strings with 5 lines of code: 

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder

def StringOneHotEncoder(inputCol, outputCol): 
	labelIndexer = StringIndexer(inputCol=iputCol, outputCol="indexed_{}".format(outputCol))
	one_hot_encoder = OneHotEncoder(inputCol="indexed_{}".format(outputCol), outputCol=outputCol)
    return Pipeline(stages=[labelIndexer, one_hot_encoder]) 

```
