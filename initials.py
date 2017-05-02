#__ Author __: 'Abdulkerim Abate'
# __Version __: '1.0'
# __Date: 04/26/2017
# Assignment: get_initials


def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name_split = fullname.split()
    initial = []
    for line in name_split:
        initial.append(line[0][0].upper())
    return ("".join(initial))

def main():
    print(get_initials(input("Enter Your Name Here:\n\t")))
if __name__ == '__main__':
    main()



