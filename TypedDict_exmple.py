from typing import TypedDict

class MyState(TypedDict):
    name: str
    age: int
def greet_user(state: MyState):
    print(f"Hello, {state['name']}! You are {state['age']}years old.")
data: MyState = {
    "name": "neha",
    "age": 18
}
greet_user(data)
