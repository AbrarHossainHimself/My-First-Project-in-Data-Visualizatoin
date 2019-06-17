import random
import csv
import matplotlib.pyplot as plt

# csv file
csv_file = open("Coin Toss.csv", 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Number of Experiment", "Total Money"])

# Setting Parameters
number = int(input("Enter the number of times you would like to execute this experiment: "))
record_list = []
total_money_list = []


def experiment():
    n = 1
    heads = 0
    tails = 0
    while n < 101:
        toss = random.randint(0, 1)

        if toss == 0:
            print(toss, "It's a Heads")
            heads = heads + 1
            record_list.append("Heads")
        else:
            print(toss, "It's a Tails")
            tails = tails + 1
            record_list.append("Tails")

        print("-------", int(n), "-----------")
        n = n + 1

    total_money = (heads*(-100) + tails*(200))
    total_money_list.append(int(total_money))

    print(total_money)
    print(record_list)
    print(total_money_list)
    print("Number of Heads : ", str(record_list.count("Heads")),  "Number of Tails : ",
          str(record_list.count("Tails")))


no_experiments = []


for i in range(number):
    no_experiments.append(int(i))
    print(i + 1, "New experiment")
    print("\n\n")
    experiment()
    print("\n\n")
    csv_writer.writerow([i + 1, total_money_list[i]])

plt.bar(no_experiments, total_money_list)
plt.ylabel("Total Money")
plt.xlabel("Instance of Experiment")

plt.show()
csv_file.close()








