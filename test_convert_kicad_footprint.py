''' 
Dependancy: pytest-mock
Matthew Oppenheim Sep 2022'''
import convert_kicad_footprint
from convert_kicad_footprint import *
import logging
import pytest
from unittest.mock import patch, mock_open

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def test_apply_regex_to_file():
    # use open_mock to mock opening files
    open_mock = mock_open()
    with patch('convert_kicad_footprint.open', open_mock, create=True):
        apply_regex_to_file("input_filepath", "output_filepath")
    assert open_mock.call_count == 2
    open_mock.assert_any_call("input_filepath", 'r')
    open_mock.assert_any_call("output_filepath", 'w')


@pytest.mark.parametrize('test_input, expected',
  [('aa(stroke (width 0.05) (type solid))bb', 'aa(width 0.05)bb'), 
  (' (tstamp 12345678-abcd-0123-0123-0123456789ab)', ''),\
    ('(stroke (width 0.05) (type solid)) (layer "F.CrtYd") (tstamp 34a82477-a37c-4c79-a51c-b7fdc28985db))',
    '(width 0.05) (layer "F.CrtYd"))'),
    ('aa(version 20220427)bb', 'aa(version 20100101)bb')])
def test_apply_regex_to_line(test_input, expected):
  assert apply_regex_to_line(test_input)== expected
        

def test_check_file_exists(monkeypatch):
  # monkeypatch os.path.exists to be True
  monkeypatch.setattr(os.path, 'exists', lambda _:True)
  assert check_file_exists('bogus_filepath') == True


def test_create_output_directory(monkeypatch):
  monkeypatch.setattr(os.path, 'exists', lambda _:True)
  assert create_output_directory('aardvark/sibling') == 'aardvark/sibling/kicad_converted'

  
def test_create_output_filepath(mocker):
  mocker.patch('convert_kicad_footprint.create_output_directory', return_value = 'file_dir/kicad_converted') 
  assert create_output_filepath('file_dir/file_name') == 'file_dir/kicad_converted/file_name'


def test_exit_code(capsys, caplog):
  with pytest.raises(SystemExit):
    exit_code('help')
  # capsys fixture capture print statement outputs
  out, err = capsys.readouterr()
  # no print output as using logging
  assert out == ""
  # caplog fixture captures logging output
  assert "exiting" in caplog.text
  assert "help" in caplog.text


def test_filepath(monkeypatch):
  # Use monkeypatch to simulate run time arguments in sys.argv
  monkeypatch.setattr(sys, 'argv', ['prog_name', 'filepath'] )
  assert filepath(['prog_name', 'filepath']) == 'filepath'




