function blending()
    I1 = imread('testimages/steel.png');
    I2 = imread('testimages/lena.png');
    
    for x = 0:.1:1
        I3 = x * I1 + (1-x) * I2;
        imshow(I3);
    end
end
