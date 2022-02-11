# f = open("abc.txt","r+")
# # for l in f:
# #     print(l)
# # f.close()
# print(f.read())
# # print(v)
# f.write("\nHellooo")

with open("xyz.txt",mode = "r+") as f1:
    # f1.read()
    f1.write("text88")
    f1.read()
    print(f1.read())

