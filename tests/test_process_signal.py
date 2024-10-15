"""This module contains tests to test the signal processing utilities."""

import unittest
import logging
from scipy.io import wavfile
import numpy as np
from signal_processing_utilities import process_signal

logging.basicConfig(level=logging.DEBUG)


class TestProcessSignal(unittest.TestCase):
    """This class is used to define tests to test the process signal module.

    Args:
        unittest (module): This is the module that enables unittests.
    """

    def setUp(self):
        self.file_path = "test_data/0ab237b7-fb12-4687-afed-8d1e2070d621.wav"

    def tearDown(self):
        pass

    def test01_compare_for_equality(self):
        logging.info(
            "test01: This is a test to ensure that the byte strings are of "
            + "equal length. The lengths are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = b"010101010001"
        byte_string2 = b"100101011001101"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test02_compare_for_equality(self):
        logging.info(
            "test02: This is a test to ensure that the byte strings are of "
            + "equal value. The values are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = b"010101010001"
        byte_string2 = b"100101011001"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test03_compare_for_equality(self):
        logging.info(
            "test03: This is a test to ensure that the byte strings are of "
            + "equal type. The types are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = "010101010001"
        byte_string2 = b"100101011001"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test04_process_neural_spikes(self):
        logging.info(
            "test04: This is a test to ensure that the spikes of the "
            + "raw neural data may be processed & that the data may be "
            + "processed in a timely manner. "
        )

        _, data = wavfile.read(self.file_path)
        spike_train_time_index_list = detect_neural_spikes(
            neural_data=data, single_spike_detection=False, real_time=True
        )
        self.assertEqual(type(spike_train_time_index_list), np.ndarray)
