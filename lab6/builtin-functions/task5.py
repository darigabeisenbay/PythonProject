def all_elements_true(tup):
    return all(tup)
tuple1 = (True, 1, "hello", 5)
tuple2 = (True, 0, "hello")

print(all_elements_true(tuple1))
print(all_elements_true(tuple2))
