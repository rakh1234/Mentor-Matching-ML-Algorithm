-- CREATE Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    UserType ENUM('BusinessInterest', 'Mentor', 'Investor') DEFAULT 'BusinessInterest',
    Interests TEXT,
    Experience TEXT,
    ProjectDetails TEXT,
    CVFilePath VARCHAR(255),
    LinkedInAccount VARCHAR(255),
    Preferences TEXT
);

-- CREATE Mentor Table
CREATE TABLE Mentor (
    MentorID INT PRIMARY KEY,
    UserID INT UNIQUE,
    -- Additional mentor-specific fields
    CVFilePath VARCHAR(255),
    LinkedInAccount VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


-- CREATE Mentor Table
INSERT INTO Users (UserID, Name, Email, Phone, UserType, Interests, Experience, ProjectDetails, CVFilePath, LinkedInAccount)
VALUES
    (1, 'John Doe', 'john.doe@example.com', '1234567890', 'BusinessInterest', 'Marketing, Finance', 'marketing', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/johndoe'),
    (2, 'Jane Smith', 'jane.smith@example.com', '9876543210', 'BusinessInterest', 'Sales, Entrepreneurship, business', 'sales', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/janesmith'),
    (3, 'Michael Johnson', 'michael.johnson@example.com', '5555555555', 'BusinessInterest', 'Technology, Startups', 'technology', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/michaeljohnson'),
    (4, 'David Lee', 'david.lee@example.com', '1111111111', 'Mentor', 'Leadership, Management', 'Management, Finance', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/davidlee'),
    (5, 'Sarah Williams', 'sarah.williams@example.com', '2222222222', 'Mentor', 'Business Strategy, Entrepreneurship', 'Business', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/sarahwilliams'),
    (6, 'Robert Anderson', 'robert.anderson@example.com', '3333333333', 'Mentor', 'Data Science, Machine Learning, Technology', 'data analytics, Technology', 'xxxxx', 'path/to/cv.pdf','linkedin.com/in/robertanderson'), 
    (7, 'Jack Willson', 'Jack. Willson @example.com', '4444444444', 'Mentor', 'Accounting', 'Accounting', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/'JackWillson),
    (8, 'Emily Davis', 'emily.davis@example.com', '5555555555', 'Mentor', 'Product Management, E-commerce', 'Product Management, E-commerce', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/emilydavis'),
    (9, 'Daniel Martinez', 'daniel.martinez@example.com', '6666666666', 'Mentor', 'Software Development, Web Development', 'Software Development, Web Development', 'xxxxx', 'path/to/cv.pdf', 'linkedin.com/in/danielmartinez');

