def water_jug_problem(capacity_a, capacity_b, target):
    jug_a = 0
    jug_b = 0

    while jug_a != target and jug_b != target:
        print(f"jug_a :{jug_a} | jug_b :{jug_b}")
        if jug_a==0 :
            jug_a = capacity_a
        elif jug_a>0 and jug_b<capacity_b:
            tranfer = min(jug_a,capacity_b-jug_b)
            jug_b+=tranfer
            jug_a-=tranfer
        elif jug_b == capacity_b:
            jug_b = 0
        elif jug_b>0 and jug_a<capacity_a:
            tranfer = min(jug_b,capacity_a-jug_a)
            jug_b-=tranfer
            jug_a+=tranfer

    print(f"jug_a :{jug_a} | jug_b :{jug_b}")
    print("hurrayyy...target reached!")

#example
water_jug_problem(6,5,2)  
                        





