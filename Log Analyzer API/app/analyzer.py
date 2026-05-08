def count_errors(log_file):
    count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                count += 1

    return count