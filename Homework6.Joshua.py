class ValidatePassword:
  def __init__(self):
      self.users = {
        "alice": {"password": "password123", "role": "admin"},
        "bob": {"password": "bob123", "role": "user"},
        "charlie": {"password": "charlie123", "role": "moderator"}
      }
  def validate_credentials(self, username, password):
      if username in self.users and self.users[username]["password"] == password:
          return (True, self.users[username]["role"])
      return (False, None)
  def run(self):
      while True:
          username = input("Enter your username: ")
          password = input("Enter your password: ")
          valid, role = self.validate_credentials(username, password)
          if valid:
              print("Login successful. Your role is:", role)
              break
          else:
              print("Invalid username or password. Please try again.")
if __name__ == "__main__":
  validator = ValidatePassword()
  validator.run()


#problem2



shopping_lists = {
    "1st": ["Pencils", "Notebooks", "Crayons", "Glue"],
    "2nd": ["Pencils", "Notebooks", "Markers", "Glue"],
    "3rd": ["Pencils", "Notebooks", "Markers", "Colored Pencils", "Glue"],
    "4th": ["Pencils", "Notebooks", "Markers", "Colored Pencils", "Glue", "Scissors"],
    "5th": ["Pencils", "Notebooks", "Markers", "Colored Pencils", "Glue", "Scissors"]
}

def back_to_school(student_name, items_already_have):
  grade = next((g for g, supplies in shopping_lists.items() if supplies == items_already_have), None)
  if grade:
      items_needed = [item for item in shopping_lists[grade] if item not in items_already_have]
      extra_items = [item for item in items_already_have if item not in shopping_lists[grade]]

      print(f"Student: {student_name}")
      print(f"Grade: {grade}")
      print("Items already have:")
      print("\n".join(items_already_have))

      print("\nItems they need to purchase:")
      print("\n".join(items_needed))

      print("\nExtra items that they have but do not need:")
      print("\n".join(extra_items))
  else:
      print("Unable to determine grade based on provided items.")
if __name__ == "__main__":
  student_name = input("Enter student name: ")
  items_already_have = input("Enter the items the student already have (separated by commas): ").split(", ")
  back_to_school(student_name, items_already_have)
