def print_separator():
    print '-' * 10

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# creates a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'Ney York'
cities['OR'] = 'Portland'

# print out some cities
print_separator()
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

# print some states
print_separator()
print "Michigan abbreviation is:", states['Michigan']
print "Florida abbreviation is:", states['Florida']

# do it by using state then cities dictionaries
print_separator()
print "Michigan state has:", cities[states['Michigan']]
print "Florida state has:", cities[states['Florida']]

# print every state abbreviation
print_separator()
for state, abbreviation in states.items():
    print state, 'state is abbreviated with:', abbreviation

# print every city in state
print_separator()
for abbreviation, city in cities.items():
    print abbreviation, "contains:", city

# now do both at the same time
print_separator()
for state, abbreviation in states.items():
    print "State %s, abbreviated with: %s has city: %s" % (state, abbreviation, cities[abbreviation])

# safely get abbreviation for state that might not be there
print_separator()
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas!"

# get a city with a default value
city = cities.get('TX', 'Does not exists')
print "The city for the state TX is:", city
