"""PR 与 diff 练习用的初始版本：一个简单购物车。"""


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def print_receipt(items):
    print("购物清单")
    for item in items:
        print(f'{item["name"]} x {item["quantity"]}')
    print(f"合计：{calculate_total(items):.2f} 元")


if __name__ == "__main__":
    cart = [
        {"name": "笔记本", "price": 12, "quantity": 2},
        {"name": "签字笔", "price": 3, "quantity": 3},
    ]
    print_receipt(cart)
