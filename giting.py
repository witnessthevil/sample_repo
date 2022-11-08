import functools

sample_list = [1,2,3,4]
nested_list = [["Daniel",1],["Tom",2]]
the_example_list = ["yes sir"]
some_list = ["some_list"]
reality = 1 

reduce_list = functools.reduce(lambda data,state: data + state , sample_list)
map_list = tuple(map(lambda num: num[0], nested_list))
print(map_list)

# bad commit 