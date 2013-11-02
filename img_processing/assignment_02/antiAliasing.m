function antiAliasing() 
    I = imread('bricks_aliased_factor_4.png');
%     figure, imshow(I)
    f = fspecial('gaussian',[5,5],2);
    I = imfilter(I,f);

%     figure, imshow(I)
    imwrite(I, 'res.png');
end