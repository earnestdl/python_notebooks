import pytest
from dateutil.parser import *

from __code import time_utility


class TestAbsoluteTimeHandler:

	def setup_method(self):
		self.starting_time = b'2020-01-10T23:55:33.303238667-05:00'

	def test_initial_absolute_format_recognized(self):
		with pytest.raises(ValueError):
			time_utility.AbsoluteTimeHandler()

	def test_wrong_initial_absolute_format_raises_error(self):
		wrong_starting_time = '2020-01-10Twrong_format'
		with pytest.raises(ValueError):
			time_utility.AbsoluteTimeHandler(initial_absolute_time=wrong_starting_time)

	def test_initial_time_correctly_parsed(self):
		o_time = time_utility.AbsoluteTimeHandler(initial_absolute_time=self.starting_time)
		formatted_initial_absolute_time = o_time.formatted_initial_absolute_time

		year_calculated = formatted_initial_absolute_time.year
		assert year_calculated == 2020

		month_calculated = formatted_initial_absolute_time.month
		assert month_calculated == 1

		day_calculated = formatted_initial_absolute_time.day
		assert day_calculated == 10

		hour_calculated = formatted_initial_absolute_time.hour
		assert hour_calculated == 23

		minute_calculated = formatted_initial_absolute_time.minute
		assert minute_calculated == 55

		second_calculated = formatted_initial_absolute_time.second
		assert second_calculated == 33

		microsecond_calculated = formatted_initial_absolute_time.microsecond
		assert microsecond_calculated == 303238

	def test_empty_delta_time_array_raises_error(self):
		o_time = time_utility.AbsoluteTimeHandler(initial_absolute_time=self.starting_time)

		with pytest.raises(ValueError):
			o_time.get_absolute_time_for_this_delta_time_array()

	def test_error_raises_if_wrong_unit_provided(self):
		o_time = time_utility.AbsoluteTimeHandler(initial_absolute_time=self.starting_time)

		with pytest.raises(NotImplementedError):
			o_time.get_absolute_time_for_this_delta_time_array(delta_time_array=[1, 2, 3],
			                                                   units="lightyear")

	def test_delta_time_array_correctly_formated(self):
		o_time = time_utility.AbsoluteTimeHandler(initial_absolute_time=self.starting_time)
		delta_time_array = [1, 2, 3, 4]
		units = 'seconds'
		o_time.get_absolute_time_for_this_delta_time_array(delta_time_array=delta_time_array,
		                                                   units=units)
		delta_time_formated = o_time.delta_time_formated

		list_hours_calculated = []
		for time_formated in delta_time_formated:
			list_hours_calculated.append(time_formated.hours)
		assert list_hours_calculated == [0, 0, 0, 0]

		list_minutes_calculated = []
		for time_formated in delta_time_formated:
			list_minutes_calculated.append(time_formated.minutes)
		assert list_minutes_calculated == [0, 0, 0, 0]

		list_seconds_calculated = []
		for time_formated in delta_time_formated:
			list_seconds_calculated.append(time_formated.seconds)
		assert list_seconds_calculated == [1, 2, 3, 4]

	def test_absolute_time_array_correctly_calculated(self):
		o_time = time_utility.AbsoluteTimeHandler(initial_absolute_time=self.starting_time)
		delta_time_array = [1, 2, 3, 4]
		units = 'seconds'
		absolute_time_array = o_time.get_absolute_time_for_this_delta_time_array(delta_time_array=delta_time_array,
		                                                                         units=units)

		expected_seconds_array = [34, 35, 36, 37]
		for index, d in enumerate(absolute_time_array):
			assert d.second == expected_seconds_array[index]
