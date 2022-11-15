import json
import os
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch, MagicMock

from manatus.cli import transform

test_dir_path = os.path.abspath(os.path.dirname(__file__))


def stand_up(self):
    """
    Open and load verification data
    init local test config
    """

    with open(os.path.join(test_dir_path, 'transformation_test_data/transformation_verification.json')) as fp:
        self.data = [json.loads(line) for line in fp]
    self.config = {'ssdn': {'InFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                            'OutFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                            'Provider': 'Sunshine State Digital Network',
                            'OutFilePrefix': 'SSDN_TMP',
                            'CustomMapPath': os.path.split(test_dir_path)[0]}}
    return self


def clean():
    """
    Remove docs built for tests
    """
    try:
        os.remove(Path(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')))
    except FileNotFoundError:
        pass


class FSUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fsu_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'Florida State University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'fsu', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[13])


class FBCTLHCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'fbctlh', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[9])


class LeonHighCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'leon', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[12])


class GodbyHighCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'godby', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[10])


class HavanaHHSCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'havana', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[11])


class FIUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fiu_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Florida International University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'fiu', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[7])


class BoyntonBeachCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Boynton Beach City Library Archives',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'boynton', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[0])


class BrockwayCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_brockway_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Miami Shores Village Archives at Brockway Memorial Library',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'brockway', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[1])


class CoralGablesCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_coral_gables_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'City of Coral Gables',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'coral_gables', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[3])


class MBVMCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_mbvm_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Miami Design Preservation League, Closeup Productions',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'mbvm', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[6])


class GNMHSCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_gnmhs_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Greater North Miami Historical Society',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'gnmhs', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[14])


class VaclavCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_vaclav_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Vaclav Havel Library Foundation',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'vhlf', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[19])


class UMCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_um_qdc_custom_map(self):
        transformation_info = {'Map': 'um_qdc_map',
                               'DataProvider': 'University of Miami Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNQDC'}
        transform(self.config, transformation_info, 'um', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[17])


class IR_FIUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_ir_fiu_dc_custom_map(self):
        transformation_info = {'Map': 'ssdn_dc_bepress_map',
                               'DataProvider': 'Florida International University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'BepressDC'}
        transform(self.config, transformation_info, 'ir_fiu', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[15])


class BrowardCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_broward_mods_custom_map(self):
        transformation_info = {'Map': 'ssdn_mods_map',
                               'DataProvider': 'Broward College Archives & Special Collections',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNPartnerMODSScenario'}
        transform(self.config, transformation_info, 'broward', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[2])


class FAUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fau_mods_custom_map(self):
        transformation_info = {'Map': 'ssdn_mods_map',
                               'DataProvider': 'Florida Atlantic University',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNPartnerMODSScenario'}
        transform(self.config, transformation_info, 'fau', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[4])


class FGCUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fgcu_mods_custom_map(self):
        transformation_info = {'Map': 'ssdn_mods_map',
                               'DataProvider': 'Florida Gulf Coast University Library',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNPartnerMODSScenario'}
        transform(self.config, transformation_info, 'fgcu', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[5])


class FSCJCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fscj_mods_custom_map(self):
        transformation_info = {'Map': 'ssdn_mods_map',
                               'DataProvider': 'Florida State College at Jacksonville',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNPartnerMODSScenario'}
        transform(self.config, transformation_info, 'fscj', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[8])


class InternetArchiveCustomMapTestCase(unittest.TestCase):
    class MockResponse(MagicMock):
        """
        Class for mocking out calls to requests.get
        """

        def __init__(self, *args, **kwargs):
            MagicMock.__init__(self, *args, **kwargs)
            with open(os.path.join(test_dir_path,
                                   'transformation_test_data/statelibraryandarchivesofflorida.json')) as state_lib_data:
                self.text = state_lib_data.read()

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    @patch('requests.get', side_effect=MockResponse)
    def test_state_library_custom_map(self, requests_mock):
        transformation_info = {'Map': 'dlis_ia_map',
                               'DataProvider': 'State Library and Archives of Florida',
                               'IntermediateProvider': None,
                               'Scenario': 'InternetArchive'}
        transform(self.config, transformation_info, 'statelibraryandarchivesofflorida', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[20])


class MDPLCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_mdpl_qdc_custom_map(self):
        transformation_info = {'Map': 'ssdn_qdc_map',
                               'DataProvider': 'Miami-Dade Public Library System',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNQDC'}
        transform(self.config, transformation_info, 'mdpl', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[16])


class USFCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_usf_dc_custom_map(self):
        transformation_info = {'Map': 'ssdn_dc_map',
                               'DataProvider': 'University of South Florida Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'usf', 'ssdn', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[18])


if __name__ == '__main__':
    unittest.main()
