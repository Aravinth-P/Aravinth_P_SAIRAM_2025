Create TABLE Students (
	  StudentID int primary key,
    FirstName varchar(100) NOT NULL,
	  LastName varchar(100) NOT NULL,
    Email varchar(100) UNIQUE NOT NULL,
    GPA float CHECK(GPA > 4.0),
    EnrollmentDate timestamp DEFAULT current_timestamp()
);
Create TABLE Department (
	  DepartmentID int primary key,
    DepartmentName varchar(100) NOT NULL,
	  HOD varchar(100)
);
Create TABLE Course (
	  CourseID int primary key,
    CourseName varchar(100) NOT NULL,
	  Description varchar(100),
    Credits int CHECK(Credits BETWEEN 1 AND 6),
    DepartmentID int references Department(DepartmentID)
);
Create TABLE Enrollment (
	EnrollmentID int primary key,
    StudentID int references Students(StudenTID),
    CourseID int references Course(CourseID),
    Email varchar(100) UNIQUE NOT NULL,
    EnrollmentDate timestamp DEFAULT current_timestamp
);
