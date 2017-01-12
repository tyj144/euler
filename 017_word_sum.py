# all numbers are composed of these words (besides "hundred" and "and")
key = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',            
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',            
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_key =  {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 
             7: 'seventy', 8: 'eighty', 9: 'ninety'}

# uses the keys to get the length of the number's word 
def get_word_length(num):
  word_length = 0
  
  if num == 1000:
    word_length += len("onethousand")
  else:
    hunds = num // 100
    tens = num % 100
    if hunds > 0:
      word_length += len(key[hunds] + "hundred") # number of letters corresponding to hundreds digit
      if tens > 0:
        word_length += len("and")
    
    if tens < 20:
      word_length += len(key[tens])
    else:
      ones = tens % 10
      tens //= 10
      word_length += len(key[ones]) + len(tens_key[tens])
  return word_length

print(sum(get_word_length(i) for i in range(0,1000+1)))