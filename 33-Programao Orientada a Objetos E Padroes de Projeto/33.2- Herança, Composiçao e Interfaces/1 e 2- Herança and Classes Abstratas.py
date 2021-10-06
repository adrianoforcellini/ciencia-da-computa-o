import json
from csv import DictWriter
from abc import ABC, abstractmethod


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file + '.json'
        self.export_csv = export_file + '.csv'

    def build(self):
        """ Aqui colocamos a lógica para a entidade 'se criar',
        ou seja, criar um relatório imprimível. Por simplicidade,
        vamos omitir essa lógica nos exemplos! """
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    @abstractmethod
    def serialize(self):
        raise NotImplementedError            


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file, 'w') as file:
            json.dump(self.build(), file)



class SalesReportCSV(SalesReport):
    def serialize(self):
        with open(self.export_csv, 'w') as file:
            headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
            csv_writer = DictWriter(file, headers)
            csv_writer.writeheader()
            for item in self.build():
                csv_writer.writerow(item)


relatorio_de_vendas = SalesReportJSON('meu_relatorio')
relatorio_de_vendas.serialize()

relatorio_csv= SalesReportCSV('relatorio-csv')
relatorio_csv.serialize()