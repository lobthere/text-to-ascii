#From a lobster

def from_txt_to_ascii(file_name, new_file_name):

    f = open(file_name, 'r')
    data = f.read()
    f.closed

    ascii_text = []
    for character in data:
        ascii_text.append(ord(character))

    ascii_text = str(ascii_text)

    characters = ",[]"
    for x in range(len(characters)):
        ascii_text = ascii_text.replace(characters[x],"")

    new_file = open(new_file_name, "x")
    new_file.write(ascii_text)
    new_file.close