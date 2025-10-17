# combination-calculator
The app calculates all possible combinations of numbers from a predefined set of numbers that equal a given sum.  
  
This app is also available on Streamlit's Community Cloud: [https://combination-calculator.streamlit.app/](https://combination-calculator.streamlit.app/).

# Parameters
The parameters are self-explanatory. However, the *Expected sum of the numbers in the set* parameter is quite special and has direct impact on the result.

## Value provided for the sum is 0
All possible sums for the provided *Amount of numbers per set* will be returned.

## Value provided for the sum is out of range
When there's no matching sum for the provided *Amount of numbers per set* and *Expected sum of the numbers in the set*, two result sets will be returned:
1. a set with the minimum sum for the provided *Amount of numbers per set*
2. a set with the maximum sum for the provided *Amount of numbers per set*

## Value provided for the sum is within range
All sets matching the provided *Expected sum of the numbers in the set* will be returned.