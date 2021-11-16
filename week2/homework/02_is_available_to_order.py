shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!

    menus.sort()
    orders.sort()

    print(menus)
    print(orders)

    for order in orders:    #[만두, 오뎅, 콜라]
        if not is_existing_target_number_binary(order,menus):   #하나라도 존재안한다면
            return False

    return True



def is_existing_target_number_binary(target, array):
    current_min = 0                 #0
    current_max = len(array) - 1    #15
    current_guess = (current_min + current_max) // 2    #7

    while current_min <= current_max:           #0<=15

        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        current_guess = (current_min + current_max) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)