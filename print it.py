import os
import time

# Path to the directory you want to monitor
directory = "/path/to/directory"

while True:
  # Get a list of all PDF files in the directory
  files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

  # Print the PDF files
  for f in files:
    # Construct the full path to the PDF file
    file_path = os.path.join(directory, f)

    # Send the PDF file to the printer
    os.startfile(file_path, "print")

  # Sleep for 1 second before checking the directory again
  time.sleep(1)
  
  
  
  
  OR
  
  
  
  import os
import time

# Path to the directory you want to monitor
directory = "/path/to/directory"

while True:
  # Get a list of all PDF files in the directory
  files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

  # Print the PDF files
  for f in files:
    # Construct the full path to the PDF file
    file_path = os.path.join(directory, f)

    # Print the PDF file using the lpr command
    os.system(f"lpr {file_path}")

  # Sleep for 1 second before checking the directory again
  time.sleep(1)
