from abc import ABS, abstractmethod

class Connector(ABS):
    @abstractmethod
    def get_count(token):
        pass

    @abstractmethod
    def count_request():
        pass

class RedisConnector(Connector):
    def __init__(self, address, port):
        pass
        # A lógica da conexão ao banco Redis

    def get_count(token):
        pass

        # A lógica de acesso ao banco Redis

    def count_request(token):
        pass

        # A lógica de acesso ao banco Redis

class SqlConnector(Connector):
    def __init__(self, address, port):
        pass
        # A lógica da conexão ao banco SQL

    def get_count(token):
        pass
        # A lógica de acesso ao banco SQL

    def count_request(token):
        pass
        # A lógica de acesso ao banco SQL