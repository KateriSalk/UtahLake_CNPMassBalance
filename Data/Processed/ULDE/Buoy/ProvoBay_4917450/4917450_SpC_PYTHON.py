#SpC for 4917450
#filter gaps
edit_service.fill_gap(gap = [u'16', u'minute'], fill= [u'15', u'minute'])
points = [
	[datetime.datetime(2020, 8, 24, 10, 30), datetime.datetime(2020, 8, 24, 10, 45), datetime.datetime(2020, 8, 24, 11, 0), datetime.datetime(2020, 8, 24, 11, 15), datetime.datetime(2020, 8, 24, 11, 30), datetime.datetime(2020, 8, 24, 11, 45), datetime.datetime(2020, 8, 24, 12, 0), datetime.datetime(2020, 8, 24, 12, 15), datetime.datetime(2020, 8, 24, 12, 30), datetime.datetime(2020, 8, 24, 12, 45), datetime.datetime(2020, 8, 24, 13, 0), datetime.datetime(2020, 8, 24, 13, 15), datetime.datetime(2020, 8, 24, 13, 30), datetime.datetime(2020, 8, 24, 13, 45), datetime.datetime(2020, 8, 24, 14, 0), datetime.datetime(2020, 8, 24, 14, 15), datetime.datetime(2020, 8, 24, 14, 30), datetime.datetime(2020, 8, 24, 14, 45), datetime.datetime(2020, 8, 24, 15, 0), datetime.datetime(2020, 8, 24, 15, 15), datetime.datetime(2020, 8, 24, 15, 30), datetime.datetime(2020, 8, 24, 15, 45), datetime.datetime(2020, 8, 24, 16, 0), datetime.datetime(2020, 8, 24, 16, 15), datetime.datetime(2020, 8, 24, 16, 30), datetime.datetime(2020, 8, 24, 16, 45), datetime.datetime(2020, 8, 24, 17, 0), datetime.datetime(2020, 8, 24, 17, 15), datetime.datetime(2020, 8, 24, 17, 30), datetime.datetime(2020, 8, 24, 17, 45), datetime.datetime(2020, 8, 24, 18, 0), datetime.datetime(2020, 8, 24, 18, 15), datetime.datetime(2020, 8, 24, 18, 30), datetime.datetime(2020, 8, 24, 18, 45), datetime.datetime(2020, 8, 24, 19, 0), datetime.datetime(2020, 8, 24, 19, 15), datetime.datetime(2020, 8, 24, 19, 30), datetime.datetime(2020, 8, 24, 19, 45), datetime.datetime(2020, 8, 24, 20, 0), datetime.datetime(2020, 8, 24, 20, 15), datetime.datetime(2020, 8, 24, 20, 30), datetime.datetime(2020, 8, 24, 20, 45), datetime.datetime(2020, 8, 24, 21, 0), datetime.datetime(2020, 8, 24, 21, 15), datetime.datetime(2020, 8, 24, 21, 30), datetime.datetime(2020, 8, 24, 21, 45), datetime.datetime(2020, 8, 24, 22, 0), datetime.datetime(2020, 8, 24, 22, 15), datetime.datetime(2020, 8, 24, 22, 30), datetime.datetime(2020, 8, 24, 22, 45), datetime.datetime(2020, 8, 24, 23, 0), datetime.datetime(2020, 8, 24, 23, 15), datetime.datetime(2020, 8, 24, 23, 30), datetime.datetime(2020, 8, 24, 23, 45), datetime.datetime(2020, 8, 25, 0, 0), datetime.datetime(2020, 8, 25, 0, 15), datetime.datetime(2020, 8, 25, 0, 30), datetime.datetime(2020, 8, 25, 0, 45), datetime.datetime(2020, 8, 25, 1, 0), datetime.datetime(2020, 8, 25, 1, 15), datetime.datetime(2020, 8, 25, 1, 30), datetime.datetime(2020, 8, 25, 1, 45), datetime.datetime(2020, 8, 25, 2, 0), datetime.datetime(2020, 8, 25, 2, 15), datetime.datetime(2020, 8, 25, 2, 30), datetime.datetime(2020, 8, 25, 2, 45), datetime.datetime(2020, 8, 25, 3, 0), datetime.datetime(2020, 8, 25, 3, 15), datetime.datetime(2020, 8, 25, 3, 30), datetime.datetime(2020, 8, 25, 3, 45), datetime.datetime(2020, 8, 25, 4, 0), datetime.datetime(2020, 8, 25, 4, 15), datetime.datetime(2020, 8, 25, 4, 30), datetime.datetime(2020, 8, 25, 4, 45), datetime.datetime(2020, 8, 25, 5, 0), datetime.datetime(2020, 8, 25, 5, 15), datetime.datetime(2020, 8, 25, 5, 30), datetime.datetime(2020, 8, 25, 5, 45), datetime.datetime(2020, 8, 25, 6, 0), datetime.datetime(2020, 8, 25, 6, 15), datetime.datetime(2020, 8, 25, 6, 30), datetime.datetime(2020, 8, 25, 6, 45), datetime.datetime(2020, 8, 25, 7, 0), datetime.datetime(2020, 8, 25, 7, 15), datetime.datetime(2020, 8, 25, 7, 30), datetime.datetime(2020, 8, 25, 7, 45), datetime.datetime(2020, 8, 25, 8, 0), datetime.datetime(2020, 8, 25, 8, 15), datetime.datetime(2020, 8, 25, 8, 30), datetime.datetime(2020, 8, 25, 8, 45), datetime.datetime(2020, 8, 25, 9, 0), datetime.datetime(2020, 8, 25, 9, 15), datetime.datetime(2020, 8, 25, 9, 30), datetime.datetime(2020, 8, 25, 9, 45), datetime.datetime(2020, 8, 25, 10, 0), datetime.datetime(2020, 8, 25, 10, 15), datetime.datetime(2020, 8, 25, 10, 30), datetime.datetime(2020, 8, 25, 10, 45), datetime.datetime(2020, 8, 25, 11, 0), datetime.datetime(2020, 8, 25, 11, 15), datetime.datetime(2020, 8, 25, 11, 30), datetime.datetime(2020, 8, 25, 11, 45), datetime.datetime(2020, 8, 25, 12, 0), datetime.datetime(2020, 8, 25, 12, 15), datetime.datetime(2020, 8, 25, 12, 30), datetime.datetime(2020, 8, 25, 12, 45), datetime.datetime(2020, 8, 25, 13, 0), datetime.datetime(2020, 8, 25, 13, 15), datetime.datetime(2020, 8, 25, 13, 30), datetime.datetime(2020, 8, 25, 13, 45), datetime.datetime(2020, 8, 25, 14, 0), datetime.datetime(2020, 8, 25, 14, 15), datetime.datetime(2020, 8, 25, 14, 30), datetime.datetime(2020, 8, 25, 14, 45), datetime.datetime(2020, 8, 25, 15, 0), datetime.datetime(2020, 8, 25, 15, 15), datetime.datetime(2020, 8, 25, 15, 30), datetime.datetime(2020, 8, 25, 15, 45), datetime.datetime(2020, 8, 25, 16, 0), datetime.datetime(2020, 8, 25, 16, 15), datetime.datetime(2020, 8, 25, 16, 30), datetime.datetime(2020, 8, 25, 16, 45), datetime.datetime(2020, 8, 25, 17, 0), datetime.datetime(2020, 8, 25, 17, 15), datetime.datetime(2020, 8, 25, 17, 30), datetime.datetime(2020, 8, 25, 17, 45), datetime.datetime(2020, 8, 25, 18, 0), datetime.datetime(2020, 8, 25, 18, 15), datetime.datetime(2020, 8, 25, 18, 30), datetime.datetime(2020, 8, 25, 18, 45), datetime.datetime(2020, 8, 25, 19, 0), datetime.datetime(2020, 8, 25, 19, 15), datetime.datetime(2020, 8, 25, 19, 30), datetime.datetime(2020, 8, 25, 19, 45), datetime.datetime(2020, 8, 25, 20, 0), datetime.datetime(2020, 8, 25, 20, 15), datetime.datetime(2020, 8, 25, 20, 30), datetime.datetime(2020, 8, 25, 20, 45), datetime.datetime(2020, 8, 25, 21, 0), datetime.datetime(2020, 8, 25, 21, 15), datetime.datetime(2020, 8, 25, 21, 30), datetime.datetime(2020, 8, 25, 21, 45), datetime.datetime(2020, 8, 25, 22, 0), datetime.datetime(2020, 8, 25, 22, 15), datetime.datetime(2020, 8, 25, 22, 30), datetime.datetime(2020, 8, 25, 22, 45), datetime.datetime(2020, 8, 25, 23, 0), datetime.datetime(2020, 8, 25, 23, 15), datetime.datetime(2020, 8, 25, 23, 30), datetime.datetime(2020, 8, 25, 23, 45), datetime.datetime(2020, 8, 26, 0, 0), datetime.datetime(2020, 8, 26, 0, 15), datetime.datetime(2020, 8, 26, 0, 30), datetime.datetime(2020, 8, 26, 0, 45), datetime.datetime(2020, 8, 26, 1, 0), datetime.datetime(2020, 8, 26, 1, 15), datetime.datetime(2020, 8, 26, 1, 30), datetime.datetime(2020, 8, 26, 1, 45), datetime.datetime(2020, 8, 26, 2, 0), datetime.datetime(2020, 8, 26, 2, 15), datetime.datetime(2020, 8, 26, 2, 30), datetime.datetime(2020, 8, 26, 2, 45), datetime.datetime(2020, 8, 26, 3, 0), datetime.datetime(2020, 8, 26, 3, 15), datetime.datetime(2020, 8, 26, 3, 30), datetime.datetime(2020, 8, 26, 3, 45), datetime.datetime(2020, 8, 26, 4, 0), datetime.datetime(2020, 8, 26, 4, 15), datetime.datetime(2020, 8, 26, 4, 30), datetime.datetime(2020, 8, 26, 4, 45), datetime.datetime(2020, 8, 26, 5, 0), datetime.datetime(2020, 8, 26, 5, 15), datetime.datetime(2020, 8, 26, 5, 30), datetime.datetime(2020, 8, 26, 5, 45), datetime.datetime(2020, 8, 26, 6, 0), datetime.datetime(2020, 8, 26, 6, 15), datetime.datetime(2020, 8, 26, 6, 30), datetime.datetime(2020, 8, 26, 6, 45), datetime.datetime(2020, 8, 26, 7, 0), datetime.datetime(2020, 8, 26, 7, 15), datetime.datetime(2020, 8, 26, 7, 30), datetime.datetime(2020, 8, 26, 7, 45), datetime.datetime(2020, 8, 26, 8, 0), datetime.datetime(2020, 8, 26, 8, 15), datetime.datetime(2020, 8, 26, 8, 30), datetime.datetime(2020, 8, 26, 8, 45), datetime.datetime(2020, 8, 26, 9, 0), datetime.datetime(2020, 8, 26, 9, 15), datetime.datetime(2020, 8, 26, 9, 30), datetime.datetime(2020, 8, 26, 9, 45), datetime.datetime(2020, 8, 26, 10, 0), datetime.datetime(2020, 8, 26, 10, 15), datetime.datetime(2020, 8, 26, 10, 30), datetime.datetime(2020, 8, 26, 10, 45), datetime.datetime(2020, 8, 26, 11, 0), datetime.datetime(2020, 8, 26, 11, 15), datetime.datetime(2020, 8, 26, 11, 30), datetime.datetime(2020, 8, 26, 11, 45), datetime.datetime(2020, 8, 26, 12, 0), datetime.datetime(2020, 8, 26, 12, 15), datetime.datetime(2020, 8, 26, 12, 30), datetime.datetime(2020, 8, 26, 12, 45), datetime.datetime(2020, 8, 26, 13, 0), datetime.datetime(2020, 8, 26, 13, 15), datetime.datetime(2020, 8, 26, 13, 30), datetime.datetime(2020, 8, 26, 13, 45), datetime.datetime(2020, 8, 26, 14, 0), datetime.datetime(2020, 8, 26, 14, 15), datetime.datetime(2020, 8, 26, 14, 30), datetime.datetime(2020, 8, 26, 14, 45), datetime.datetime(2020, 8, 26, 15, 0), datetime.datetime(2020, 8, 26, 15, 15), datetime.datetime(2020, 8, 26, 15, 30), datetime.datetime(2020, 8, 26, 15, 45), datetime.datetime(2020, 8, 26, 16, 0), datetime.datetime(2020, 8, 26, 16, 15), datetime.datetime(2020, 8, 26, 16, 30), datetime.datetime(2020, 8, 26, 16, 45), datetime.datetime(2020, 8, 26, 17, 0), datetime.datetime(2020, 8, 26, 17, 15), datetime.datetime(2020, 8, 26, 17, 30), datetime.datetime(2020, 8, 26, 17, 45), datetime.datetime(2020, 8, 26, 18, 0), datetime.datetime(2020, 8, 26, 18, 15), datetime.datetime(2020, 8, 26, 18, 30), datetime.datetime(2020, 8, 26, 18, 45), datetime.datetime(2020, 8, 26, 19, 0), datetime.datetime(2020, 8, 26, 19, 15), datetime.datetime(2020, 8, 26, 19, 30), datetime.datetime(2020, 8, 26, 19, 45), datetime.datetime(2020, 8, 26, 20, 0), datetime.datetime(2020, 8, 26, 20, 15), datetime.datetime(2020, 8, 26, 20, 30), datetime.datetime(2020, 8, 26, 20, 45), datetime.datetime(2020, 8, 26, 21, 0), datetime.datetime(2020, 8, 26, 21, 15), datetime.datetime(2020, 8, 26, 21, 30), datetime.datetime(2020, 8, 26, 21, 45), datetime.datetime(2020, 8, 26, 22, 0), datetime.datetime(2020, 8, 26, 22, 15), datetime.datetime(2020, 8, 26, 22, 30), datetime.datetime(2020, 8, 26, 22, 45), datetime.datetime(2020, 8, 26, 23, 0), datetime.datetime(2020, 8, 26, 23, 15), datetime.datetime(2020, 8, 26, 23, 30), datetime.datetime(2020, 8, 26, 23, 45), datetime.datetime(2020, 8, 27, 0, 0), datetime.datetime(2020, 8, 27, 0, 15), datetime.datetime(2020, 8, 27, 0, 30), datetime.datetime(2020, 8, 27, 0, 45), datetime.datetime(2020, 8, 27, 1, 0), datetime.datetime(2020, 8, 27, 1, 15), datetime.datetime(2020, 8, 27, 1, 30), datetime.datetime(2020, 8, 27, 1, 45), datetime.datetime(2020, 8, 27, 2, 0), datetime.datetime(2020, 8, 27, 2, 15), datetime.datetime(2020, 8, 27, 2, 30), datetime.datetime(2020, 8, 27, 2, 45), datetime.datetime(2020, 8, 27, 3, 0), datetime.datetime(2020, 8, 27, 3, 15), datetime.datetime(2020, 8, 27, 3, 30), datetime.datetime(2020, 8, 27, 3, 45), datetime.datetime(2020, 8, 27, 4, 0), datetime.datetime(2020, 8, 27, 4, 15), datetime.datetime(2020, 8, 27, 4, 30), datetime.datetime(2020, 8, 27, 4, 45), datetime.datetime(2020, 8, 27, 5, 0), datetime.datetime(2020, 8, 27, 5, 15), datetime.datetime(2020, 8, 27, 5, 30), datetime.datetime(2020, 8, 27, 5, 45), datetime.datetime(2020, 8, 27, 6, 0), datetime.datetime(2020, 8, 27, 6, 15), datetime.datetime(2020, 8, 27, 6, 30), datetime.datetime(2020, 8, 27, 6, 45), datetime.datetime(2020, 8, 27, 7, 0), datetime.datetime(2020, 8, 27, 7, 15), datetime.datetime(2020, 8, 27, 7, 30), datetime.datetime(2020, 8, 27, 7, 45), datetime.datetime(2020, 8, 27, 8, 0), datetime.datetime(2020, 8, 27, 8, 15), datetime.datetime(2020, 8, 27, 8, 30), datetime.datetime(2020, 8, 27, 8, 45), datetime.datetime(2020, 8, 27, 9, 0), datetime.datetime(2020, 8, 27, 9, 15), datetime.datetime(2020, 8, 27, 9, 30), datetime.datetime(2020, 8, 27, 9, 45), datetime.datetime(2020, 8, 27, 10, 0), datetime.datetime(2020, 8, 27, 10, 15), datetime.datetime(2020, 8, 27, 10, 30), datetime.datetime(2020, 8, 27, 10, 45), datetime.datetime(2020, 8, 27, 11, 0), datetime.datetime(2020, 8, 27, 11, 15), datetime.datetime(2020, 8, 27, 11, 30), datetime.datetime(2020, 8, 27, 11, 45), datetime.datetime(2020, 8, 27, 12, 0), datetime.datetime(2020, 8, 27, 12, 15), datetime.datetime(2020, 8, 27, 12, 30), datetime.datetime(2020, 8, 27, 12, 45), datetime.datetime(2020, 8, 27, 13, 0), datetime.datetime(2020, 8, 27, 13, 15), datetime.datetime(2020, 8, 27, 13, 30), datetime.datetime(2020, 8, 27, 13, 45), datetime.datetime(2020, 8, 27, 14, 0), datetime.datetime(2020, 8, 27, 14, 15), datetime.datetime(2020, 8, 27, 14, 30), datetime.datetime(2020, 8, 27, 14, 45), datetime.datetime(2020, 8, 27, 15, 0), datetime.datetime(2020, 8, 27, 15, 15), datetime.datetime(2020, 8, 27, 15, 30), datetime.datetime(2020, 8, 27, 15, 45), datetime.datetime(2020, 8, 27, 16, 0), datetime.datetime(2020, 8, 27, 16, 15), datetime.datetime(2020, 8, 27, 16, 30), datetime.datetime(2020, 8, 27, 16, 45), datetime.datetime(2020, 8, 27, 17, 0), datetime.datetime(2020, 8, 27, 17, 15), datetime.datetime(2020, 8, 27, 17, 30), datetime.datetime(2020, 8, 27, 17, 45), datetime.datetime(2020, 8, 27, 18, 0), datetime.datetime(2020, 8, 27, 18, 15), datetime.datetime(2020, 8, 27, 18, 30), datetime.datetime(2020, 8, 27, 18, 45), datetime.datetime(2020, 8, 27, 19, 0), datetime.datetime(2020, 8, 27, 19, 15), datetime.datetime(2020, 8, 27, 19, 30), datetime.datetime(2020, 8, 27, 19, 45), datetime.datetime(2020, 8, 27, 20, 0), datetime.datetime(2020, 8, 27, 20, 15), datetime.datetime(2020, 8, 27, 20, 30), datetime.datetime(2020, 8, 27, 20, 45), datetime.datetime(2020, 8, 27, 21, 0), datetime.datetime(2020, 8, 27, 21, 15), datetime.datetime(2020, 8, 27, 21, 30), datetime.datetime(2020, 8, 27, 21, 45), datetime.datetime(2020, 8, 27, 22, 0), datetime.datetime(2020, 8, 27, 22, 15), datetime.datetime(2020, 8, 27, 22, 30), datetime.datetime(2020, 8, 27, 22, 45), datetime.datetime(2020, 8, 27, 23, 0), datetime.datetime(2020, 8, 27, 23, 15), datetime.datetime(2020, 8, 27, 23, 30), datetime.datetime(2020, 8, 27, 23, 45), datetime.datetime(2020, 8, 28, 0, 0), datetime.datetime(2020, 8, 28, 0, 15), datetime.datetime(2020, 8, 28, 0, 30), datetime.datetime(2020, 8, 28, 0, 45), datetime.datetime(2020, 8, 28, 1, 0), datetime.datetime(2020, 8, 28, 1, 15), datetime.datetime(2020, 8, 28, 1, 30), datetime.datetime(2020, 8, 28, 1, 45), datetime.datetime(2020, 8, 28, 2, 0), datetime.datetime(2020, 8, 28, 2, 15), datetime.datetime(2020, 8, 28, 2, 30), datetime.datetime(2020, 8, 28, 2, 45), datetime.datetime(2020, 8, 28, 3, 0), datetime.datetime(2020, 8, 28, 3, 15), datetime.datetime(2020, 8, 28, 3, 30), datetime.datetime(2020, 8, 28, 3, 45), datetime.datetime(2020, 8, 28, 4, 0), datetime.datetime(2020, 8, 28, 4, 15), datetime.datetime(2020, 8, 28, 4, 30), datetime.datetime(2020, 8, 28, 4, 45), datetime.datetime(2020, 8, 28, 5, 0), datetime.datetime(2020, 8, 28, 5, 15), datetime.datetime(2020, 8, 28, 5, 30), datetime.datetime(2020, 8, 28, 5, 45), datetime.datetime(2020, 8, 28, 6, 0), datetime.datetime(2020, 8, 28, 6, 15), datetime.datetime(2020, 8, 28, 6, 30), datetime.datetime(2020, 8, 28, 6, 45), datetime.datetime(2020, 8, 28, 7, 0), datetime.datetime(2020, 8, 28, 7, 15), datetime.datetime(2020, 8, 28, 7, 30), datetime.datetime(2020, 8, 28, 7, 45), datetime.datetime(2020, 8, 28, 8, 0), datetime.datetime(2020, 8, 28, 8, 15), datetime.datetime(2020, 8, 28, 8, 30), datetime.datetime(2020, 8, 28, 8, 45), datetime.datetime(2020, 8, 28, 9, 0), datetime.datetime(2020, 8, 28, 9, 15), datetime.datetime(2020, 8, 28, 9, 30), datetime.datetime(2020, 8, 28, 9, 45), datetime.datetime(2020, 8, 28, 10, 0), datetime.datetime(2020, 8, 28, 10, 15), datetime.datetime(2020, 8, 28, 10, 30), datetime.datetime(2020, 8, 28, 10, 45), datetime.datetime(2020, 8, 28, 11, 0), datetime.datetime(2020, 8, 28, 11, 15), datetime.datetime(2020, 8, 28, 11, 30), datetime.datetime(2020, 8, 28, 11, 45), datetime.datetime(2020, 8, 28, 12, 0), datetime.datetime(2020, 8, 28, 12, 15), datetime.datetime(2020, 8, 28, 12, 30), datetime.datetime(2020, 8, 28, 12, 45), datetime.datetime(2020, 8, 28, 13, 0), datetime.datetime(2020, 8, 28, 13, 15), datetime.datetime(2020, 8, 28, 13, 30), datetime.datetime(2020, 8, 28, 13, 45), datetime.datetime(2020, 8, 28, 14, 0), datetime.datetime(2020, 8, 28, 14, 15), datetime.datetime(2020, 8, 28, 14, 30), datetime.datetime(2020, 8, 28, 14, 45), datetime.datetime(2020, 8, 28, 15, 0), datetime.datetime(2020, 8, 28, 15, 15), datetime.datetime(2020, 8, 28, 15, 30), datetime.datetime(2020, 8, 28, 15, 45), datetime.datetime(2020, 8, 28, 16, 0), datetime.datetime(2020, 8, 28, 16, 15), datetime.datetime(2020, 8, 28, 16, 30), datetime.datetime(2020, 8, 28, 16, 45), datetime.datetime(2020, 8, 28, 17, 0), datetime.datetime(2020, 8, 28, 17, 15), datetime.datetime(2020, 8, 28, 17, 30), datetime.datetime(2020, 8, 28, 17, 45), datetime.datetime(2020, 8, 28, 18, 0), datetime.datetime(2020, 8, 28, 18, 15), datetime.datetime(2020, 8, 28, 18, 30), datetime.datetime(2020, 8, 28, 18, 45), datetime.datetime(2020, 8, 28, 19, 0), datetime.datetime(2020, 8, 28, 19, 15), datetime.datetime(2020, 8, 28, 19, 30), datetime.datetime(2020, 8, 28, 19, 45), datetime.datetime(2020, 8, 28, 20, 0), datetime.datetime(2020, 8, 28, 20, 15), datetime.datetime(2020, 8, 28, 20, 30), datetime.datetime(2020, 8, 28, 20, 45), datetime.datetime(2020, 8, 28, 21, 0), datetime.datetime(2020, 8, 28, 21, 15), datetime.datetime(2020, 8, 28, 21, 30), datetime.datetime(2020, 8, 28, 21, 45), datetime.datetime(2020, 8, 28, 22, 0), datetime.datetime(2020, 8, 28, 22, 15), datetime.datetime(2020, 8, 28, 22, 30), datetime.datetime(2020, 8, 28, 22, 45), datetime.datetime(2020, 8, 28, 23, 0), datetime.datetime(2020, 8, 28, 23, 15), datetime.datetime(2020, 8, 28, 23, 30), datetime.datetime(2020, 8, 28, 23, 45), datetime.datetime(2020, 8, 29, 0, 0), datetime.datetime(2020, 8, 29, 0, 15), datetime.datetime(2020, 8, 29, 0, 30), datetime.datetime(2020, 8, 29, 0, 45), datetime.datetime(2020, 8, 29, 1, 0), datetime.datetime(2020, 8, 29, 1, 15), datetime.datetime(2020, 8, 29, 1, 30), datetime.datetime(2020, 8, 29, 1, 45), datetime.datetime(2020, 8, 29, 2, 0), datetime.datetime(2020, 8, 29, 2, 15), datetime.datetime(2020, 8, 29, 2, 30), datetime.datetime(2020, 8, 29, 2, 45), datetime.datetime(2020, 8, 29, 3, 0), datetime.datetime(2020, 8, 29, 3, 15), datetime.datetime(2020, 8, 29, 3, 30), datetime.datetime(2020, 8, 29, 3, 45), datetime.datetime(2020, 8, 29, 4, 0), datetime.datetime(2020, 8, 29, 4, 15), datetime.datetime(2020, 8, 29, 4, 30), datetime.datetime(2020, 8, 29, 4, 45), datetime.datetime(2020, 8, 29, 5, 0), datetime.datetime(2020, 8, 29, 5, 15), datetime.datetime(2020, 8, 29, 5, 30), datetime.datetime(2020, 8, 29, 5, 45), datetime.datetime(2020, 8, 29, 6, 0), datetime.datetime(2020, 8, 29, 6, 15), datetime.datetime(2020, 8, 29, 6, 30), datetime.datetime(2020, 8, 29, 6, 45), datetime.datetime(2020, 8, 29, 7, 0), datetime.datetime(2020, 8, 29, 7, 15), datetime.datetime(2020, 8, 29, 7, 30), datetime.datetime(2020, 8, 29, 7, 45), datetime.datetime(2020, 8, 29, 8, 0), datetime.datetime(2020, 8, 29, 8, 15), datetime.datetime(2020, 8, 29, 8, 30), datetime.datetime(2020, 8, 29, 8, 45), datetime.datetime(2020, 8, 29, 9, 0), datetime.datetime(2020, 8, 29, 9, 15), datetime.datetime(2020, 8, 29, 9, 30), datetime.datetime(2020, 8, 29, 9, 45), datetime.datetime(2020, 8, 29, 10, 0), datetime.datetime(2020, 8, 29, 10, 15), datetime.datetime(2020, 8, 29, 10, 30), datetime.datetime(2020, 8, 29, 10, 45), datetime.datetime(2020, 8, 29, 11, 0), datetime.datetime(2020, 8, 29, 11, 15), datetime.datetime(2020, 8, 29, 11, 30), datetime.datetime(2020, 8, 29, 11, 45), datetime.datetime(2020, 8, 29, 12, 0), datetime.datetime(2020, 8, 29, 12, 15), datetime.datetime(2020, 8, 29, 12, 30), datetime.datetime(2020, 8, 29, 12, 45), datetime.datetime(2020, 8, 29, 13, 0), datetime.datetime(2020, 8, 29, 13, 15), datetime.datetime(2020, 8, 29, 13, 30), datetime.datetime(2020, 8, 29, 13, 45), datetime.datetime(2020, 8, 29, 14, 0), datetime.datetime(2020, 8, 29, 14, 15), datetime.datetime(2020, 8, 29, 14, 30), datetime.datetime(2020, 8, 29, 14, 45), datetime.datetime(2020, 8, 29, 15, 0), datetime.datetime(2020, 8, 29, 15, 15), datetime.datetime(2020, 8, 29, 15, 30), datetime.datetime(2020, 8, 29, 15, 45), datetime.datetime(2020, 8, 29, 16, 0), datetime.datetime(2020, 8, 29, 16, 15), datetime.datetime(2020, 8, 29, 16, 30), datetime.datetime(2020, 8, 29, 16, 45), datetime.datetime(2020, 8, 29, 17, 0), datetime.datetime(2020, 8, 29, 17, 15), datetime.datetime(2020, 8, 29, 17, 30), datetime.datetime(2020, 8, 29, 17, 45), datetime.datetime(2020, 8, 29, 18, 0), datetime.datetime(2020, 8, 29, 18, 15), datetime.datetime(2020, 8, 29, 18, 30), datetime.datetime(2020, 8, 29, 18, 45), datetime.datetime(2020, 8, 29, 19, 0), datetime.datetime(2020, 8, 29, 19, 15), datetime.datetime(2020, 8, 29, 19, 30), datetime.datetime(2020, 8, 29, 19, 45), datetime.datetime(2020, 8, 29, 20, 0), datetime.datetime(2020, 8, 29, 20, 15), datetime.datetime(2020, 8, 29, 20, 30), datetime.datetime(2020, 8, 29, 20, 45), datetime.datetime(2020, 8, 29, 21, 0), datetime.datetime(2020, 8, 29, 21, 15), datetime.datetime(2020, 8, 29, 21, 30), datetime.datetime(2020, 8, 29, 21, 45), datetime.datetime(2020, 8, 29, 22, 0), datetime.datetime(2020, 8, 29, 22, 15), datetime.datetime(2020, 8, 29, 22, 30), datetime.datetime(2020, 8, 29, 22, 45), datetime.datetime(2020, 8, 29, 23, 0), datetime.datetime(2020, 8, 29, 23, 15), datetime.datetime(2020, 8, 29, 23, 30), datetime.datetime(2020, 8, 29, 23, 45), datetime.datetime(2020, 8, 30, 0, 0), datetime.datetime(2020, 8, 30, 0, 15), datetime.datetime(2020, 8, 30, 0, 30), datetime.datetime(2020, 8, 30, 0, 45), datetime.datetime(2020, 8, 30, 1, 0), datetime.datetime(2020, 8, 30, 1, 15), datetime.datetime(2020, 8, 30, 1, 30), datetime.datetime(2020, 8, 30, 1, 45), datetime.datetime(2020, 8, 30, 2, 0), datetime.datetime(2020, 8, 30, 2, 15), datetime.datetime(2020, 8, 30, 2, 30), datetime.datetime(2020, 8, 30, 2, 45), datetime.datetime(2020, 8, 30, 3, 0), datetime.datetime(2020, 8, 30, 3, 15), datetime.datetime(2020, 8, 30, 3, 30), datetime.datetime(2020, 8, 30, 3, 45), datetime.datetime(2020, 8, 30, 4, 0), datetime.datetime(2020, 8, 30, 4, 15), datetime.datetime(2020, 8, 30, 4, 30), datetime.datetime(2020, 8, 30, 4, 45), datetime.datetime(2020, 8, 30, 5, 0), datetime.datetime(2020, 8, 30, 5, 15), datetime.datetime(2020, 8, 30, 5, 30), datetime.datetime(2020, 8, 30, 5, 45), datetime.datetime(2020, 8, 30, 6, 0), datetime.datetime(2020, 8, 30, 6, 15), datetime.datetime(2020, 8, 30, 6, 30), datetime.datetime(2020, 8, 30, 6, 45), datetime.datetime(2020, 8, 30, 7, 0), datetime.datetime(2020, 8, 30, 7, 15), datetime.datetime(2020, 8, 30, 7, 30), datetime.datetime(2020, 8, 30, 7, 45), datetime.datetime(2020, 8, 30, 8, 0), datetime.datetime(2020, 8, 30, 8, 15), datetime.datetime(2020, 8, 30, 8, 30), datetime.datetime(2020, 8, 30, 8, 45), datetime.datetime(2020, 8, 30, 9, 0), datetime.datetime(2020, 8, 30, 9, 15), datetime.datetime(2020, 8, 30, 9, 30), datetime.datetime(2020, 8, 30, 9, 45), datetime.datetime(2020, 8, 30, 10, 0), datetime.datetime(2020, 8, 30, 10, 15), datetime.datetime(2020, 8, 30, 10, 30), datetime.datetime(2020, 8, 30, 10, 45), datetime.datetime(2020, 8, 30, 11, 0), datetime.datetime(2020, 8, 30, 11, 15), datetime.datetime(2020, 8, 30, 11, 30), datetime.datetime(2020, 8, 30, 11, 45), datetime.datetime(2020, 8, 30, 12, 0), datetime.datetime(2020, 8, 30, 12, 15), datetime.datetime(2020, 8, 30, 12, 30), datetime.datetime(2020, 8, 30, 12, 45), datetime.datetime(2020, 8, 30, 13, 0), datetime.datetime(2020, 8, 30, 13, 15), datetime.datetime(2020, 8, 30, 13, 30), datetime.datetime(2020, 8, 30, 13, 45), datetime.datetime(2020, 8, 30, 14, 0), datetime.datetime(2020, 8, 30, 14, 15), datetime.datetime(2020, 8, 30, 14, 30), datetime.datetime(2020, 8, 30, 14, 45), datetime.datetime(2020, 8, 30, 15, 0), datetime.datetime(2020, 8, 30, 15, 15), datetime.datetime(2020, 8, 30, 15, 30), datetime.datetime(2020, 8, 30, 15, 45), datetime.datetime(2020, 8, 30, 16, 0), datetime.datetime(2020, 8, 30, 16, 15), datetime.datetime(2020, 8, 30, 16, 30), datetime.datetime(2020, 8, 30, 16, 45), datetime.datetime(2020, 8, 30, 17, 0), datetime.datetime(2020, 8, 30, 17, 15), datetime.datetime(2020, 8, 30, 17, 30), datetime.datetime(2020, 8, 30, 17, 45), datetime.datetime(2020, 8, 30, 18, 0), datetime.datetime(2020, 8, 30, 18, 15), datetime.datetime(2020, 8, 30, 18, 30), datetime.datetime(2020, 8, 30, 18, 45), datetime.datetime(2020, 8, 30, 19, 0), datetime.datetime(2020, 8, 30, 19, 15), datetime.datetime(2020, 8, 30, 19, 30), datetime.datetime(2020, 8, 30, 19, 45), datetime.datetime(2020, 8, 30, 20, 0), datetime.datetime(2020, 8, 30, 20, 15), datetime.datetime(2020, 8, 30, 20, 30), datetime.datetime(2020, 8, 30, 20, 45), datetime.datetime(2020, 8, 30, 21, 0), datetime.datetime(2020, 8, 30, 21, 15), datetime.datetime(2020, 8, 30, 21, 30), datetime.datetime(2020, 8, 30, 21, 45), datetime.datetime(2020, 8, 30, 22, 0), datetime.datetime(2020, 8, 30, 22, 15), datetime.datetime(2020, 8, 30, 22, 30), datetime.datetime(2020, 8, 30, 22, 45), datetime.datetime(2020, 8, 30, 23, 0), datetime.datetime(2020, 8, 30, 23, 15), datetime.datetime(2020, 8, 30, 23, 30), datetime.datetime(2020, 8, 30, 23, 45), datetime.datetime(2020, 8, 31, 0, 0), datetime.datetime(2020, 8, 31, 0, 15), datetime.datetime(2020, 8, 31, 0, 30), datetime.datetime(2020, 8, 31, 0, 45), datetime.datetime(2020, 8, 31, 1, 0), datetime.datetime(2020, 8, 31, 1, 15), datetime.datetime(2020, 8, 31, 1, 30), datetime.datetime(2020, 8, 31, 1, 45), datetime.datetime(2020, 8, 31, 2, 0), datetime.datetime(2020, 8, 31, 2, 15), datetime.datetime(2020, 8, 31, 2, 30), datetime.datetime(2020, 8, 31, 2, 45), datetime.datetime(2020, 8, 31, 3, 0), datetime.datetime(2020, 8, 31, 3, 15), datetime.datetime(2020, 8, 31, 3, 30), datetime.datetime(2020, 8, 31, 3, 45), datetime.datetime(2020, 8, 31, 4, 0), datetime.datetime(2020, 8, 31, 4, 15), datetime.datetime(2020, 8, 31, 4, 30), datetime.datetime(2020, 8, 31, 4, 45), datetime.datetime(2020, 8, 31, 5, 0), datetime.datetime(2020, 8, 31, 5, 15), datetime.datetime(2020, 8, 31, 5, 30), datetime.datetime(2020, 8, 31, 5, 45), datetime.datetime(2020, 8, 31, 6, 0), datetime.datetime(2020, 8, 31, 6, 15), datetime.datetime(2020, 8, 31, 6, 30), datetime.datetime(2020, 8, 31, 6, 45), datetime.datetime(2020, 8, 31, 7, 0), datetime.datetime(2020, 8, 31, 7, 15), datetime.datetime(2020, 8, 31, 7, 30), datetime.datetime(2020, 8, 31, 7, 45), datetime.datetime(2020, 8, 31, 8, 0), datetime.datetime(2020, 8, 31, 8, 15), datetime.datetime(2020, 8, 31, 8, 30), datetime.datetime(2020, 8, 31, 8, 45), datetime.datetime(2020, 8, 31, 9, 0), datetime.datetime(2020, 8, 31, 9, 15), datetime.datetime(2020, 8, 31, 9, 30), datetime.datetime(2020, 8, 31, 9, 45), datetime.datetime(2020, 8, 31, 10, 0), datetime.datetime(2020, 8, 31, 10, 15), datetime.datetime(2020, 8, 31, 10, 30), datetime.datetime(2020, 8, 31, 10, 45), datetime.datetime(2020, 8, 31, 11, 0), datetime.datetime(2020, 8, 31, 11, 15), datetime.datetime(2020, 8, 31, 11, 30), datetime.datetime(2020, 8, 31, 11, 45), datetime.datetime(2020, 8, 31, 12, 0), datetime.datetime(2020, 8, 31, 12, 15), datetime.datetime(2020, 8, 31, 12, 30), datetime.datetime(2020, 8, 31, 12, 45), datetime.datetime(2020, 8, 31, 13, 0), datetime.datetime(2020, 8, 31, 13, 15), datetime.datetime(2020, 8, 31, 13, 30), datetime.datetime(2020, 8, 31, 13, 45), datetime.datetime(2020, 8, 31, 14, 0), datetime.datetime(2020, 8, 31, 14, 15), datetime.datetime(2020, 8, 31, 14, 30), datetime.datetime(2020, 8, 31, 14, 45), datetime.datetime(2020, 8, 31, 15, 0), datetime.datetime(2020, 8, 31, 15, 15), datetime.datetime(2020, 8, 31, 15, 30), datetime.datetime(2020, 8, 31, 15, 45), datetime.datetime(2020, 8, 31, 16, 0), datetime.datetime(2020, 8, 31, 16, 15), datetime.datetime(2020, 8, 31, 16, 30), datetime.datetime(2020, 8, 31, 16, 45), datetime.datetime(2020, 8, 31, 17, 0), datetime.datetime(2020, 8, 31, 17, 15), datetime.datetime(2020, 8, 31, 17, 30), datetime.datetime(2020, 8, 31, 17, 45), datetime.datetime(2020, 8, 31, 18, 0), datetime.datetime(2020, 8, 31, 18, 15), datetime.datetime(2020, 8, 31, 18, 30), datetime.datetime(2020, 8, 31, 18, 45), datetime.datetime(2020, 8, 31, 19, 0), datetime.datetime(2020, 8, 31, 19, 15), datetime.datetime(2020, 8, 31, 19, 30), datetime.datetime(2020, 8, 31, 19, 45), datetime.datetime(2020, 8, 31, 20, 0), datetime.datetime(2020, 8, 31, 20, 15), datetime.datetime(2020, 8, 31, 20, 30), datetime.datetime(2020, 8, 31, 20, 45), datetime.datetime(2020, 8, 31, 21, 0), datetime.datetime(2020, 8, 31, 21, 15), datetime.datetime(2020, 8, 31, 21, 30), datetime.datetime(2020, 8, 31, 21, 45), datetime.datetime(2020, 8, 31, 22, 0), datetime.datetime(2020, 8, 31, 22, 15), datetime.datetime(2020, 8, 31, 22, 30), datetime.datetime(2020, 8, 31, 22, 45), datetime.datetime(2020, 8, 31, 23, 0), datetime.datetime(2020, 8, 31, 23, 15), datetime.datetime(2020, 8, 31, 23, 30), datetime.datetime(2020, 8, 31, 23, 45), datetime.datetime(2020, 9, 1, 0, 0), datetime.datetime(2020, 9, 1, 0, 15), datetime.datetime(2020, 9, 1, 0, 30), datetime.datetime(2020, 9, 1, 0, 45), datetime.datetime(2020, 9, 1, 1, 0), datetime.datetime(2020, 9, 1, 1, 15), datetime.datetime(2020, 9, 1, 1, 30), datetime.datetime(2020, 9, 1, 1, 45), datetime.datetime(2020, 9, 1, 2, 0), datetime.datetime(2020, 9, 1, 2, 15), datetime.datetime(2020, 9, 1, 2, 30), datetime.datetime(2020, 9, 1, 2, 45), datetime.datetime(2020, 9, 1, 3, 0), datetime.datetime(2020, 9, 1, 3, 15), datetime.datetime(2020, 9, 1, 3, 30), datetime.datetime(2020, 9, 1, 3, 45), datetime.datetime(2020, 9, 1, 4, 0), datetime.datetime(2020, 9, 1, 4, 15), datetime.datetime(2020, 9, 1, 4, 30), datetime.datetime(2020, 9, 1, 4, 45), datetime.datetime(2020, 9, 1, 5, 0), datetime.datetime(2020, 9, 1, 5, 15), datetime.datetime(2020, 9, 1, 5, 30), datetime.datetime(2020, 9, 1, 5, 45), datetime.datetime(2020, 9, 1, 6, 0), datetime.datetime(2020, 9, 1, 6, 15), datetime.datetime(2020, 9, 1, 6, 30), datetime.datetime(2020, 9, 1, 6, 45), datetime.datetime(2020, 9, 1, 7, 0), datetime.datetime(2020, 9, 1, 7, 15), datetime.datetime(2020, 9, 1, 7, 30), datetime.datetime(2020, 9, 1, 7, 45), datetime.datetime(2020, 9, 1, 8, 0), datetime.datetime(2020, 9, 1, 8, 15), datetime.datetime(2020, 9, 1, 8, 30), datetime.datetime(2020, 9, 1, 8, 45), datetime.datetime(2020, 9, 1, 9, 0), datetime.datetime(2020, 9, 1, 9, 15), datetime.datetime(2020, 9, 1, 9, 30), datetime.datetime(2020, 9, 1, 9, 45), datetime.datetime(2020, 9, 1, 10, 0), datetime.datetime(2020, 9, 1, 10, 15)]][0]
edit_service.select_points([], points)
edit_service.delete_points()
#interpolatepoints = [
	[datetime.datetime(2020, 4, 29, 12, 15), datetime.datetime(2020, 7, 9, 13, 45), datetime.datetime(2020, 7, 9, 14, 0), datetime.datetime(2020, 8, 13, 13, 15), datetime.datetime(2020, 8, 13, 13, 30)]][0]
edit_service.select_points([], points)
edit_service.interpolate()
points = [
	[datetime.datetime(2020, 4, 20, 21, 0)]][0]
edit_service.select_points([], points)
edit_service.interpolate()
points = [
	[datetime.datetime(2020, 5, 26, 21, 45)]][0]
edit_service.select_points([], points)
edit_service.interpolate()
points = [
	[datetime.datetime(2020, 6, 30, 22, 30)]][0]
edit_service.select_points([], points)
edit_service.interpolate()
edit_service.change_value_threshold(0.0,'<')
edit_service.filter_value(0.0, '<')
new_variable = series_service.get_variable_by_id(9)
edit_service.save_existing(new_variable, None, None)