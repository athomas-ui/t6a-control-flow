# Location Codes for Aisles and shelves for easy picking 
aisles = ["A1", "A2", "A3"]
shelves = ["S1", "S2", "S3", "S4"]
for aisle in aisles: 
    row = ""
    for shelf in shelves:
        row =row +aisle +"-" +shelf +" "
    print(row) 
