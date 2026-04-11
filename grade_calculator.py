marks = int(input('Enter score:'))
if 90 <= marks and marks <= 100 :
    if marks >95:
        print(f'score : {marks} -> Grade : A+ - Excellent!')
    else :
        print(f'score : {marks} -> Grade : A- - Excellent!')
elif 80 <= marks >= 89 :
    if marks > 85:
        print(f'score : {marks} -> Grade : B+ - Very good!')
    else:
        print(f'score : {marks} -> Grade : B- - Excellent!')
elif 70 <= marks >= 79 :
    if marks > 75:
        print(f'score : {marks} -> Grade : C+ - Excellent!')
    else :
        print(f'score : {marks} -> Grade : C- - Excellent!')
elif 60 <= marks >=69 :
    if marks > 65:
        print(f'score : {marks} -> Grade : D+ - Excellent!')
    else :
        print(f'score : {marks} -> Grade : D- - Excellent!')
elif 0 > marks < 60 :
    print(f'score : {marks} -> Grade : F - Excellent!')
else:
    print('Invalid Score!')
    
    

    
    
