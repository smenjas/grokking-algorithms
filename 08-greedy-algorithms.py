# Find the least radio stations that cover the most states.

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["k1"] = set(["id", "nv", "ut"])
stations["k2"] = set(["wa", "id", "mt"])
stations["k3"] = set(["or", "nv", "ca"])
stations["k4"] = set(["nv", "ut"])
stations["k5"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    print(states_covered)
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
