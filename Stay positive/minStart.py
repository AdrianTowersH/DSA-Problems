import sys

def minStart(arr):
    # 'current_sum' rastrea el valor de la suma acumulada simulando que empezamos desde 0
    current_sum = 0
    
    # 'min_sum' registrará el punto más bajo (el número más negativo) al que llegue la suma
    min_sum = 0
    
    # Recorremos cada número del arreglo para evaluar las fluctuaciones
    for num in arr:
        current_sum += num  # Sumamos el elemento actual a la cuenta acumulada
        
        # Si la suma actual cae por debajo de nuestro mínimo histórico, lo actualizamos
        if current_sum < min_sum:
            min_sum = current_sum
            
    # El valor inicial 'x' debe contrarrestar la peor caída para que el total sea al menos 1.
    # Matemáticamente: x + min_sum >= 1  -->  x >= 1 - min_sum
    # Usamos max(1, ...) porque el problema exige que el valor inicial sea un entero positivo (mínimo 1).
    return max(1, 1 - min_sum)


if __name__ == '__main__':
    # Optimizamos la lectura de datos desde la entrada estándar (consola / tubería de archivos)
    input_data = sys.stdin.read
    data = input_data().split()
    
    # Verificamos que la entrada no esté vacía
    if data:
        # El primer elemento suele indicar cuántos números contiene el arreglo (n)
        n = int(data[0])
        
        # Convertimos a enteros los elementos desde la posición 1 hasta n
        arr = [int(x) for x in data[1:n+1]]
        
        # Ejecutamos la función e imprimimos el resultado final
        print(minStart(arr))
        

# Si tu arreglo es arr = [-3, 2, -1]
# Empiezas en 0.
# Sumas -3 → current_sum = -3. Como -3 < 0, tu min_sum se vuelve -3.
#Sumas 2 → current_sum = -1. No supera el mínimo.
# Sumas -1 → current_sum = -2. No supera el mínimo.
# Al final, tu min_sum es -3.
# La fórmula hace: 1 - (-3) = 4.
# El resultado de max(1, 4) es 4.