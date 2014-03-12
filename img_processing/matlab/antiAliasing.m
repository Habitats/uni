function antiAliasing() 
    I = imread('bricks.png');
%     figure, imshow(I)
    f = fspecial('gaussian',[5,5],2);
    I = imfilter(I,f);

    I = I(1:3:end,1:3:end);
    
    figure, imshow(I)
    imwrite(I, 'res.png');
end