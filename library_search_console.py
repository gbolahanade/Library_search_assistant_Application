from library_search_common import read_csv, get_location, get_subject_names


def search_by_subject(subjects_data, classmarks_data):
    subject_name = input("Enter the subject name or part-name: ")
    matches = []

    for row in subjects_data:
        if subject_name.lower() in row[0].lower():
            classmark = row[1]
            location = get_location(classmark, classmarks_data)
            matches.append((classmark, location, subject_name))

    return matches


def search_by_classmark(subjects_data, classmarks_data):
    classmark = input("Enter the classmark: ")
    location = get_location(classmark, classmarks_data)
    subject_names = get_subject_names(classmark, subjects_data)
    return [(classmark, location, subject_names)]


def search_by_location(classmarks_data, subjects_data):
    location = input(
        "Enter the location (Ground Floor, Middle Floor, Top Floor Back Left, Top Floor Back Right, Top Floor Front "
        "Left, Top Floor Front Right): ")
    matches = []

    for row in classmarks_data:
        if location.lower() == row[1].lower():
            classmark = row[0]
            subject_names = get_subject_names(classmark, subjects_data)
            matches.append((classmark, location, subject_names))

    return matches


def main():
    subjects_data = read_csv("subjects.csv")
    classmarks_data = read_csv("locations.csv")

    while True:
        print("\nOptions:")
        print("1. Search by subject name/part-name")
        print("2. Search by classmark")
        print("3. Search by location")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            matches = search_by_subject(subjects_data, classmarks_data)
        elif choice == '2':
            matches = search_by_classmark(subjects_data, classmarks_data)
        elif choice == '3':
            matches = search_by_location(classmarks_data, subjects_data)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        if not matches:
            print("No matches found.")
        else:
            for match in matches:
                print(f"Classmark: {match[0]}, Location: {match[1]}, Subject Name(s): {', '.join(match[2])}")


if __name__ == "__main__":
    main()
