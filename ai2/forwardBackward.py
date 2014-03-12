import numpy as np

def forward(O1, O2, umbrella, T, f, t=1):
    for i in range(t):
        # use the appropriate umbrealla matrix based on whether the umbrella is brought or not
        if(umbrella[i]):
            O = O1
        else:  
            O = O2
        # formula 15.12
        f = O * np.transpose(T) * f
        # normalize
        f /= sum(f)
        print "Normalized values for day %i: %f, %f" % (i + 1, f[0], f[1])
    return f

def backward(O1, O2, umbrella, T, b, t=1):
    sv = []
    # iterate from t to 0
    for i in range(t - 1, -1, -1):
        if(umbrella[i]):
            O = O1
        else:  
            O = O2
        # formula 15.13
        b = T * O * b
        # normalize
#         b /= sum(b)
        # append most likely event to SV
        sv.append(True if (b[0] > b[1]) else False)
        print "Smoothed values for day %i: %f, %f" % (i + 1, b[0] / sum(b), b[1] / sum(b))
    return sv 

def run():
    # facts we have
    # P(R1|r0) - rain on day 1 given rain day 0
    T1 = np.matrix([
                      # r0 == True 
                      [0.7, 0.3],
                      # r0 == False
                      [0.3, 0.7]])
    # P(u1|R1) - umbrella day t given rain day t 
    O1 = np.matrix([
                    # R1 == True
                    [0.9, 0],
                    # R1 == False
                    [0, 0.2]])
    # P(!u1|R1) - !umbrella day t given rain day t 
    O2 = np.matrix([
                    # R1 == True
                    [0.1, 0],
                    # R1 == False
                    [0, 0.8]])
    # initial conditions
    f0 = np.matrix([
                    [0.5],
                    [0.5]])
    # umbrealla seqeuence
    umbrella = [True, True, False, True, True]
    # do the actual calculation and print results
    print "Observed sequence: " , umbrella
    f = forward(O1, O2, umbrella, T1, f0, 5)
 
    sv = backward(O1, O2, umbrella, T1, f, 5)
    print "Most likely sequence: ", sv 
    
#     0.69, 0.41
#     0.459, 0.15
#     0.0906, 0.15
#     0.0661, 0.0455
# run()

def readme():
    pr = 25600.
    readme = 10240 * 6 
    budsjett = 68812.8
    repro = 47206.
    
    andel = pr / readme
    totaltTilTrykk = pr + readme
    
    ntnuTrykk = readme / 6.
    trykkPartner = 12800

    
    print "Alle priser eks. mva. med mindre annet er spesifisert"
    print "readme trykk: ", readme
    print "PR trykk: " , pr
    print "Totalt til trykk: " , totaltTilTrykk
    print ""

    print "Total repro: ", repro
    print "Andel repro til readme: ", round((1 - andel) * repro, 2) , " " , round((1 - andel) * 100, 2), " %"
    print "Andel repro til PR: ", round(andel * repro, 2), " " , round(andel * 100, 2), " %"
    print ""
    
    print "Per opplag NTNU-trykk: " , round(ntnuTrykk , 2)
    print "Per opplag NTNU-trykk (inkl. repro): " , round(ntnuTrykk - (1 - andel) * repro / 6 , 2)
    print "Per opplag Trykkpartner: " , trykkPartner
    print "Budsjettert pris pr. opplag: " , budsjett / 6 
    print ""

    print "Pris pr. utgave, NTNU-trykk: " , round(ntnuTrykk / 512., 2)
    print "Pris pr. utgave, NTNU-trykk (inkl. repro): " , round((ntnuTrykk - (1 - andel) * repro / 6) / 512., 2)
    print "Pris pr. utgave, Trykkpartner: " , round(trykkPartner / 500., 2)
    print "Budsjettert pris pr. utgave (inkl. mva): "  , round(budsjett / (512.*6), 2)

readme()
