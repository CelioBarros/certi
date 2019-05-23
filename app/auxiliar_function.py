translate_dict_simple_positive = {
  0: "",
  1: "um",
  2: "dois",
  3: "três",
  4: "quatro",
  5: "cinco",
  6: "seis",
  7: "sete",
  8: "oito",
  9: "nove",
  10: "dez",
  11: "onze",
  12: "doze",
  13: "treze",
  14: "catorze",
  15: "quize",
  16: "dezeseis",
  17: "dezesete",
  18: "dezoito",
  19: "dezenove"
}
translate_dict_composed_positive = {
  0: "",
  1: "",
  2: "vinte",
  3: "trinta",
  4: "quarenta",
  5: "cinquenta",
  6: "sessenta",
  7: "setenta",
  8: "oitenta",
  9: "noventa",
}
translate_dict_hundred_positive = {
  1: "cento",
  2: "duzentos",
  3: "trezentos",
  4: "quatrocentos",
  5: "quinhentos",
  6: "seiscentos",
  7: "setecentos",
  8: "oitocentos",
  9: "novecentos",
}

def number_to_word(number):
  result = ''
  if(number == 0):
    return 'zero'
  if (number < 0):
    result += 'menos '
    number *= -1

  thousand = int(number/1000)
  if (thousand > 0):
    if (thousand > 1):
      result += composed_value(thousand) + ' '
    result += 'mil'
  
  number -= (thousand*1000)
  hundred = int(number/100)
  if (hundred >= 1 and thousand > 0):
    result += ' e '
  if (number == 100):
    result += 'cem'
    return result

  if (hundred >= 1):
    result += translate_dict_hundred_positive[hundred]
  number -= (hundred*100)
  
  if ((hundred >= 1 or thousand > 0) and number > 0):
    result += ' e '
  result += composed_value(number)
  return result

def composed_value(number):
  result = ''
  single = int(number % 10)
  composed = int(((number % 100) - single) / 10)
  if (composed <= 1):
    result += translate_dict_simple_positive[int(number % 100)]
  else:
    result += translate_dict_composed_positive[composed] 
    if (single > 0):
      result += ' e ' + translate_dict_simple_positive[single]
  return result