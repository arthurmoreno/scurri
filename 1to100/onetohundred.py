

def print_1_to_100():
    for i in range(1, 100):
        
        if i%3 == 0 and i%5 == 0:
            i = 'ThreeFive'
        elif i%3 == 0:
            i = 'Three'
        elif i%5 == 0:
            i = 'Five'

        print(i)


if __name__ == '__main__':
    print_1_to_100()
