def main():
    mass=float(input('\nm:'))
     
    def calc_E(mass):
        digits=len(str(mass))
        p=str(mass).index('.')
        calc_E.light_Speed=300_000_000
        if p==digits-2 and str(mass)[digits-1]=='0':
            n_Decimal=3 
        else:
            n_Decimal=digits-(p+1)

        return mass*(calc_E.light_Speed**2), n_Decimal
    
    energy, presicion = calc_E(mass)
    print(f"Energy: {energy:.{presicion}e} J", end='\n\n')
    
main()