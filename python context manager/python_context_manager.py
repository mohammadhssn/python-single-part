"""
   context manager:
                __enter__ , __exit__
"""


# class A:                                 # create context manager
#
#     def __enter__(self):                # ghabl az amale asli ejra mishe.
#         print("Enter Context Manager")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  # bad az amale asli ejra mishe
#         print("Exit Context Manager")
#
#
# def Show():
#     print("Hello mohammadhssn")
#
#
# with A():
#     Show()

# ---------------------------------------------------------------------------------------------------------------------

# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb): # 3 ta parameter exception hastan ke mitonim handle konim.
#         print(f"type: {exc_type}")
#         print(f"type: {exc_val}")
#         print(f"type: {exc_tb}")
#         self.file.close()
#
#         return True # exception khode python ro dige namayesh nemide.
#
#
# with FileManager('hello.txt', 'r') as f:
#     for i in f:
#         print(i)