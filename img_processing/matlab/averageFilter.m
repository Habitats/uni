function G = averageFilter(I)

    % box-filter
    f = fspecial('average', 15);

    % alternative:
    n = 15;
    f = ones(n);
    f = f/sum(sum(f));

    G = imfilter(I, f,'symmetric');

end