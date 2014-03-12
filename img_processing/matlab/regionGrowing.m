function regionGrowing()
    I = imread('testimages/region.png');
    
    f = I .* globalThresholding(I);
    
    imshow(I);
end