function I2 = logarithm()
    I = imread('testimages/cameraman.png');
    I = im2double(I);
    
    f = 1/log(1+(max(I(:))-min(I(:))));
    f = 1
    I2 = f * log(1+I);
    subplot(2,2,1), imshow(I2);
    subplot(2,2,2), imhist(I2);
    subplot(2,2,3), imshow(I);
    subplot(2,2,4), eps(hist(I(:),linspace(0,1)));
end