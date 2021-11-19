"""
    time module :
        gmtime(), time(), ctime(), sleep(), strftime(),
        perf_counter(), process_time()

        epoch = 1-1-1970  00-00-00
"""

import time as tm

# print(tm.gmtime())              # zamani alan ro neshoon mide
# print(tm.gmtime(20000000))      # yek meghdar bar hasbe saniye migire ke zamani az epock rafte jelo ro neshoon mide.


# print(tm.ctime())                 # tarikh va zaman alan ro neshoon mide    mesle => Fri Jul 30 20:53:38 2021

# print(tm.sleep(5))      # sleep yek meghdar bar hasbe saniye migire va barname motevaghef mishe (cpu kar nemikonad)

# print(tm.strftime("%d/%m/%Y - %H:%M:%S %p"))

#print("------------------------------------------------------------------------------------------------------------")

# perf_counter()    zamani ke barname ejra shode va karbar mibine
# process_time()    zamani ke cpu barname ro ejra mikon

# perf_counter_start = tm.perf_counter()
# process_time_start = tm.process_time()
#
#
# tm.sleep(5)
#
#
# perf_counter_end = tm.perf_counter()
# process_time_end = tm.process_time()
#
# print(perf_counter_end - perf_counter_start )   # 5.014326
# print(process_time_end - process_time_start)    # 0
