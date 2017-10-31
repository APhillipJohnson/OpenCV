with open("faces.csv", 'w') as f:
    for i in range(1,34):
        f.write("488/" + str(i) + ".pgm;0\n")