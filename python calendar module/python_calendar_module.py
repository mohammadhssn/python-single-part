"""
    calendar module:
        methods:
            month(), calendar(), isleap(), leapdays(), monthcalendar(), month_name

        Calendar:
            itermonthdates()

        HTMLCalendar:
            formatmonth()
"""
# import calendar as cr

# methods

# print(cr.month(2020, 4))          # taghvim oon month ro miyare.
# print(cr.calendar(2020))          # taghvim oon year ro miyare.
# print(cr.isleap(2020))            # check mikone sale kanise hast ya na.
# print(cr.leapdays(2000, 2020))    # tedade slae kabise beyn 2 ta sal ro neshoon mide.
# print(cr.monthcalendar(2020, 3))  # hafte haye oon mah ro neshoon mide.
# for i in cr.month_name:           # name mah haye sal ro neshoon mide.
#     print(i)

# ------------------------------------------------------------------------------------------------------------------

# # Calendar
#
# v = cr.Calendar()
#
# for i in v.itermonthdates(2020, 3):     # tarkh rooz haye oon mah ro barmigardoone.
#     print(i)
#
# ------------------------------------------------------------------------------------------------------------------

# # HTMLCalendar
#
# h = cr.HTMLCalendar()
#
# print(h.formatmonth(2020, 4))   # code html barmigardoone.
