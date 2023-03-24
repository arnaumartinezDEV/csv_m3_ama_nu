import csv

def ex1():
    with open("slavery.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        seller = {}

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} xxx {row[1]} xxx {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


def main():
    while True:
        print("\t1.- quin va ser el venedor que més esclaus en va vendre ")
        print("\t2.-  ")
        print("\t3.-  ")
        print("\t4.-  ")
        print("\t5.- ")

        # Menu options condition
        optionMenu = input("\nSelect any option: ")

        if optionMenu == "1":
            ex1()

        elif optionMenu == "2":
            pass

        elif optionMenu == "3":
            pass

        elif optionMenu == "4":
            pass

        elif optionMenu == "5":
            print("\nBye :)")
            break

        else:
            print("")
            input("Please select the correct option...\npress any key to continue")

if __name__ == '__main__':
    main()
