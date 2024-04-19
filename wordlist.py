def generate_numbers_with_prefix(prefix, start, end):
    with open('pass.txt', 'w') as file:
        for num in range(start, end + 1):
            formatted_num = f"{prefix}{num:05}"
            file.write(formatted_num + '\n')

generate_numbers_with_prefix("air", 0,99999)


#"Please Check README.md before Editing"