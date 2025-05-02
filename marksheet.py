import streamlit as st

class Marksheet:
    def __init__(self, rollno, student, marks):
        self.rollno = rollno
        self.student = student
        self.subjects = ["Math", "English", "Science", "Computer"]
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total = self.calculate_total()
        return (total / (len(self.subjects) * 100)) * 100

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        elif percentage >= 60:
            return 'C'
        else:
            return 'Fail'

    def display_marks(self):
        st.markdown("---")
        st.markdown(f"### 🧾 Marksheet for {self.student} (Roll No: {self.rollno})")
        for i in range(len(self.subjects)):
            st.write(f"**{self.subjects[i]}:** {self.marks[i]}")
        st.success(f"**Total Marks:** {self.calculate_total()}")
        st.info(f"**Percentage:** {self.calculate_percentage():.2f}%")
        st.warning(f"**Grade:** {self.calculate_grade()}")


# Streamlit App
st.set_page_config(page_title="Student Marksheet", layout="centered")
st.title("📚 Student Marksheet Generator")

num_students = st.number_input("Enter number of students:", min_value=1, step=1)

students_data = []

for i in range(num_students):
    with st.expander(f"Enter details for Student {i + 1}"):
        rollno = st.number_input(f"Roll No (Student {i+1}):", key=f"roll{i}")
        name = st.text_input(f"Name (Student {i+1}):", key=f"name{i}")
        marks = []
        for subject in ["Math", "English", "Science", "Computer"]:
            mark = st.number_input(f"{subject} Marks:", min_value=0, max_value=100, key=f"{subject}{i}")
            marks.append(mark)
        if st.button(f"Generate Marksheet for Student {i+1}", key=f"btn{i}"):
            student = Marksheet(rollno, name, marks)
            student.display_marks()
