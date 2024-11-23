def process_routes(n, m, cities, routes, queries):
    # Create a dictionary to map city names to indices
    city_index = {city: i for i, city in enumerate(cities)}
    
    # Adjacency matrix for direct flights between cities
    direct_flights = [[0] * n for _ in range(n)]
    
    # Fill the adjacency matrix based on the routes
    for route in routes:
        source, destination = route
        direct_flights[city_index[source]][city_index[destination]] = 1
    
    # Process queries and build output
    output = []
    for query in queries:
        query_index = city_index[query]
        # Count of direct routes from this city
        direct_count = sum(direct_flights[query_index])
        output.append(str(direct_count))
        
        # Add cities that have a direct route
        for i in range(n):
            if direct_flights[query_index][i] == 1:
                output.append(cities[i])
        
        # Add "0" if no direct route exists
        if direct_count == 0:
            output.append("0")
    
    return output

# Main function to read input and produce output
def main():
    # Get the number of cities and routes from the user
    n = int(input("How many cities are there? "))
    m = int(input("How many direct flight routes are there? "))
    
    # Get the names of the cities
    cities = []
    for i in range(n):
        city = input(f"What is the name of city {i + 1}? ")
        cities.append(city.strip())
    
    # Get the routes
    routes = []
    print("Please enter each flight route as 'source destination':")
    for _ in range(m):
        route = input("What is the flight route? ").strip().split()
        routes.append((route[0], route[1]))
    
    # Get the number of queries
    q = int(input("How many queries do you have? "))
    
    # Get the queries
    queries = []
    for i in range(q):
        query = input(f"What is the name of city for query {i + 1}? ").strip()
        queries.append(query)
    
    # Process routes and generate output
    output = process_routes(n, m, cities, routes, queries)
    
    # Display the output
    for line in output:
        print(line)

# Run the main function
main()
