def count_line():
    line_count = 0

    file = open("./Clustering.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()    

    file = open("./Count_line.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Cover_set_test.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Euclid_dist.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Kmeans.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Main.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Make_total_circle.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    
    file = open("./Make_circle.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Mkdir.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Pre_process.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Process.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Scatter_circles.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Update_data.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    file = open("./Update_unionSet.py", "r")
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count