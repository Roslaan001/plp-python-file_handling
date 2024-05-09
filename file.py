def write_to_file(filename ="hello.txt", content = "hello world"):

  try:
    with open("hello.txt", 'w') as f:
      if isinstance(content, list):
        f.writelines(["\n I will make it Bi Idhnillahi soon", "\n i will be so glad i started", "\n Alhamdu Lillahi always"])  # Write multiple lines efficiently if content is a list
      else:
        f.write("Allah Akbar")  # Write a single line if content is a string
      print(f"Successfully wrote to '{filename}'.")
  except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")

def read_file(filename ="hello.txt"):
 
  try:
    with open("hello.txt", 'r') as f:
      contents = f.read()
      print(f"Contents of '{filename}':\n{contents}")
  except FileNotFoundError as e:
    print(f"Error reading file: {e}")

def append_to_file(filename, content):
  filename = "hello.txt"
                    

  try:
    with open("hello.txt", 'a') as f:
      if isinstance(content, list):
        f.writelines(content)
      else:
        f.write(content + '\n')  # Add newline for clarity if appending a single line
      print(f"Successfully appended to '{filename}'.")
  except (IOError, OSError) as e:
    print(f"Error appending to file: {e}")
    
    
    isinstance("hello world")
    
    
    
write_to_file()
read_file()
append_to_file("hello world", "hello world")