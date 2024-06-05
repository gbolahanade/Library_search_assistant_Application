# library_search_gui.py

import tkinter as tk
from library_search_common import read_csv, get_location, get_subject_names


class LibrarySearchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Search")

        self.subjects_data = read_csv("subjects.csv")
        self.classmarks_data = read_csv("locations.csv")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Options:")
        self.label.pack()

        self.choice_var = tk.StringVar()
        self.choice_var.set("1")

        self.radio_button_1 = tk.Radiobutton(self.root, text="Search by subject name/part-name",
                                             variable=self.choice_var, value="1")
        self.radio_button_2 = tk.Radiobutton(self.root, text="Search by classmark", variable=self.choice_var, value="2")
        self.radio_button_3 = tk.Radiobutton(self.root, text="Search by location", variable=self.choice_var, value="3")
        self.radio_button_4 = tk.Radiobutton(self.root, text="Exit", variable=self.choice_var, value="4")

        self.radio_button_1.pack()
        self.radio_button_2.pack()
        self.radio_button_3.pack()
        self.radio_button_4.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.handle_submit)
        self.submit_button.pack()

        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

    def handle_submit(self):
        choice = self.choice_var.get()

        if choice == '1':
            matches = self.search_by_subject()
        elif choice == '2':
            matches = self.search_by_classmark()
        elif choice == '3':
            matches = self.search_by_location()
        elif choice == '4':
            self.root.destroy()
            return
        else:
            matches = []

        output = ""
        if not matches:
            output = "No matches found."
        else:
            for match in matches:
                output += f"Classmark: {match[0]}, Location: {match[1]}, Subject Name(s): {', '.join(match[2])}\n"

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output)

    def search_by_subject(self):
        subject_name = self.input_entry.get()
        matches = []

        for row in self.subjects_data:
            if subject_name.lower() in row[0].lower():
                classmark = row[1]
                location = get_location(classmark, self.classmarks_data)
                matches.append((classmark, location, subject_name))

        return matches

    def search_by_classmark(self):
        classmark = self.input_entry.get()
        location = get_location(classmark, self.classmarks_data)
        subject_names = get_subject_names(classmark, self.subjects_data)
        return [(classmark, location, subject_names)]

    def search_by_location(self):
        location = self.input_entry.get()
        matches = []

        for row in self.classmarks_data:
            if location.lower() == row[1].lower():
                classmark = row[0]
                subject_names = get_subject_names(classmark, self.subjects_data)
                matches.append((classmark, location, subject_names))

        return matches


if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySearchGUI(root)
    root.mainloop()
