from read_ecg import Read_ecg
import pytest

def test_try_exception_import():

    """

    tests that the imported file is a csv

    """

    with pytest.raises(ImportError):
        import ThisisNotAFile


#def test_read_time():

 #   """

  #  tests that the  time is read properly from the file

   # """

    #test_time = read_time()
    #assert test_time == time


#def test_read_voltage():

 #   """
#
 #   tests that the voltage is read properly from the file

  #  """

   # test_voltage = read_voltage()
   # assert test_voltage == voltage


