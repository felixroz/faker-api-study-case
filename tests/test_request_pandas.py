from faker.extract.request import request_data_as_df
import pandas as pd
from pandas.testing import assert_frame_equal
import unittest


class TestFakerRequestPandas(unittest.TestCase):
    def request_10_should_request_10(self):
        # arrange
        df = request_data_as_df(10)

        # act
        expected_rows = 10
        rows_requested = df.count()[0]

        # assert
        assert_frame_equal(expected_rows,rows_requested)

