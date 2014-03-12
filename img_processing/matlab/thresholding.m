function thresholding()
%     I = imread('testimages/threshold.png');
    I = imread('testimages/region.png');
    
    I = uint8(I);
    
    seeds = multiSegmentThresholing(I, 254);
    
    I = regionGrowing(I, seeds, 100);

    imshow(I);
    imwrite(I,'res.png');
end

% takes in a vector of threshold values and segments the image
function I = multiSegmentThresholing(I,t)

    I2 = zeros(size(I));
    seg = length(t);
    for i = 1:seg
        I2 = I2+(I > t(i))*i/seg + (I < t(i))*0;
    end
    
    I = I2;
end

function I = basicGlobalThresholing(I)
    t = mean(I(:));
    oldT = 1;
    I = double(I);
    while abs(oldT - t) > 0.005
        oldT = t;
        g1 = I .* (I > t);
        g2 = I .* (I <= t);
        imshow(g1);
        imshow(g2);
        m1 = sum(g1(:))/sum(g1(:)>0);
        m2 = sum(g2(:))/sum(g2(:)>0);
        
        t = (m1 + m2)/2
    end
    
    I = multiSegmentThresholing(I, t);
end

function I = regionGrowing(I, seeds, t)
    
    imshow(seeds);
    I2 = zeros(size(I));
    set(0, 'RecursionLimit',1000000);
    
    keepLooping = true;
    while keepLooping
        [r, c] = find(seeds==1,1,'first');
        if length(r) == 0
            keepLooping = false;
        end
        seeds = reduceRegion(seeds, r,c);
        I2(r,c) = 1;
        imshow(seeds);
        imshow(I2);
    end
   
    
    I = seeds
 
    imshow(I);
end

function seeds = reduceRegion(seeds, r, c)
    if seeds(r,c) == 1
        seeds(r,c) = 0;
        seeds = reduceRegion(seeds, r+1,c);
        seeds = reduceRegion(seeds, r-1, c);
        seeds = reduceRegion(seeds, r, c+1);
        seeds = reduceRegion(seeds, r, c-1);
    end
end

function Phi = segCroissRegion(tolerance,Igray,x,y)
    if(x == 0 || y == 0)
        imshow(Igray,[0 255]);
        [x,y] = ginput(1);
    end
    Phi = false(size(Igray,1),size(Igray,2));
    ref = true(size(Igray,1),size(Igray,2));
    PhiOld = Phi;
    Phi(uint8(x),uint8(y)) = 1;
    while(sum(Phi(:)) ~= sum(PhiOld(:)))
        PhiOld = Phi;
        segm_val = Igray(Phi);
        meanSeg = mean(segm_val);
        posVoisinsPhi = imdilate(Phi,strel('disk',1,0)) - Phi;
        voisins = find(posVoisinsPhi);
        valeursVoisins = Igray(voisins);
        Phi(voisins(valeursVoisins > meanSeg - tolerance & valeursVoisins < meanSeg + tolerance)) = 1;
    end
end
