// Question - Write a program to store the roll no. (starting from 1),
// name and age of 5 students
// and then print the details of the student with roll no. 2.

#include<iostream>
using namespace std;

int main(){
struct student{
    int rollno;
    char name[27];
    int age;

};
    struct student stdu[5];
    for(int i=0;i<5;i++){
        stdu[i].rollno=i+1;
        cout<<"rollno is "<<stdu[i].rollno<<"\n";
        cout<<"enter name";
        cin>>stdu[i].name;
        cout<<"enter age";
        cin>>stdu[i].age;
    }
    for(int i=0;i<5;i++){
        if(stdu[i].rollno==2){
            cout<<"student rollno"<<stdu[i].rollno<<endl;
            cout<<"student name"<<stdu[i].name<<endl;
            cout<<"student age"<<stdu[i].age<<endl;
        }
    }
    return 0;
}
