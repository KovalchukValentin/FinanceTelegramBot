import sqlite3


class Item:
    def __init__(self, id_):
        self.id_ = id_

    def isNew(self):
        return self.id_ is None

    def __str__(self):
        return f"Item(id={self.id_})"


class GroupItem(Item):
    def __init__(self, id_: int, name: str):
        super(GroupItem, self).__init__(id_=id_)
        self.name = name

    def __str__(self):
        return f"GroupItem(id={self.id_}, name='{self.name}')"


class BindingItem(Item):
    def __init__(self, id_: int, name: str, group: GroupItem):
        super(BindingItem, self).__init__(id_=id_)
        self.name = name
        self.group = group

    def __str__(self):
        return f"BindingItem(id={self.id_}, name='{self.name}', group_id={self.group})"


class TransactionItem(Item):
    def __init__(self, id_: int, group: GroupItem, name: str, description: str, amount: int, time: int):
        super(TransactionItem, self).__init__(id_=id_)
        self.group = group
        self.name = name
        self.description = description
        self.amount = amount
        self.time = time

    def __str__(self):
        return f"TransactionItem(id={self.id_}, group={self.group}, name='{self.name}', " \
               f"description='{self.description}', amount={self.amount}, time={self.time})"


class DatabaseManager:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS groups (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE
                    )
                ''')

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS binding (
                        id INTEGER PRIMARY KEY,
                        group_id INTEGER,
                        name TEXT UNIQUE,
                        FOREIGN KEY (group_id) REFERENCES groups(group_id)
                    )
                ''')

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    group_id INTEGER,
                    name TEXT,
                    description TEXT,
                    amount INTEGER,
                    time INTEGER,
                    FOREIGN KEY (group_id) REFERENCES groups(id)
                )
            ''')
        self.conn.commit()

    def insert_into_binding(self, name, group):
        query = 'INSERT INTO groups (group_id, name) VALUES (?, ?)'
        group_id = self.get_id_from_groups_where_group_name(group)
        if group_id is None:
            return
        self.cursor.execute(query, (group_id, name))
        self.conn.commit()

    def insert_into_binding_item(self, binding: BindingItem):
        query = 'INSERT INTO groups (group_id, name) VALUES (?, ?)'
        group_id = self.get_id_from_groups_where_group_name(binding.group.name)
        if group_id is None:
            return
        self.cursor.execute(query, (group_id, binding.name,))
        self.conn.commit()

    def insert_into_groups(self, name):
        query = 'INSERT INTO groups (name) VALUES (?)'
        self.cursor.execute(query, (name,))
        self.conn.commit()

    def insert_into_groups_item(self, group: GroupItem):
        query = 'INSERT INTO groups (name) VALUES (?)'
        self.cursor.execute(query, (group.name,))
        self.conn.commit()

    def insert_into_transactions(self, group, name, description, amount, time):
        query = 'INSERT INTO groups (group_id, name, description, amount, time) VALUES (?, ?, ?, ?, ?)'
        group_id = self.get_id_from_groups_where_group_name(group)
        if group_id is None:
            return
        self.cursor.execute(query, (group_id, name, description, amount, time))
        self.conn.commit()

    def insert_into_transactions_item(self, transaction: TransactionItem):
        query = 'INSERT INTO groups (group_id, name, description, amount, time) VALUES (?, ?, ?, ?, ?)'
        group_id = self.get_id_from_groups_where_group_name(transaction.group.name)
        if group_id is None:
            return
        self.cursor.execute(query, (group_id if transaction.group.id_ is None else transaction.group.id_,
                                    transaction.name, transaction.description, transaction.amount, transaction.time))
        self.conn.commit()

    def get_records_with_group_names(self):
        query = '''
            SELECT transactions.*, groups.name
            FROM transactions
            JOIN groups ON transactions.group_id = groups.id
        '''
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def get_id_from_groups_where_group_name(self, name):
        query = f'''
                   SELECT *
                   FROM groups
                   WHERE name = {name}
               '''
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records[0][0]

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    table_manager = DatabaseManager()
    table_manager.create_tables()
    table_manager.close_connection()