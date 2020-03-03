from notebook import Note, Notebook

def note():
    """
    a function for testing class Note
    """
    note = Note("IT and BA", tags="Applied science")
    print(f"Cheking if note belongs to class Note using fuction " +
          f"isinstance: {isinstance(note, Note)}")
    print(f"Using built-in object method __dict__ get all atributes and their values of note object: {note.__dict__}")
    print(f"Atributes of note object: {dir(note)}")


def notebook():
    """
    a function for testing class Notebook
    """
    notebook = Notebook()
    print(f"Cheking if note belongs to class Note using fuction " +
          f"isinstance: {isinstance(notebook, Notebook)}")
    print(f"Using built-in object method __dict__ get all atributes and their values of note object: {notebook.__dict__}")
    print(f"Atributes of note object: {dir(notebook)}")


if __name__ == "__main__":
    note()
    print(2*"\n")
    notebook()