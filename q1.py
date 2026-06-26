#q1:
# n = int(input())
# d = {}
# pt = ""
# for i in range(n):
#     line = input().strip()
#     if line == "{" or line == "}" or line == "},":
#         continue
#     line = line.replace('"', "").replace(",", "")
#     if line.endswith("{"):
#         pt = line.split(":")[0]
#         d[pt] = {}
#     else:
#         key, value = line.split(":")
#         d[pt][key.strip()] = value.strip()

# def get_dict_value(d, path):
#     p = path.split(".")
#     if p[0] in d:
#         if p[1] in d[p[0]]:
#             return d[p[0]][p[1]]
#     return "None"

# m = int(input())
# paths = []
# for i in range(m):
#     paths.append(input())
# for i in paths:
#     print(get_dict_value(d, i))