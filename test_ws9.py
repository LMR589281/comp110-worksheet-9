# Do not edit, rename or delete this file!

import pytest
import os

dat = {}

with open("save.dat", "rt") as datfile:
	for line in datfile:
		if '=' in line:
			key, value = [x.strip() for x in line.split("=")]
			dat[key] = value

which_tests = os.getenv('TEST_SET', 'core')

if which_tests == 'core':
	levels = [
		("00150", "Self-Test Diagnostic"),
		("10981", "Signal Amplifier"),
		("20176", "Differential Converter"),
		("21340", "Signal Comparator"),
		("22280", "Signal Multiplexer"),
		("30647", "Sequence Generator"),
		("31904", "Sequence Counter"),
		("32050", "Signal Edge Detector"),
		("33762", "Interrupt Handler"),
		("40196", "Signal Pattern Detector"),
		("41427", "Sequence Peak Detector"),
		("42656", "Sequence Reverser"),
		("43786", "Signal Multiplier")
	]
	
	@pytest.mark.parametrize("level_id,level_friendly_name", levels)
	def test_level_completed(level_id, level_friendly_name):
		assert ("Best.%s.Cycles" % level_id) in dat, "'%s' has not been passed" % level_friendly_name

elif which_tests == 'stretch_a':
	def test_diffconv_250():
		key = "Best.20176.Cycles"
		assert key in dat, "'Differential Converter' has not been passed"
		assert int(dat[key]) <= 250, "'Differential Converter' has not been passed in 250 cycles or fewer"

elif which_tests == 'stretch_b':
	def test_seqcount_4():
		key = "Best.31904.Nodes"
		assert key in dat, "'Sequence Counter' has not been passed"
		assert int(dat[key]) <= 4, "'Sequence Counter' has not been passed in 4 nodes or fewer"

elif which_tests == 'stretch_c':
	def test_seqsort():
		assert "Best.63534.Cycles" in dat, "'Sequence Sorter' has not been passed"
