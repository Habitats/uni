function houghTransform()
    I = imread('testimages/steel.png');
    
    BW = edge(I, 'canny');
    
    [H, theta, rho] = hough(BW, 'RhoResolution',0.7,'Theta',-90:0.5:89.5);
    P = houghpeaks(H,40);
    
    lines = houghlines(BW, theta, rho, P);
    HTrans = imadjust(mat2gray(H));
    figure, imshow(HTrans);
    imwrite(HTrans,'h.png');
    
    figure, imshow(I), hold on;
    for k = 1:length(lines)
        xy = [lines(k).point1; lines(k).point2];
        plot(xy(:,1), xy(:, 2), 'LineWidth', 2, 'Color', 'green');
    end
    
    imwrite(I, 'res.png');

    
end