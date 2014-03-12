function derivatives()
    I = imread('testimages\cameraman.png');
     
    laplacian = [0, 1, 0; 1, -4, 1; 0, 1, 0];

    % using Sobels method
    dx = [-1,-2,-1;
           0, 0, 0;
           1, 2, 1];
    dy = [-1, 0, 1;
          -2, 0, 2;
          -1, 0, 1];
    
    gradient = apply(I, dx)+apply(I, dy);
    magnitude = abs(apply(I, dx)) + abs(apply(I, dy))
    imshow(uint8(magnitude))
    imshow(gradient)
    sharpened = I+gradient;
    quivert(sharpened)
%     figure, imshow(gradient); figure, imshow(sharpened);
%     imwrite(gradient,'gradient.png');
%     imwrite(sharpened, 'sharpened.png');
end

function [I2]= apply(I,f)
    I2 = imfilter(I, f, 'symmetric');
end