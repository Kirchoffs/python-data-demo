import unittest
import pandas as pd

# SQL:
# SELECT FirstName, LastName, City, State 
# FROM Person LEFT JOIN address 
# ON Person.PersonId = Address.PersonId;
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined = person.merge(address, on = 'personId', how = 'left')
    columns = ['firstName', 'lastName', 'city', 'state']
    combined = combined[columns]
    return combined

class SqlPandaTest(unittest.TestCase):
    def test_combine_two_tables(self):
        person = pd.DataFrame({
            'personId': [1, 2, 3],
            'firstName': ['Ben', 'Tom', 'John'],
            'lastName': ['Walker', 'Robertson', 'Smith']
        })
        
        address = pd.DataFrame({
            'personId': [1, 2],
            'city': ['New York', 'San Francisco'],
            'state': ['NY', 'CA']
        })
        
        res = combine_two_tables(person, address)
        
        print(res)
        self.assertEqual(res.shape, (3, 4))
        self.assertEqual(res.iloc[0]['firstName'], 'Ben')
        self.assertEqual(res.iloc[0]['lastName'], 'Walker')
        self.assertEqual(res.iloc[0]['city'], 'New York')
        self.assertEqual(res.iloc[0]['state'], 'NY')

if __name__ == '__main__':
    unittest.main()
    