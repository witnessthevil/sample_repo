import functools

sample_list = [1,2,3,4]
nested_list = [["Daniel",1],["Tom",2]]
the_other_example_list = ["Some name"]

reduce_list = functools.reduce(lambda data,state: data + state , sample_list)
map_list = tuple(map(lambda num: num[0], nested_list))
print(map_list)