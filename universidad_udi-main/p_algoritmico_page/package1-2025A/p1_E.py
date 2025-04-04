H = float(input())
CA = float(input()) / 100

CO = (H**2 - CA**2) ** 0.5

print(round(CO, 2))
print(int(CO * 100) / 100)