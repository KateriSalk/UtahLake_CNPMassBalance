points = [
	[datetime.datetime(2020, 7, 9, 13, 45), datetime.datetime(2020, 7, 9, 14, 0), datetime.datetime(2020, 8, 13, 13, 15), datetime.datetime(2020, 8, 13, 13, 30)]][0]
edit_service.select_points([], points)
edit_service.interpolate()
points = [
	[datetime.datetime(2020, 7, 8, 2, 0)]][0]
edit_service.select_points([], points)
edit_service.filter_date(datetime.datetime(2020, 8, 14, 23, 59, 59), datetime.datetime(2020, 7, 8, 0, 0))
edit_service.change_value_threshold(20.0,'>')
edit_service.interpolate()
edit_service.reset_filter()
