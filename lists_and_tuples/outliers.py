outliers = [4, 5, 104, 105, 110, 120, 130, 130, 150,
            160, 170, 183, 185, 187, 188, 181, 350, 360]

# Manual deletion, Error prone
# del outliers[0:2]
# print(outliers)
# del outliers[14:]
# print(outliers)

min_valid = 100
max_valid = 200

# The code below causes errors
for index, value in enumerate(outliers):
    if(value < min_valid) or (value > max_valid):
        del outliers[index]

print(outliers)

# outlier in both sides
# outliers = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#             160, 170, 183, 185, 187, 188, 181, 350, 360]
# outliers on left side
# outliers = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#             160, 170, 183, 185, 187, 188, 181]
# outliers on right side
# outliers = [104, 105, 110, 120, 130, 130, 150,
#             160, 170, 183, 185, 187, 188, 181, 350, 360]
# No outliers
# outliers = [104, 105, 110, 120, 130, 130, 150,
#             160, 170, 183, 185, 187, 188, 181]
# Only outliers
# outliers = [4, 5, 14, 15, 11, 12, 13, 1130, 1150,
#             1160, 1170, 1183, 1185, 1187, 1188, 1181, 1350, 1360]
# Empty list
# outliers = []


# process low values in the list
stop = 0
for index, value in enumerate(outliers):
    if value >= min_valid:
        stop = index
        break
print(stop)
del outliers[:stop]
print(outliers)

# process high values in the list
start = 0
for index in range(len(outliers) - 1, -1, -1):
    if outliers[index] <= max_valid:
        start = index + 1  # The if checks the index of the last item to keep
# so we need to add 1 to get the first to delete
        break

print(start)
del outliers[start:]
print(outliers)
