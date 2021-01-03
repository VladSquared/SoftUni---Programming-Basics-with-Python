price_ratings = list(map(int, input().split()))
entry_point = int(input())
entry_point_value = price_ratings[entry_point]
type_of_items = input()
type_of_price_ratings = input()

left_list = price_ratings[:entry_point]
right_list = price_ratings[entry_point + 1:]

if type_of_items == 'cheap':
    left_list = [x for x in left_list if x < entry_point_value]
    right_list = [x for x in right_list if x < entry_point_value]
elif type_of_items == 'expensive':
    left_list = [x for x in left_list if x >= entry_point_value]
    right_list = [x for x in right_list if x >= entry_point_value]

if type_of_price_ratings == 'positive':
    left_list = [x for x in left_list if x > 0]
    right_list = [x for x in right_list if x > 0]
elif type_of_price_ratings == 'negative':
    left_list = [x for x in left_list if x < 0]
    right_list = [x for x in right_list if x < 0]

if sum(left_list) >= sum(right_list):
    print(f'Left - {sum(left_list)}')
elif sum(right_list) > sum(left_list):
    print(f'Right - {sum(right_list)}')
