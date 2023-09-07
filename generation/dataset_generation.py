read_file = open("../sampleData200k.txt", "r")
dataset_05k = open("../testing/dataset_0.5k.txt", "w")
dataset_1k = open("../testing/dataset_1k.txt", "w")
dataset_5k = open("../testing/dataset_5k.txt", "w")
dataset_10k = open("../testing/dataset_10k.txt", "w")
dataset_50k = open("../testing/dataset_50k.txt", "w")
dataset_100k = open("../testing/dataset_100k.txt", "w")


for count, line in enumerate(read_file):
    if count + 1 <= 500:
        dataset_05k.write(line)
    elif count + 1 <= 500 + 1000:
        dataset_1k.write(line)
    elif count + 1 <= 500 + 1000 + 5000:
        dataset_5k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000:
        dataset_10k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000 + 50000:
        dataset_50k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000 + 50000 + 100000:
        dataset_100k.write(line)
