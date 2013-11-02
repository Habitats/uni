function fourier()
    I = imread('testimages/cameraman.png');
    
    F = fft2(I);
    
    % shift
    F = fftshift(F);
    
    % i couldn't figure out the actual filter...
    f = 'high/lowpassfilter';

    % apply the filter
    F = imfilter(F, f);

    % shift back and inverse-transform
    F = ifftshift(F);
    F = ifft2(F);
    I = uint8(F);
    
    imshow(I);
end