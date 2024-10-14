testcase = int(input())

for _ in range(testcase):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    q = int(input())
    
    if q == 1:
        jumlah_max = float("-inf")
        
        for i in range(n):
            jumlah_sekarang = 0
            
            for j in range(i, min(i + k, n)):
                jumlah_sekarang += array[j]
                jumlah_max = max(jumlah_max, jumlah_sekarang)
                
        print(jumlah_max)
    
    elif q == 2:
        jumlah_min = float("inf")
        
        for i in range(n):
            jumlah_sekarang = 0
            
            for j in range(i, min(i + k, n)):
                jumlah_sekarang += array[j]
                jumlah_min = min(jumlah_min, jumlah_sekarang)
                
        print(jumlah_min)