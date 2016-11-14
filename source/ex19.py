def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Get more!"


# feeding function directly
cheese_and_crackers(20, 30)

amount_of_cheese = 10
amount_of_crackers = 50

# feeding function with variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# math inside function arguments
cheese_and_crackers(10 + 20, 5 + 6)

# combining variables and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
