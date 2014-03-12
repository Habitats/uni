function fourier()

%     I = imread('testimages/cameraman.png');
    I = imread('testimages/einstein.png');
    smoothing(I);
%     convolution(I);
end

function convolution(I)
    f = fspecial('average', [5 5]);
%     I2 = imfilter(I, f, 'symmetric');
    F = fft2(I);
    F2 = fft2(f);
    
    c = F .* F2;
    
    c = ifft2(c);
    
    subplot(1,2,1), imshow(I);
    subplot(1,2,2), imshow(c);
end

function smoothing(I)
    F = fft2(I);
    
    % shift
    F = fftshift(F);
    
    Fpattern = logarithm(F);
    
    imshow(Fpattern);
    % i couldn't figure out the actual filter...
%     f = 'high/lowpassfilter';

    circle = imread('testimages/hp_circle_small_gaussian.png');
    circle = im2double(rgb2gray(circle));
    circle = strel('disk',256);
%     F = abs(F);
    F = F .* im2double(circle);
    % apply the filter
%     F = imfilter(F, f);

    % shift back and inverse-transform
    F = ifftshift(F);
    F = ifft2(F);
    I = uint8(F);
    
    imshow(I);    
%     subplot(1,2,1), imshow(I);
%     subplot(1,2,2), imshow(Fpattern);
end