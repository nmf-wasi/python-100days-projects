# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
hg=0
for num in student_scores:
  if(hg<num):
    hg=num

print(f"The highest score in the class is: {hg}")