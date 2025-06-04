import os
import P_Logger
import csv


def main():
    P_Logger.logger.info("How to save csv file")
    myDir = r'C:/Users/user/source/repos/P_Learning/Source'

    # Path to the original CSV file
    input_file = os.path.join(myDir, "input.csv")

    # Path to the new CSV file to save the data
    output_file = os.path.join(myDir, "output.csv")

    try:

        # Example object: list of dictionaries
        data = [
            {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
            {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
            {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
        ]

        # Write to CSV
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()  # Write the header
            writer.writerows(data)  # Write the data rows

        print(f"Data saved to {output_file}")

    except Exception as e:
        P_Logger.logger.error(" " + str(e))


if __name__ == '__main__':
    main()        

