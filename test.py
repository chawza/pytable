from pytable import Table
from pydantic import BaseModel, Field
from unittest import TestCase, main
from typing import Optional

class Model(BaseModel):
    title: str = Field(title='Title')
    notes: Optional[str]

class TestTableCase(TestCase):

    def test_csv(self):

        table = Table(Model, initial=[Model(title='Test1', notes='Note 1'), Model(title='Test2', notes=None)])
        csv = table.to_csv()

        from csv import reader
        csv_reader = reader(csv.getvalue().strip().split('\n'))

        rows = list(csv_reader) 

        self.assertEqual(len(rows), 3, rows)

        self.assertEqual(rows[0], ['Title', 'notes'])

if __name__ == '__main__':
    main()