function[] = averageFiltering()
%     path = 'withgaussiannoise.png';
    path = 'withsaltpeppernoise.png';

    I = imread(path);
%     I = buildIn(I);
    I = manualMedian(I);
%     I = medfilt2(I,[3,3]);

    imshow(I);
    imwrite(I,'res.png');
end

function[I2] = manualMedian(I)
    
    I2 = I;
    for r = 2:size(I,1)-1
        for c = 2:size(I,2)-1
            section = I(r-1:r+1,c-1:c+1);
%             section = reshape(section,1,[]);
            n = median(section(:));
            I2(r,c) = n;
        end
    end
end

function[I] = manualAverage(I)
    s = [3,3];
    filter = ones(s(1),s(2));
    filter = filter/sum(sum(filter));
    
    for r = 2:size(I,1)-1
        for c = 2:size(I,2)-1
            section = I(r-1:r+1,c-1:c+1);
            n = sum(sum(section))/numel(section);
            I(r,c) = n;
        end
    end
%     filter = ones(s(1),s(1))*-1;
%     filter(ceil(s(1)/2),ceil(s(1)/2)) = abs(sum(sum(filter)))
end

function[I] = buildIn(I)
    avg = fspecial('average',[3,3]);
    I = imfilter(I, avg);
end