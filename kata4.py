## Incident Validation (guard clauses)
incidents = [
    {"id": "INC-1001", "branch": "DC-North", "severity": 2},
    {"id": "INC-1002", "branch": None, "severity": 1},
    {"id": "INC-1003", "branch": "DC-South", "severity": 5},
    {"id": "INC-1004", "branch": "DC-North", "severity": 3},
]

for incident in incidents:
    # Guard clause 1: Check if branch exists
    if incident["branch"] is None:
        print(f"SKIPPED {incident['id']}: missing branch")
        continue
    
    # Guard clause 2: Check if severity is valid (1-3)
    if incident["severity"] < 1 or incident["severity"] > 3:
        print(f"SKIPPED {incident['id']}: severity {incident['severity']} is not 1-3")
        continue
    
    # If we get here, it passed both checks
    print(f"LOGGED {incident['id']} at {incident['branch']} (severity {incident['severity']})")