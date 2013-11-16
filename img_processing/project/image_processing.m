function image_processing()
    path = 'projectimages/sweetsA02.png';
    %     03
    %     blue:    16
    %     green:   16
    %     yellow:  14
    %     orange:  10
    %     pink:    11
    %     red:      9
    
    %     02
    %     green:   20
    %     blue:    16
    %     pink:    16
    %     yellow:  19
    %     orange:  13
    %     red:     15
    
%     path = 'projectimages/circle2.png';
    
    I = imread(path);
    
    % to avoid 0-rgb values
    I = I + uint8(I == 0);

    % find circles
    [centers, radii, circles] = identifyCircles(I);
    imshow(circles);
    viscircles(centers, radii,'EdgeColor','b');
    
    % create an image where each circle center is represented by a 1
    circleImage = zeros(size(I));
    for i = 1:length(centers(:,1))
        x = round(centers(i,1));
        y = round(centers(i,2));
        circleImage(y,x,:) = 1;
    end
    
    % count circles
    numCircles = sum(circleImage(:)>0)/3;
    imwrite(circleImage, 'circleImage.png');
    
    % process the image to be suitable for color sampling
    processed = identifyColors(I);
    % remove all pixles but the centers of the circles
    colors = processed .* uint8(circleImage);
    imwrite(colors,'colors.png');
    
    % count the number of pixles with a given color
    colorPalette = countColors(I, colors);
    
    imshow(I);
    % draw circles on the currently active image
    viscircles(centers, radii,'EdgeColor','b');

    % print it in a pretty fashion
    fprintf('\nTotal number of objects: %i\n',numCircles);
    for i = 1:length(colorPalette)
       fprintf('RGB: ');
       fprintf('%3i ', colorPalette(i).rgb(:) );
       fprintf('\tNumber of similar: %3i\n', colorPalette(i).num );
    end
    
    imwrite(processed, 'processed.png');
    imwrite(I,'image.png');
    
    writeCircles(colorPalette);
end

function processed = identifyColors(I)
    
    processed = I;
    % use blurred image to get color values for the circles
    % todo: try doing this another time
    for i = 1:5
        processed = medianFilterRgb(processed, 10);
    end

    % remove noise
    processed = imfilter(processed, fspecial('average',2),'symmetric');
    
    % trying to normalize the lighting
    bg = imclose(I, strel('disk',30));
    bg = imfilter(bg, fspecial('gaussian',30,30),'symmetric');
    bg = imcomplement(bg); 
    
    imshow(processed)
    imwrite(processed, 'processed.png');
end

function [centers,radii, circles] = identifyCircles(I)
    
    gI = rgb2gray(I);
    
    circles = gI;
    circles = imfilter(circles, fspecial('laplacian',0.2));
    
    % remove noise
    circles = imfilter(circles, fspecial('average',3));
    
    % normalize the image for easier thresholding
    circles = histeq(circles);

    % filter out the circles
    t = max(circles(:)-30);
    circles = circles .* uint8(circles > t);
    imwrite(circles, 'circles.png');
    
    % identify circles with a hough-transform
    [centers,radii,metric] = imfindcircles(circles,[10 25],'Sensitivity',0.93 );

end

function colorPalette = countColors(I, colors)
    colorPalette = struct;
    colorNum = 1;
    
    % while there are still unchecked pixles in the image
    while max(colors(:)) > 0
        
        % find the first colored circle
        [y,x] = find(colors>0,1);
        
        imshow(colors)
        similarColors = double(rgb2gray(colors)>0);

        
        % find all the pixels that differ less than dt in each of the rgb
        % channels, then combine them

        rgb = true;
        if(rgb)        
            % set the delta value for rgb-similarity
            dt = 40; 
            i = 1;
            for j = colors(y,x,:)
                
                similarColorsSingleChannel = (colors(:,:,i) <= (j + dt)) .* (colors(:,:,i) > (j - dt));
                imshow(similarColorsSingleChannel)
                
                similarColors = similarColors .* similarColorsSingleChannel;
                imshow(similarColors)
                i = i + 1;   
            end
        else
            % this doesn't really work
            dt = 0.02;
            hsvColors = rgb2hsv(colors); 
            similarColors = (hsvColors(:,:,1) < (hsvColors(y,x,1) + dt)) .* (hsvColors(:,:,1) > (hsvColors(y,x,1) - dt));
        end
        % number of objects that share the same color
        numberOfSimilar = sum(similarColors(:)>0);
        
        
        % remove the objects that have the same color from the original
        % image so that we can proceed with a new color
        imshow(similarColors)
        similarColors = uint8(repmat(similarColors,[1,1,3]));
        matched = colors .* similarColors;
        imshow(matched)
        imshow(colors)
        colors = colors - matched;
        imshow(colors)

        % calculate the rgb-value for the current color and save them in a
        % hashtable
        rgb = I(y,x,:);
        rgb = rgb(:);

        [y,x] = find(similarColors(:,:,1) == 1);
        pairs = [x, y];

        colorPalette(colorNum).rgb = rgb;
        colorPalette(colorNum).similar = {};
        colorPalette(colorNum).pairs = pairs;
        colorPalette(colorNum).num = numberOfSimilar;
        colorNum = colorNum + 1;

    end
end

function writeCircles(colorPalette)
    % format: index-numberOfSimilar-rrr:ggg:bbb-x:y
    f = fopen('circles.txt', 'w');
    for i = 1:length(colorPalette)
        rgb = sprintf('%i:',colorPalette(i).rgb(:));
        rgb = rgb(1:end-1);
        pairs = colorPalette(i).pairs;
        s = '';
        for j = 1:length(pairs)
            s = sprintf('%s:%i,%i',s, pairs(j,1), pairs(j,2) );
        end
        s = s(2:end);
        line = sprintf('%i-%i-%s-%s\r\n', i, colorPalette(i).num, rgb, s);
        fprintf(f, line);
        fprintf(line);
    end
        
    fclose(f);
end

function median = medianFilterRgb(I, m)
    m = [m, m];
    median = I;
    for i = 1:3 
        median(:,:,i) = medfilt2(I(:,:,i),m,'symmetric');    
    end 
end