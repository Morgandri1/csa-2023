#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#
def extract_alphanumeric_from_gif(file_path):
    alphanumeric_data = []

    # Open the GIF file in binary mode
    with open(file_path, 'rb') as file:
        # Read the entire content of the file
        content = file.read()

        # Iterate over each byte in the content
        for byte in content:
            char = chr(byte)
            # Check if the character is alphanumeric
            if char.isalnum():
                alphanumeric_data.append(char)

    # Join the alphanumeric characters into a string
    return ''.join(alphanumeric_data)

# Replace 'path_to_your_gif.gif' with the path to your GIF file
alphanumeric_data = extract_alphanumeric_from_gif('/tmp/destroymoonbase.gif')
print(alphanumeric_data)
