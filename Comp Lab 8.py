def menu():
  print('      Menu Grades      ')
  print()
  print('[1] - Add Tests')
  print()
  print('[2] - Remove Tests')
  print()
  print('[3] - Clear Tests')
  print()
  print('[4] - Add Assignments')
  print()
  print('[5] - Remove Assignments')
  print()
  print('[6] - Clear Assignments')
  print()
  print(str('[D] - Display Scores'))
  print()
  print(str('[Q] - Quit'))
  print()

print()

def menuGrades():
  
  menuGrades = ['Add Tests','Remove Tests','Clear Tests','Add Assignments', 'Remove Assignments', 'Clear Assignments']

menuGrades()


scores = []

test_grade = []
program_grade = []

final_grade = []

def add_test_score(value):
  test_grade.append(value)
  return

def add_program_score(value):
  program_grade.append(value)
  return

def clear_test_score():
  test_grade.clear()
  return

def clear_program_score():
  program_grade.clear()
  return

def remove_test_score(value):
  test_grade.remove(value)
  return

def remove_program_score(value):
  program_grade.remove(value)
  return

  


'''for menu_choice in range (1,99):
  if menu_choice == 'Q':
    break'''

#for menu_choice in range(1,99):
def main():
  while True:

    menu()
  
    menu_choice = input('==>')
    print()
                 
    if menu_choice == '1':
      
      test_input = float(input('Enter the new Test score 0-100 ==>'))
      add_test_score(test_input)
      print()
      
    elif menu_choice == '2':
      remove_input = float(input('Enter the Test to remove 0-100 ==>'))
      remove_test_score(remove_input)
      print('')
      
    elif  menu_choice == '3':
      print()
      clear_test_score()

    elif menu_choice == '4':
      assignment_grade = float(input('Enter the new Assignment score 0-100 ==>'))
      add_program_score(assignment_grade)
      
    elif menu_choice == '5':
      assignment_remove = float(input('Enter the Assignment to remove 0-100 ==>'))
      remove_program_score(assignment_remove)
                                                      
    elif menu_choice == '6':
      print('')
      clear_program_score()

    elif menu_choice == 'D':
      print('')
      print("Tests: ", test_grade)
      print("Assignments: ", program_grade)
      print("\n\n\n\n")

    elif menu_choice == 'Q':
      break

main()



          






    

      
      
      
      
      
