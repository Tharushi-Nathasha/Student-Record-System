# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230577
# Date : 2023 / 12/ 07

from graphics import *


# (Part 1 - B.Validation)

def check_range(credits):
    valid_ranges = [0, 20, 40, 60, 80, 100, 120]

    if isinstance(credits, int):
        if credits in valid_ranges:
            pass
        else:
            print("Out of range")
    else:
        print("Integer required")


def check_credits(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        print('Total incorrect')


# Calculating the progression
def calculate_progression(pass_credits, fail_credits):
    if pass_credits == 120:
        return 'Progress'
    elif pass_credits == 100:
        return 'Progress (module trailer)'
    elif fail_credits >= 80:
        return 'Exclude'
    else:
        return 'Module retriever'


# Displaying the histogram ( Part 1 - D)
def display_histogram(progress_counts, trailing_counts, retriever_counts, exclude_counts):
    win = GraphWin("Progression Histogram", 500, 300)
    win.setBackground("white")

    bar_width = 80
    bar_spacing = 20
    # Displaying the progress bar
    progress_bar = Rectangle(Point(50, 250), Point(50 + bar_width, 250 - progress_counts * 10))
    progress_bar.setFill("green")
    progress_label = Text(Point(50 + bar_width / 2, 270), f"Progress: {progress_counts}")
    progress_bar.draw(win)
    progress_label.draw(win)
    # Displaying the trailing bar
    trailing_bar = Rectangle(Point(150, 250), Point(150 + bar_width, 250 - trailing_counts * 10))
    trailing_bar.setFill("yellow")
    trailing_label = Text(Point(150 + bar_width / 2, 270), f"Trailing: {trailing_counts}")
    trailing_bar.draw(win)
    trailing_label.draw(win)
    # Displaying the retriever bar
    retriever_bar = Rectangle(Point(250, 250), Point(250 + bar_width, 250 - retriever_counts * 10))
    retriever_bar.setFill("pink")
    retriever_label = Text(Point(250 + bar_width / 2, 270), f"Retriever: {retriever_counts}")
    retriever_bar.draw(win)
    retriever_label.draw(win)
    # Displaying the exclude bar
    exclude_bar = Rectangle(Point(350, 250), Point(350 + bar_width, 250 - exclude_counts * 10))
    exclude_bar.setFill("red")
    exclude_label = Text(Point(350 + bar_width / 2, 270), f"Exclude: {exclude_counts}")
    exclude_bar.draw(win)
    exclude_label.draw(win)

    total_label = Text(Point(200, 290),
                       f"Total Students: {progress_counts + trailing_counts + retriever_counts + exclude_counts}")
    total_label.draw(win)

    win.getMouse()
    win.close()


# (Part 2 - List (extension)

# Displaying the progress data
def print_data(progress_data, print_progress=True):
    if print_progress:
        print("Part 2:")
        for data in progress_data:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")


# Saving to files
def save_to_file(progress_data, filename):
    with open(filename, 'w') as file:
        file.write("Part 3:\n")  # Add Part 3 as the first line in the file
        for data in progress_data:
            file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")


# Reading from files
def read_from_file(filename):
    progress_data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(' - ')
                if len(data) == 4:
                    credits = [int(x) for x in data[1].split(', ')]
                    progress_data.append([data[0]] + credits)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return progress_data



# Clarification of the user
def main():
    position = input("Are you a student or staff member? (student/staff): ").lower()

    # Code if the user is a student ( Part 1 - A. Outcomes )
    if position == 'student':
        pass_credits = int(input("Enter pass credits: "))
        check_range(pass_credits)

        defer_credits = int(input("Enter defer credits: "))
        check_range(defer_credits)

        fail_credits = int(input("Enter fail credits: "))
        check_range(fail_credits)

        check_credits(pass_credits, defer_credits, fail_credits)
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            pass
        else:
            progression_outcome = calculate_progression(pass_credits, fail_credits)
            print(f"Progression outcome: {progression_outcome}")

            if progression_outcome == 'Progress':
                progress_count = 1
                trailing_count = retriever_count = exclude_count = 0
            elif progression_outcome == 'Progress (module trailer)':
                trailing_count = 1
                progress_count = retriever_count = exclude_count = 0
            elif progression_outcome == 'Module retriever':
                retriever_count = 1
                progress_count = trailing_count = exclude_count = 0
            elif progression_outcome == 'Exclude':
                exclude_count = 1
                progress_count = trailing_count = retriever_count = 0

            progress_data = [[progression_outcome, pass_credits, defer_credits, fail_credits]]

    # Code if the user is a staff member ( Part 1 - C )
    elif position == 'staff':
        progress_count = trailing_count = retriever_count = exclude_count = 0
        progress_data = []

        while True:
            try:
                pass_credits = int(input("Enter pass credits: "))
                check_range(pass_credits)

                defer_credits = int(input("Enter defer credits: "))
                check_range(defer_credits)

                fail_credits = int(input("Enter fail credits: "))
                check_range(fail_credits)

                check_credits(pass_credits, defer_credits, fail_credits)
                total_credits = pass_credits + defer_credits + fail_credits

                if total_credits != 120:
                    pass
                else:
                    progression_outcome = calculate_progression(pass_credits, fail_credits)

                    print(f"Progression outcome: {progression_outcome}")

                    if progression_outcome == 'Progress':
                        progress_count += 1
                    elif progression_outcome == 'Progress (module trailer)':
                        trailing_count += 1
                    elif progression_outcome == 'Module retriever':
                        retriever_count += 1
                    elif progression_outcome == 'Exclude':
                        exclude_count += 1

                    progress_data.append([progression_outcome, pass_credits, defer_credits, fail_credits])

                    # Part 1 - C Multiple outcomes to a staff member
                    user_input = input("Would you like to enter another set of data? (y/q): ")
                    if user_input.lower() != 'y':
                        break

            except ValueError:
                print("Integer required")

        # Displaying the histogram for the staff member ( Part 1 - D )
        display_histogram(progress_count, trailing_count, retriever_count, exclude_count)
        print_data(progress_data)

        # Part 3 - Text file extension
        filename = input("Enter a filename to save data: ")
        save_to_file(progress_data, filename)

        stored_data = read_from_file(filename)
        if stored_data:
            print("Part 3:")
            print_data(stored_data, print_progress=False)  # Do not print "Part 2:" when reading from file


if __name__ == "__main__":
    main()
