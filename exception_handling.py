file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        wombat_text = file_in.read()
except FileNotFoundError as err:
    # 1. report error
    # 2. log error (same as #1??)
    # 3. use alternate value
    # 4. exit program gracefully
    print(err)

nums = [0, 800, 0, 80, 1000, 32, [1,2,3], 255, 0, 400, 5, "ABC",  5000]
try:
    print(nums[22])
except IndexError as err:
    print(err)

for num in nums:
    try:
        result = 9999 / num
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    else:
        print("result: {}".format(result))


print("ALL DONE")


