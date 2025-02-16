from typing import List
from uuid import UUID

class BaseEntity:
    def __init__(self, id: UUID):
        self.id = id

class NamedEntity(BaseEntity):
    def __init__(self, id: UUID, name: str):
        super().__init__(id)
        self.name = name

class Item(NamedEntity):
    def __init__(self, id: UUID, name: str, leadtime: int, price: int):
        super().__init__(id, name)
        self.leadtime = leadtime
        self.price = price

class Mixer(BaseEntity):
    def __init__(self, id: UUID, max_capacity: int, changeover_hours: int):
        super().__init__(id)
        self.max_capacity = max_capacity
        self.changeover_hours = changeover_hours

class Precursor(BaseEntity):
    def __init__(self, id: UUID, item: Item):
        super().__init__(id)
        self.item = item

class Product(BaseEntity):
    def __init__(self, id: UUID, item: Item):
        super().__init__(id)
        self.item = item

class Craft(BaseEntity):
    def __init__(self, id: UUID, required_hours: int, yield_: float, product: Product, precursors: List[Precursor]):
        super().__init__(id)
        self.required_hours = required_hours
        self.yield_ = yield_
        self.product = product
        self.precursors = precursors

class Player(NamedEntity):
    def __init__(self, id: UUID, name: str):
        super().__init__(id, name)

class Savedata(BaseEntity):
    def __init__(self, id: UUID, player: Player, gold: int, current_day: int, current_hour: int):
        super().__init__(id)
        self.player = player
        self.gold = gold
        self.current_day = current_day
        self.current_hour = current_hour

class Belonging(BaseEntity):
    def __init__(self, id: UUID, savedata: Savedata, item: Item, quantity: int):
        super().__init__(id)
        self.savedata = savedata
        self.item = item
        self.quantity = quantity

class Facility(NamedEntity):
    def __init__(self, id: UUID, name: str, savedata: Savedata, mixer: Mixer):
        super().__init__(id, name)
        self.savedata = savedata
        self.mixer = mixer

class Schedule(BaseEntity):
    def __init__(self, id: UUID, savedata: Savedata, craft: Craft, mixer: Mixer, quantity: int, start_day: int, start_hour: int, end_day: int, end_hour: int, has_completed: bool):
        super().__init__(id)
        self.savedata = savedata
        self.craft = craft
        self.mixer = mixer
        self.quantity = quantity
        self.start_day = start_day
        self.start_hour = start_hour
        self.end_day = end_day
        self.end_hour = end_hour
        self.has_completed = has_completed

class Order(BaseEntity):
    def __init__(self, id: UUID, savedata: Savedata, product: Product, quantity: int, due_day: int):
        super().__init__(id)
        self.savedata = savedata
        self.product = product
        self.quantity = quantity
        self.due_day = due_day

class Message(BaseEntity):
    def __init__(self, id: UUID, savedata: Savedata, message: str, day: int, hour: int):
        super().__init__(id)
        self.savedata = savedata
        self.message = message
        self.day = day
        self.hour = hour