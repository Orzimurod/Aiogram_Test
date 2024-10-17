from aiogram.fsm.state import State, StatesGroup


class Shop(StatesGroup):
    product_type = State()
    event_type = State()
    event = State()
    for_who = State()
    product = State()
    order_item = State()
    order = State