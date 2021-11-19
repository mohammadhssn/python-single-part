"""
    python logging module
"""

import logging

# logging.error("this is a error")    # CRITICAL & ERROR & WARNING => show
# logging.debug("this is a debug")    # DEBUG & NotSet & INFO => not show

# --------------------------------------------------------------------------------------------------------------------

# logging.basicConfig(level=logging.INFO)  # level = baes mish DEBUG & NotSet & INFO chap beshan.
#
# logging.info("this is a info")  # Show msg

# --------------------------------------------------------------------------------------------------------------------

# name = "mohammadhssn"
#
# logging.basicConfig(filename="msg.log")     # save in file
# logging.error(f"{name} raise a error")

# --------------------------------------------------------------------------------------------------------------------


# logging.basicConfig(filename="msg.log", format='%(asctime)s-%(filename)s-%(message)s')
#
# a = {'name': 'mohammadhssn'}
#
# try:
#     print(a['age'])
# except Exception:
#     logging.exception("this is a error")