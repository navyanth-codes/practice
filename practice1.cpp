// Question write a program to store and print roll.n0,name,age,marks of a student using structures

#include<iostream>
using namespace std;

struct student{
    int RollNo;
    char name[27];
    int age;
    int marks;

};
int main(){
    struct student s={10,"navyanth",19,976};
    cout<<s.RollNo<<endl<<s.name<<endl<<s.age<<endl<<s.marks<<endl;
}
