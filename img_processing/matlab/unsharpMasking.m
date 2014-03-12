function I = unsharpMasking(I)
%     I = imread('testimages/einstein.png');
    blur = averageFilter(I);
    mask = I-blur;
    
    I = I + 1* mask;
    imshow(I)
end