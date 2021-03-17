def check_division(N):
	file_to_write = open(f'{N}.txt', 'w')
	count_numbers = 0
	number = 0 

	while count_numbers < N:
		digits_count = len(str(number))

		if number % digits_count == 0:
			count_numbers += 1
			file_to_write.write(f"{number} ")
		number += 1
	file_to_write.close()


check_division(28)
check_division(120)
check_division(500)
