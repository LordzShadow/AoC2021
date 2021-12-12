
conns = {}

with open("input.txt", "r") as file:
    for line in file:
        start, end = line.strip().split("-")
        if start not in conns.keys():
            conns[start] = []
        if end not in conns.keys() and end != "end":
            conns[end] = []
        conns[start].append(end)
        if end != "end" and start != "start":
            conns[end].append(start)

def router(x = "start", route = [], routes = [], small = False):
    if x == "end":
        routes.append(route + [x])
        return routes
    for x_n in conns[x]:
        if x_n.isupper():
            routes = router(x_n, route + [x], routes, small)
        if x_n.islower():
            if x_n not in route:
                routes = router(x_n, route + [x], routes, small)
            elif not small and x_n != "start":
                routes = router(x_n, route + [x], routes, True)

    return routes


print(len(router()))
