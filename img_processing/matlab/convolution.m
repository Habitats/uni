function convolution
    I = imread('testimages/einstein.png');
    imshow(I);
    
    k1 = [1  1  1;
          1 -9  1;
          1  1  1];
      
    % weighed average
    k2 = [1  2  1;
          2  4  2;
          1  2  1]/16;
    
    % average
    k3 = [1  1  1;
          1  1  1;
          1  1  1]/9;
    
    % laplacian
    k4 = [0  1  0;
          1 -4  1;
          0  1  0];
    % directly apply in one convolution
    k5 = k4*-1 + (k4<0)
    
      
    % sobel dx
    k7 = [-1  0  1;
          -2  0  2;
          -1  0  1];
    % sobel dy
    k8 = [-1 -2 -1;
           0  0  0;
           1  2  1];
    
    I2 = uint8(filter2(k4, I));
    
    
%     I2 = uint8(filter2(k7, I));
%     I2 = I2 + uint8(filter2(k3, I));
    
    imshow(I2)
    
end