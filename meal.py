'''
def main():
    ...
def convert(time):
    ...
if __name__ == "__main__":
    main()
'''
#convert (time)
time = float(input("what time is it? ").replace(":","."))
def main():
    if 7 <= time <= 8 :
        print("breakfast time")
    elif 12 <= time <=13 :
        print("lunch time")
    elif 18 <= time <= 19 :
        print("dinner time")

main()
