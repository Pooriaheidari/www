def sort_string(input_string):
    # لیست‌های جداگانه برای حروف، اعداد و سایر کاراکترها
    letters = []
    numbers = []
    specials = []
    
    # طبقه‌بندی کاراکترهای ورودی
    for char in input_string:
        if char.isalpha():         # اگر حرف است
            letters.append(char)
        elif char.isdigit():       # اگر عدد است
            numbers.append(char)
        else:                      # اگر کاراکتر خاص است
            specials.append(char)
    
    # مرتب‌سازی هر لیست به ترتیب حروف الفبا
    letters.sort(key=lambda c: (c.lower(), c.islower()))
    numbers.sort()
    specials.sort()
    
    # ترکیب لیست‌ها به ترتیب: حروف، اعداد، و سپس کاراکترهای خاص
    sorted_string = ''.join(specials + numbers + letters)
    
    return sorted_string

# گرفتن ورودی از کاربر
input_string = input("Please enter a string: ")
# تولید خروجی مرتب شده
output_string = sort_string(input_string)

# نمایش خروجی
print("Sorted output:", output_string)
