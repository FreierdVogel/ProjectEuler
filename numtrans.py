import stopwatch
def numtran(n):
    numero=""
    unidad = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dieces = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    decena = ['veint', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']      
    if int(str(n)[0])==1:
        numero = dieces[int(str(n)[1])]
        if int(str(n)[-1])==0:
            numero = dieces[0]
    else:
        numero = decena[int(str(n)[0])-2]+" y "+unidad[int(str(n)[1])]
        if int(str(n)[-1])==0 and int(str(n)[0])!=2:
            numero = decena[int(str(n)[0])-2]
        elif int(str(n)[-1])==0 and int(str(n)[0])==2:
            numero = "veinte"
    return numero.capitalize()

print(stopwatch.crono(numtran(200))," s, ", numtran(110))