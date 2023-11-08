"""
You are testing a medical kit that tests for a disease. 

The vendor has provided the following table on tests of 1000 patients. 

            |TESTS POSITIVE|TESTS NEGATIVE|
+-----------+--------------+--------------+             
|AT RISK    |     198      |       2      |
|NOT AT RISK|      50      |      750     |
+-----------+--------------+--------------+ 

It shows who tested positive or negative versus actually having the disease. 

The vendor claims that 99% of those at risk will test positive. However, you 
are suspicious of the results as only 1% of the population actually has the disease. 

What true positive rate can we expect as we test on the population? 

Complete and run the Python script below to calculate your answer.
"""

p_true_positive = 198.0 / (198.0 + 2.0)
p_at_risk = .01
p_positive = (198.0 + 50.0) / 1000.0

p_true_positive_population = ? 
