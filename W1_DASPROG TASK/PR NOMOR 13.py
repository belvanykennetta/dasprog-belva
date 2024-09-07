#How many students enrolled
students = int(input('Enter the number of students enrolled: '))

#number of sections required
section_capacity = 30
number_of_sections_required = students // section_capacity

#remaining students
remaining_students = students % section_capacity

print('The number of students enrolled: ',students,'students' )
print('The number of sections required: ', number_of_sections_required)
print('The number of remaining students: ',remaining_students)