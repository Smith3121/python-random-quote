import random


def main():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 14
  rnd = random.randint(0, last)
  rmd = random.randint(0, last)
  rdt = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[rmd])
  print(quotes[rdt])




if __name__== "__main__":
  main()
