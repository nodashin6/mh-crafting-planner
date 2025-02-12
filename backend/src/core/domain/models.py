from pydantic import BaseModel, UUID4


class BaseEntity(BaseModel):
    pass


class UuidEntity(BaseEntity):
    id: UUID4


class NamedEntity(UuidEntity):
    name: str


class Item(NamedEntity):
    leadtime: int
    price: int


class Mixer(UuidEntity):
    max_capacity: int
    changeover_hours: int


class Precursor(UuidEntity):
    item: Item


class Product(UuidEntity):
    item: Item


class Craft(UuidEntity):
    required_hours: int
    yield_: float
    product: Product
    precursors: list[Precursor]


class Player(NamedEntity):
    name: str


class Savedata(UuidEntity):
    player: Player
    gold: int
    current_day: int
    current_hour: int


class Belonging(UuidEntity):
    savedata: Savedata
    item: Item
    quantity: int


class Facility(NamedEntity):
    savedata: Savedata
    mixser: Mixer


class Schedule(UuidEntity):
    savedata: Savedata
    craft: Craft
    mixser: Mixer
    quantity: int
    start_day: int
    start_hour: int
    end_day: int
    end_hour: int
    has_completed: bool


class Order(UuidEntity):
    savedata: Savedata
    product: Product
    quantity: int
    due_day: int


class Message(UuidEntity):
    savedata: Savedata
    message: str
    day: int
    hour: int
