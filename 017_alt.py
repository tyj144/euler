# all numbers are composed of these words (besides "hundred" and "and")
key = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',            
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',            
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_key =  {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 
             7: 'seventy', 8: 'eighty', 9: 'ninety'}

# finds the lengths of each word in the key
lengths = {i:len(key[i]) for i in key}
tens_lengths = {i:len(tens_key[i]) for i in tens_key}

# uses the keys to get the length of the number's word 
def get_word_length(num):
  word_length = 0
  
  if num == 1000:
    word_length += len("onethousand")
  else:
    hunds = num // 100
    if hunds > 0:
      word_length += lengths[hunds] # pull the hundreds digit's length (e.g. "one" [hundred])
      word_length += len("hundred")
      if num % 100 > 0:
        word_length += len("and")
    
    tens = num % 100
    if tens < 20:
      word_length += lengths[tens]
    else:
      ones = tens % 10
      tens //= 10
      word_length += lengths[ones] + tens_lengths[tens]

  return word_length

print(sum(get_word_length(i) for i in range(0,1000+1)))