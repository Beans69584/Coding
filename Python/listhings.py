import time
def main():
    choice = str(input("Do you want to read or write to the file? (r/w) (presss c to clear file): "))
    if choice == "w":
        add_to_file()
    elif choice == "r":
        read_file()
    elif choice == "c":
        # delete file to clear it
        import os
        try:
            os.remove("test_scores.dat")
            print("File cleared.")
            time.sleep(0.5)
            main()
        except:
            print("File not found.")
            time.sleep(0.5)
            main()
    else:
        print("Invalid choice.")
        time.sleep(0.5)
        main()
def add_to_file():
    try:
        test_scores = []
        average_score = 0
        total_score = 0
        number_of_scores = 0
        choice = ""
        name = ""
        score = 0
        name_and_score = ""
        while choice != "n":
            name = input("Enter the student's name: ")
            score = int(input("Enter the student's score: "))
            name_and_score = name + " " + str(score)
            test_scores.append(name_and_score)
            total_score += score
            number_of_scores += 1
            choice = input("Do you want to enter another score? (y/n): ")
        average_score = total_score / number_of_scores
        file = open("test_scores.dat", "w")
        file.write(str(average_score) + "\n")
        file.write(str(total_score) + "\n")
        file.write(str(number_of_scores) + "\n")
        for score in test_scores:
            file.write(score + "\n")
        file.close()
        time.sleep(0.5)
        read_file()
        time.sleep(0.5)
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Program terminated.")
        time.sleep(0.5)
        main()
def read_file():
    try:
        file = open("test_scores.dat", "r")
        average_score = float(file.readline())
        total_score = float(file.readline())
        number_of_scores = int(file.readline())
        test_scores = []
        for line in file:
            test_scores.append(line.rstrip("\n"))
        file.close()
        print("Test Scores")
        print("-----------")
        for score in sorted(test_scores, key=lambda score: int(score.split()[1]), reverse=True):
            print(score)
        print("Average Score: ", average_score)
        print("Total Score: ", total_score)
        print("Number of Scores: ", number_of_scores)
        time.sleep(0.5)
        main()
    except FileNotFoundError:
        print("File not found.")
        print("Please add some scores to the file.")
        time.sleep(0.5)
        add_to_file()
main()