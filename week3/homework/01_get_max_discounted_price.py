shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!

    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    #print(prices)
    #print(coupons)

    coupons_index = 0
    princes_index = 0
    sum =0

    #for 문 보다는 while문 추천 : 둘중 길이 끝날때 까지만 해야되므로
    for coupon in coupons:
        sum += int((1-coupon/100)*prices[princes_index])
        #print(sum)
        coupons_index += 1
        princes_index += 1

        if coupons_index > (len(prices)-1): #가격 계산이 다끝났다면 탈출
            break

    while princes_index<len(prices):     #2 < 3
        sum += prices[princes_index]
        #print("prices[princes_index]",prices[princes_index])
        princes_index +=1

    return sum


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))