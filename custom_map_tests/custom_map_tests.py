import os
import unittest
import json
from datetime import date
from pathlib import Path
from citrus.cli import transform

test_dir_path = os.path.abspath(os.path.dirname(__file__))

"""
0 = Boynton Beach City Library Archives
1 = Miami Shores Village Archives at Brockway Memorial Library
2 = Broward College Archives & Special Collections
3 = City of Coral Gables
4 = Florida Atlantic University
5 = Florida Gulf Coast University Library
6 = Miami Design Preservation League, Closeup Productions
7 = Florida International University Libraries
8 = Florida State College at Jacksonville
9 = First Baptist Church of Tallahassee
10 = Godby High School, Tallahassee, Florida
11 = Havana History & Heritage Society, Havana, Florida
12 = Leon High School, Tallahassee, Florida
13 = Florida State University Libraries
14 = Greater North Miami Historical Society
15 = Florida International University Libraries
16 = Miami-Dade Public Library System
17 = University of Miami Libraries
18 = University of South Florida Libraries
19 = Vaclav Havel Library Foundation
"""    


class CustomMapTestCase(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(test_dir_path, 'transformation_test_data/transformation_verification.json')) as fp:
            self.data = [json.loads(line) for line in fp]
        self.config = {'ssdn': {'InFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                                'OutFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                                'Provider': 'Sunshine State Digital Network',
                                'CustomMapPath': os.path.split(test_dir_path)[0]}}
                                                            
    #def tearDown(self):
    #    os.remove(Path(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')))
    
    def test_fsu_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'Florida State University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'fsu', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[13])
        #test_data = json.load(os.path)
        

if __name__ == '__main__':
    unittest.main()
