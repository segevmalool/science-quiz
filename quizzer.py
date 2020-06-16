import numpy as np

games = {
  '0': 'metric_prefix',
  '1': 'decreasing_8_bit_binary_number'
}

metric_prefix = {
  'tera': '12',
  'giga': '9',
  'mega': '6',
  'kilo': '3',
  'hecto': '2',
  'deca': '1',
  'deci': '-1',
  'centi': '-2',
  'milli': '-3',
  'micro': '-6',
  'nano': '-9',
  'pico': '-12'
}

decreasing_8_bit_binary_number = {
  '0': '0',
  '1': '128',
  '2': '192',
  '3': '224',
  '4': '240',
  '5': '248',
  '6': '252',
  '7': '254',
  '8': '255'
}

if __name__ == '__main__':
  selection = input("""
    Welcome to the general knowledge quizzer thing. 
    Select mode:
     
    0: Practise metric prefixes
    1: Practise netmask numbers
  """)
 
  mode = games[selection]

  print('============================================================')

  while True:
    choice_list = eval(mode).keys()

    choice = np.random.choice(list(choice_list))

    selection = input(mode + ' of ' + choice + ': ==> ')

    if selection == 'reverse':
      globals()[mode] = { v:k for k,v in eval(mode).items() }
      continue

    if selection == 'exit':
      print('Science for fun and profit!')
      exit()

    if selection == eval(mode)[choice]:
      print("Success")
    else:
      print("Failure")
