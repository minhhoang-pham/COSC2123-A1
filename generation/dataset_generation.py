read_file = open("../sampleData200k.txt", "r")
dataset_05k = open("../dataset_0.5k", "w")
dataset_1k = open("../dataset_1k", "w")
dataset_5k = open("../dataset_5k", "w")
dataset_10k = open("../dataset_10k", "w")
dataset_20k = open("../dataset_20k", "w")
dataset_50k = open("../dataset_50k", "w")
dataset_100k = open("../dataset_100k", "w")


for count, line in enumerate(read_file):
    if count + 1 <= 500:
        dataset_05k.write(line)
    elif count + 1 <= 500 + 1000:
        dataset_1k.write(line)
    elif count + 1 <= 500 + 1000 + 5000:
        dataset_5k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000:
        dataset_10k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000 + 20000:
        dataset_20k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000 + 20000 + 50000:
        dataset_50k.write(line)
    elif count + 1 <= 500 + 1000 + 5000 + 10000 + 20000 + 50000 + 100000:
        dataset_100k.write(line)
