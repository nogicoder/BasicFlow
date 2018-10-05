def median(number_list):
    number_list = sorted(number_list)
    for i in range(len(number_list)):
      if len(number_list) % 2 != 0:
        index = int(len(number_list)/2)
        return number_list[index]
      elif len(number_list) % 2 == 0:
        index1 = int(len(number_list)/2 - 1)
        index2 = int(len(number_list)/2)
        med = (number_list[index1] + number_list[index2])/2
        return med


print(median([4,5,5,4]))
