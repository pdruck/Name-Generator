# Name-Generator
User Input: Gender, Minimum name length, Maximum name length, Number of generated names

This program reads two files that contain lists of the most names for boys and girls.  

A 2nd-Order Markov Model is then used to create a dictionary where the **key** represents a sequence of 2 characters and the **value** represents a list of characters where each character is the letter following the sequence used as the key.  This list will sometimes contain duplicates for more common character sequences.  

A name is then randomly generated (one character at a time) based on those character sequences.  If a character sequence is more common, it will have a higher chance to be chosen because there are more of them included in the dictionary.  There is a check to make sure that the generated name is within the user's bounds and to make sure that the name is not already in the list of common boys/girls names.

This process is repeated until there are as many generated names as the user requested.
