import sys

#setting up a dictionary of atomic symbols and their atomic weights
atomic_weights = {
    'H':1.00797,
'He':4.0026,
'Li':6.941,
'Be':9.01218,
'B':10.81,
'C':12.011,
'N':14.0067,
'O':15.9994,
'F':18.998403,
'Ne':20.179,
'Na':22.98977,
'Mg':24.305,
'Al':26.98154,
'Si':28.0855,
'P':30.97376,
'S':32.06,
'Cl':35.453,
'K':39.0983,
'Ar':39.948,
'Ca':40.08,
'Sc':44.9559,
'Ti':47.9,
'V':50.9415,
'Cr':51.996,
'Mn':54.938,
'Fe':55.847,
'Ni':58.7,
'Co':58.9332,
'Cu':63.546,
'Zn':65.38,
'Ga':69.72,
'Ge':72.59,
'As':74.9216,
'Se':78.96,
'Br':79.904,
'Kr':83.8,
'Rb':85.4678,
'Sr':87.62,
'Y':88.9059,
'Zr':91.22,
'Nb':92.9064,
'Mo':95.94,
'Ru':101.07,
'Rh':102.9055,
'Pd':106.4,
'Ag':107.868,
'Cd':112.41,
'In':114.82,
'Sn':118.69,
'Sb':121.75,
'I':126.9045,
'Te':127.6,
'Xe':131.3,
'Cs':132.9054,
'Ba':137.33,
'La':138.9055,
'Ce':140.12,
'Pr':140.9077,
'Nd':144.24,
'Sm':150.4,
'Eu':151.96,
'Gd':157.25,
'Tb':158.9254,
'Dy':162.5,
'Ho':164.9304,
'Er':167.26,
'Tm':168.9342,
'Yb':173.04,
'Lu':174.967,
'Hf':178.49,
'Ta':180.9479,
'W':183.85,
'Re':186.207,
'Os':190.2,
'Ir':192.22,
'Pt':195.09,
'Au':196.9665,
'Hg':200.59,
'Tl':204.37,
'Pb':207.2,
'Bi':208.9804,
'Ra':226.0254,
'Ac':227.0278,
'Pa':231.0359,
'Th':232.0381,
'Np':237.0482,
'U':238.029,
}

def main():
    elements = get()
    atomic_percents = ask(elements)
    answer = convert(elements, atomic_percents)
    for i in range(len(answer)):
        print(f"Weight percentage of {elements[i]} is {answer[i]}.")

def get():
    #find out how many elements need to be converted from atomic percent to weight percent
    number_elements = int(input("How many elements present? "))
    element_list = []
    #find out which elements are present, as many times as was indicated in number_elements
    for i in range(number_elements):
        inp = input("Atomic symbol: ").capitalize()
        #check if the input is a valid atomic symbol, if not exit program so user can try again
        if inp in atomic_weights:
            element_list.append(inp)
        else:
            sys.exit("Must be a valid atomic symbol.")
    return(element_list)

def ask(e):
    #ask input of atomic percent of all elements in element_list
    #only asks as many times as needed based on input given in get()
    #if the user has atomic percents that sum to greater than 100, ask if they want to try again in case it was a typo. otherwise exit
    atomic_percents = []
    while True:
        try:
            for i in range(len(e)):
                atomic_percents.append(float(input(f"Atomic percentage present of {e[i]}: ")))
            if 0 < sum(atomic_percents) <= 100:
                return atomic_percents
            else:
                if input("Atomic percent total must be greater than 0 and less than 100. Try again? ").lower() == "y":
                    atomic_percents = []
                    pass
                else:
                    sys.exit()
        except ValueError:
            sys.exit("Must input a valid number for atomic percent.")

def convert(e,a):
    #e is the list of elements given in get()
    #a is the list of atomic percents given in ask()
    #use dictionary to get atomic weights of the elements in element list
    answer_list=[]
    for i in range(len(e)):
        answer_list.append(atomic_weights[e[i]] * a[i] / 60.22)
    s = 100 / sum(answer_list)
    for i in range(len(answer_list)):
        #format final answer here rounded to three decimal points
        answer_list[i] = "{:.3f}".format(answer_list[i] * s)
    return answer_list

if __name__ == "__main__":
    main()
