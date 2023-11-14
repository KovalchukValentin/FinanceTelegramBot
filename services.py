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

