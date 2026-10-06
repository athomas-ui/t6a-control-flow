for day in range (1,61): 
    if day % 3 == 0 and day % 5 == 0:
        print(f"Day {day}: FULL AUDIT")
    elif day % 3 == 0:
        print(f"Day {day}: Cycle count")
    elif day % 5 == 0:
        print(f"Day {day}: Scanner audit")
    else:
        print(f"Day {day}: Normal operations")