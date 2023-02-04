file_name = "fileprocessor.input"

with open(file_name, "r") as file:
    lines = file.readlines()

print("Printing out User Data:")
for line in lines:
    if not line.startswith("#"):
        elements = line.strip().split(":")
        print(f"The user {elements[0]} has a password of {elements[1]} and has userid {elements[2]} and groupid {elements[3]}")
    else:
        print(f"{line.strip()} is skipped because it starts with a hashtag (is commented out)")
print("End of User Data")

