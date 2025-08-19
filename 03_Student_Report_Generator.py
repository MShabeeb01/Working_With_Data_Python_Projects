# Student Report Generator using "CSV"-"Comma-Separated Values"
import csv

# Step-1: Read student data and calculate averages:
def process_student_data(input_file, output_file):
    try:
        # Open input CSV file for reading
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []

            # Process each row (student record)
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])

                # Calculate average
                average = round((math + science + english) / 3, 2)

                # Determine pass/fail status
                status = "Pass" if average >= 60 else "Fail"

                # Append processed student data
                student_reports.append(
                    {
                        'Name': name,
                        'Math': math,
                        'Science': science,
                        'English': english,
                        'Average': average,
                        'Status': status
                    }
                )

        # Step-2: Write processed data to a new CSV
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)

            print(f"Student report generated in {output_file} successfully.")

    # Error handling
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found ")
    except KeyError:
        print("Error: Invalid column names in the input file")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main program
input_file = 'students.csv'
output_file = 'students_report.csv'
process_student_data(input_file, output_file)


# Learnings 
# 1. def process_student_data(input_file, output_file): Defines a function named process_student_data 
#    that takes two arguments: (input_file) → path of the CSV file to read student marks from. 
#    (output_file) → path of the CSV file to save processed results (with averages and pass/fail).
# 2. reader = csv.DictReader(infile) creates a CSV reader object that reads rows as dictionaries. 
#    Example: If CSV header is Name,Math,Science,English, then one row will look like: 
#    {'Name': 'Alice', 'Math': '70', 'Science': '80', 'English': '90'}
# 3. student_reports = [] creates an empty list to store all processed student data (with average and pass/fail).
# 4. average = round((math + science + english) / 3, 2) calculates the student’s average mark.  
#    round(..., 2) → rounds result to 2 decimal places.
# 5. for row in reader means: “Go through each student’s record (row) in the CSV file, one at a time.”
# 6. infile is the variable that represents the opened input file, so Python can read from it.
# 7. with open(output_file, 'w', newline='') as outfile: opens the output CSV file in write mode 
#    and ensures no extra blank lines are added.
# 8. writer.writeheader() writes the header row to the CSV file, and writer.writerows(student_reports) 
#    writes all the processed student data.
