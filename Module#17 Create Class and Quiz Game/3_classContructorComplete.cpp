#include <bits/stdc++.h>
using namespace std;
class Student
{
    public:
        string username;
        int id;
        int roll;
        string section;
        Student(string name, int id, int roll, string section)
        {
            this->username = name;
            this->id = id;
            this->roll = 0; //if someone doesn't fillup this attribute, this will be set to 0
            this->section = section;
        }
};

int main()
{
    Student student1 = Student("Wasi", 1001, 1, "Lions");
    Student student2 = Student("Lia", 1003, 5, "Tigers");
    cout << "Name: " << student1.username << " " << "Roll: " << student1.roll << " " << "ID: " << student1.id << " " << "Section: " << student1.section << endl;
    cout << "Name: " << student2.username << " " << "Roll: " << student2.roll << " " << "ID: " << student2.id << " " << "Section: " << student2.section << endl;
    return 0;
}







