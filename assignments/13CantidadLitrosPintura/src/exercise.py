import math
def main():
    area=float(input('Area a pintar en metros:'))  
    rend=float(input('Rendimiento (m2/1):'))    
    litros= area/rend 
    res=math.cell(litros)
    print=(f'litros a comprar: {res}')

if __name__ == '__main__':
    main()
