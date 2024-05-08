# Define a variable milliseconds and ask the user to enter a milliseconds value. Then, convert
# and print it in an “hours, minutes, seconds, milliseconds” format:

# Get milliseconds from user to do the operations.
milliseconds = int(input('Enter milliseconds: '))

# Return the remainder from the process of converting milliseconds into seconds.
ms = (milliseconds) % 1000

# Substract the remainded milliseconds (above) from the milliseconds variable and return the remainder from the process of converting it from seconds to minutes.
s = ((milliseconds - ms) // 1000) % 60

# Substract the remainded milliseconds and seconds (above) from the milliseconds variable and return the remainder from the process of converting it from minutes to hours.
m = ((milliseconds - (ms + (s * 1000))) // (1000 * 60)) % 60

# Substract the remainded milliseconds, seconds and minutes (above) from the milliseconds variable and return the conversion of it to hours.
h = ((milliseconds - (ms + (s * 1000) + (m * 60 * 1000 ))) // (1000 * 60 * 60))

# Print the result.
print(f'{milliseconds}ms ---> {h}h {m}m {s}s {ms}ms')