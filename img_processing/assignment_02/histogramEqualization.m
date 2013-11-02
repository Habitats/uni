function[] = histogramEqualization()
%     grayVal = 7
%     I = ceil(rand(200,400)*(grayVal+1))-1;
%     I = mat2gray(I,[0,255]);
%     I = im2uint8(I);
    I = imread('testimages/cameraman.png');
    
    figure, imshow(I); figure, imhist(I);
    I = histeq(I);
%     I = manualEqualization(I,255);
    
%     figure, imhist(I); figure, imshow(I);
    imwrite(I,'res.png');
end

function[I2] = manualEqualization(I,grayVal)
    fprintf('manual equalization:\n');
    
    c = zeros(1,grayVal);

    for i = 1:grayVal
        c(i) = sum(sum(I==i)); 
    end
    
    c = c/(size(I,1)*size(I,2));
    sum(c)
    
    for i = 2:grayVal
        c(i) = c(i)+c(i-1);
    end
    
    I2 = zeros(size(double(I)));
 
    for i = 1:grayVal
        I == i;
        (I==i)*i*c(i);
        I2 = I2 +(I==i)*c(i);
    end
    I2 = mat2gray(I2,[0,1]);

end

