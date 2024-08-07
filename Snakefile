rule all:
    input:
        "output/new.csv",
        "output/SecCSV.csv",
        "output/binary.png"
        

rule process:
    input:
        "input/df_grouped_byPlateandPertype.csv"
    output:
        "output/new.csv"
    script:
        "code/test.py"

rule plot:
    input:
        "output/new.csv"
    output:
        "output/SecCSV.csv"
    script:
        "code/plot.py"

rule binary:
    input:
        "input/RPE.tif"
    output:
        "output/binary.png"
    script:
        "code/ForDocker.py"







