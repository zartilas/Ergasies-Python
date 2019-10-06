def load_paragraph():
    with open('Paragraph.txt', 'r') as file:
        paragraph = file.read()
        return paragraph


def save_to_file(pl):
    file = open("Plithos.txt", "w", "utf-8")
    file.write("Number of non-printable characters: ", pl)
    file.close()
