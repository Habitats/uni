I = double(imread('testimages/cameraman.png')); % load image
illustrate = uint8(I); figure (); imshow(illustrate);
Iscaled = double(I)/255.0;

density =0.25;
Inoisy = imnoise(Iscaled , 'salt & pepper' , density );
illustrate = uint8( Inoisy *255.0); figure(); imshow( illustrate );
filename = sprintf('withsaltpeppernoise.png');
imwrite( illustrate , filename ); %save results

mean=0.0; std =0.1;
Inoisy = imnoise( Iscaled , 'gaussian' , mean ,std);
% max(max(Inoisy)), min(min(Inoisy))
illustrate = uint8( Inoisy *255.0); figure(); imshow( illustrate );
filename = sprintf('withgaussiannoise.png');
imwrite( illustrate , filename ); %save results