sample_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
months = ("jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sept", "oct", "nov", "dec")
message = "Your limitation, it's only your imagination."

# slicing [start:stop:step] , slice(start, stop, step)
# start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided., 0
# stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element). length-1
# step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided. 1


slice_ob = slice(1, 8, 3)
print(sample_list[slice_ob])


