from pytable import Table
from pydantic import BaseModel, Field
from unittest import TestCase, main
from typing import Optional
from csv import reader

class Model(BaseModel):
    title: str = Field(title='Title')
    notes: Optional[str]

class TestTableCase(TestCase):

    def test_csv(self):
        table = Table(Model, initial=[Model(title='Test1', notes='Note 1'), Model(title='Test2', notes=None)])
        csv = table.to_csv()

        csv_reader = reader(csv.getvalue().strip().split('\n'))

        rows = list(csv_reader) 

        self.assertEqual(len(rows), 3, rows)

        self.assertEqual(rows[0], ['Title', 'notes'])

    def test_excel(self):
        table = Table(Model, initial=[Model(title='Test1', notes='Note 1'), Model(title='Test2', notes=None)])
        excel = table.to_excel_workbook()

        sheet = excel.worksheets[0]
        rows = list(sheet.iter_rows())
        
        self.assertEqual(len(rows), 3, rows)
        values = [cell.value for cell in rows[0]]
        self.assertEqual(values, ['Title', 'notes'])


if __name__ == '__main__':
    main()