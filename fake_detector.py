print("Fake Alert Detector ON")

file = open("sample.log", "r")

real = 0
fake = 0

for line in file:
    if "failed" in line:
        if "admin" in line:
            real = real + 1
            print("REAL:", line)
        else:
            fake = fake + 1
            print("FAKE:", line)

file.close()

print("Total Real Hackers:", real)
print("Total Fake Bots:", fake)
