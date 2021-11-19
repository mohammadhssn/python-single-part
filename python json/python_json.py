"""
    json:
        dump    => python to json
        dumps   => python(string) to json

        load    => json to python
        loads   => json(string) to python
"""

# import json
#
# with open("my.json") as j:  # file my.json ro baz kardim va rikhtim dakhe j
#     data = json.load(j)     # motvaye j ro ke json hast ro tabdil kardim be python va rikhtim dakhele data
#
# print(data)
#
# print("----------------------------------------------------------------------------------------------------")
#
# for i in data:
#     del i["age"]            # hazfe age iz dakhel data
#
# print(data)
#
# print("----------------------------------------------------------------------------------------------------")
#
# with open("my2.json", "w") as m:
#     json.dump(data, m, indent=2)    # tabdile code python be json va rikhtan oon dakhele file my2.josn