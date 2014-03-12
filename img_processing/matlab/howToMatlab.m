% Assignment 1 - Voluntary Part: Introduction
% TDT4195 - Visual Computing Fundamentals
% ================================================
% Add your code to this file where indicated
%
% This is the voluntary part of the assignments 1

% A few notes about matlab:
% - Almost all variables are matrices
% - You don't have to specify datatypes (like int, char, string etc.)
% - Matlab do not use curly braces {} or parantheses, instead it use the keyword end
% - Most statements that don't end with a ; will print out a result, thus it don't have
%   the exact same meaning as ; in Java and C/C++. Still, it can be used to seperate
%   statements on the same line
% - Matrices are accessed using y,x like A(y,x). So first the row and then the column is addressed.

% ------------------------------------------------

% Task 1: Basic Matlab. Avoid loop structures in this first task as this is more efficient in Matlab!!!

% Task 1.1: Create a 4x6 matrix, A, where each element is 1
A = ones(4,6);
% Task 1.2: Print the contents of the matrix to the screen
A;
% Task 1.3: Create another 6x4 matrix, B, with random values
B = rand(6,4);
% Task 1.4: Print the contents of the new matrix to the screen
B;
% Task 1.5: Do matrix multiplication on A and B and print result (resulting matrix should be 4x4)
C = A * B;
% Task 1.6: Do element-by-element multiplication on B and B (note the difference from task 1.5)
C = B .* B;
% Task 1.7: Change element x=2,y=4 in A to 2 (remember Matlab indexes start with 1)
A(4,2) = 2; 
% Task 1.8: Set all elements in matrix A with x index 2 and 5 and y index from 2 to 3 to 4 without using any loops
A(2:3,[2,5]) = 4;
% Task 1.9: Add 0.5 to the first row in matrix B (again no loops)
B(:,1) = B(:,1) + 0.5;
% Task 1.10: Substract 0.5 from all elements in B that are above 1 (again no loops)
B = B - 0.5*(B>1)
% Task 1.11: Type whos to see details of current variables
whos
% Task 1.12: Type clear A to delete matrix A
clear A
% Task 2: Control structures and functions in matlab

% Task 2.1: Create a for loop on the variable i from 4 to 20 with step 2 and print i*2 and i if i > 10
for i = 4:2:20
    if i>10
        i*2
    end
end
% Task 2.2: Create a function (and a "magnitude.m" file for it) called magnitude that takes a vector (one dimension in the matrix has size 1) in and computes the magnitude of it. magnitude = sqrt(x^2 + y^2 + z^2...)

% Task 2.3: Call your magnitude function on B(:) ( the (:) statement makes B into a vector) (note that this can be done without any loops or ifs)

% Task 3: Basic image processing in matlab (see functions that start with im in matlab)

% Task 3.1: Read one of the testimages (i.e. mandrill.png, lena.png ..) from disk into a matrix
I = imread('testimages/lenacolor.png');

% Task 3.2: Convert image to grayscale
I = rgb2gray(I);

% Task 3.3: Convert image to floating point (double) representation
I = im2double(I);

% Task 3.4: Show image on screen (remember to put figure; before this and all other commands that displays something on screen to insure that all images are shown)
%  figure, imshow(I);

% Task 3.5: For all pixels (elements in the image matrix) with values above 0.7 set the pixel value to 1.0 (recall task 1.10)
I2 = I .* (I <= 0.7) + (I > 0.7);

% Task 3.6: Show image on screen
% figure, imshow(I2);

% Task 3.7: Compute the maximum and minimum gray-value of the image
minGray = min(I2(:))
maxGray = max(I2(:))

% Task 3.8: Create and show a histogram of the image
% imhist(I2);

% Task 3.9: Save image to disk and call it result.png
imwrite(I2, 'result.png')
