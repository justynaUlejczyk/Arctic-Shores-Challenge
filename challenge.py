def ArrayChallenge(strArr):
  #handling split of words
  sequence = strArr[0]
  dictionary = set(strArr[1].split(','))  

  varOcg = None

    #loop through possible split 
  for i in range(1, len(sequence)):	
      first_word = sequence[:i]
      second_word = sequence[i:]

      #check for both words exist in the dictionary
      if first_word in dictionary and second_word in dictionary:
         #storing the results
        varOcg = first_word + "," + second_word
        break  

  if varOcg:
    # final output with the ChallengeToken
    challenge_token = "94vtsbc6"
    final_output = varOcg + challenge_token
        
    final_output_list = list(final_output)
    for i in range(2, len(final_output), 3):
      final_output_list[i] = 'X'
    
    final_output = ''.join(final_output_list)
    return final_output  

  if varOcg:
    strArr = varOcg
  else:
    return "not possible"
  #return "not possible"
  return strArr

# keep this function call here 
print ArrayChallenge(raw_input())
