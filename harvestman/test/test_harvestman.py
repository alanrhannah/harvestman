import os 
import py
import pytest
import tempfile

def create_input_file():
	content = 'some keyword\nanother keyword\nsome more keywords\n'
	tmp_file = tempfile.NamedTemporaryFile(delete=False)
	tmp_file.write(content)
	tmp_file.close()
	return tmp_file

def test_read_input_file():
	expected = ['some keyword', 'another keyword', 'some more keywords']
	content = create_input_file()
	with open(content.name, 'r') as keyphrase_file:
		keyword_list = keyphrase_file.read().splitlines()

	assert keyword_list == expected
	content.delete

