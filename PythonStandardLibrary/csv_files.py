import csv

# csvFile = open("data.csv", "w")
# csvFile.close()


# creating csv file
# with open("data.csv", "w") as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 3, 65])
#     writer.writerow([1002, 8, 59])

with open("data.csv") as csvFile:
    reader = csv.reader(csvFile)
    # print(list(reader))
    for row in reader:
        print(row)
