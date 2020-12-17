import os
import requests

os.system('clear')

running = True

while running:
  url_result = []
  print("Welcom to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
# Get URLs
  urls = input()
  url_list = urls.split(',')

  for i in url_list:
    str_url = i.strip()
    if '.' not in str_url:
      print(f'{str_url} is not valid URL')
    elif 'http://' not in str_url:
      str_url = 'http://'+str_url
      url_result.append(str_url)
    else:
      url_result.append(str_url)
  # print("url_result:", url_result)

# Main
  for i in url_result:
    try:
      r=requests.get(i)
      # print(i)
      if r.status_code == 200:
        # print(r.status_code)
        print(f'{i} is Up!')
        
    except:
      print(f'{i} is Down!')
      ConnectionError

# Checking Continuous
  check = True
  while check:
    ans = input("Do you want to start over? y/n\t",)
    if ans == 'y' or ans == 'Y':
      os.system('clear')
      check = False
    elif ans == 'n' or ans == 'N':
      print('OK, bye!')
      running = False
      break
    else:
      print("That's not a valid answer!")
