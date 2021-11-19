# class A:
#     a_Calls = 0
#
#     def Call(self):
#         print("Class A Calling")
#         A.a_Calls += 1
#
#
# class B(A):
#     b_Calls = 0
#
#     def Call(self):
#         print("Class B Calling")
#         B.b_Calls += 1
#         super().Call()
#
#
# class E(A):
#     e_Calls = 0
#
#     def Call(self):
#         print("Class E Calling")
#         E.e_Calls += 1
#         super().Call()
#
#
# class C(A):
#     c_Calls = 0
#
#     def Call(self):
#         print("Class C Calling")
#         C.c_Calls += 1
#         super().Call()
#
#
# class D(C, E, B):
#     d_Calls = 0
#
#     def Call(self):
#         print("Class D Calling")
#         D.d_Calls += 1
#         super().Call()
#
#
# d1 = D()
# d1.Call()
#
# print(d1.d_Calls)
# print(d1.c_Calls)
# print(d1.b_Calls)
# print(d1.a_Calls)
# print(d1.e_Calls)
#
# help(d1)
