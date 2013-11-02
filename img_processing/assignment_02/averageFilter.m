I = imread('testimages/cameraman.png');

% box-filter
f = fspecial('average', 15);

% alternative:
n = 15;
f = ones(n);
f = f/sum(sum(f));

G = imfilter(I, f);

img_to_show = uint8(G);
figure(1);
imshow(img_to_show)