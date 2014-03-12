function normalization()
    I = imread('testimages/einstein_lowcontrast.png');
    
    c = min(I(:));
    d = max(I(:));
    a = 0;
    b = 255;
    
    I2 = (I-c) * ((b-a)/double(d-c));
    
    imshow(I2);
end