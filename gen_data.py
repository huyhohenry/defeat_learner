
import math
import numpy as np

# this function should return a dataset (X and Y) that will work  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
# better for linear regression than decision trees  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def best_4_lin_reg(seed=1489683273):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  	  			  		 			 	 	 		  
    :param seed: The random seed for your data generation.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type seed: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: numpy.ndarray  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """
    np.random.seed(seed)
    row_count = np.random.randint(10, 1000)
    col_count = np.random.randint(2, 10)
    x = np.random.normal(size=(row_count, col_count))
    y = np.zeros(row_count)
    for col in range(col_count):
        y += np.random.randint(1, 10) * x[:, col]
    return x, y


def best_4_dt(seed=1489683273):
    """
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param seed: The random seed for your data generation.
    :type seed: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: numpy.ndarray  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """
    np.random.seed(seed)
    row_count = np.random.randint(10, 1000)
    col_count = np.random.randint(2, 10)
    x = np.random.normal(size=[row_count, col_count])
    y = np.zeros(row_count)
    for col in range(col_count):
        y += x[:, col]**2 - 2*x[:, col] + 1
    return x, y  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 


def author():
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: str  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return ""
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
if __name__ == "__main__":  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print("they call me Tim.")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
