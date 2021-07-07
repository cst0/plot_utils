# plot_utils Collection of scripts for parsing data and generating plots.

I find that I seem to keep re-writing a lot of functionality for the sake of
making nice-looking plots, so now I'm attempting to consolidate all that effort
to one place. There's a handful of stuff here:

- data
    - sets of data to work with
- plot
    - code for generating plots
    - boxplot: generates some typical box plots.
- tests
    - tests for each of the functions in utils.
- utils
    - various utilities for parsing and converting data. 
    - convert.py:
        - numparse: take in a formula string ("32+3-12*8") and turn it into a
          float
        - numparselist: take in several formula strings seperated by whitespace
          ("32+3 12*8") and turn it into a list of floats
