# class A:
#     def Call(self, a=''):
#         print(f"Class A => {a}")
#
#
# class B:
#     def Call(self, b='', a='' , **kwargs):
#         print(f"Class B => {b} {a}")
#         kwargs['a'] = a
#         super().Call(**kwargs)
#
#
# class C(B, A):
#     def Call(self, c='', **kwargs):
#         print(f"Class C => {c}")
#         super().Call(**kwargs)
#
#
# c1 = C()
# c1.Call(a='aaaa', b='bbbb', c='cccc')