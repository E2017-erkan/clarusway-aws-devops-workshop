milis=input("Please enter the milliseconds (should be greater than zero)(To exit the program, please type 'exit'): ")
while True:
    if milis == "exit":
        print("Exiting the program... Good Bye")
        break
    try:
        milis=int(input("Please enter the milliseconds (should be greater than zero)(To exit the program, please type 'exit'): "))
    except ValueError:
        print("Not Valid Input !!!")
        continue
    if int(milis) <= 0:
        print("Not Valid Input !!!")
    elif int(milis) == 1:
        milis=input("Please enter the milliseconds greater than 1 : ")
    else:
        if milis < 1000:
            print(f"just {milis} miliseconds/s")
            break
        milis = int(milis//1000)
        if milis < 60:
            seconds=int(milis%60)
            print(f"{seconds} second/s")
            break
        elif milis < 3600:
            seconds=int(milis%60)
            minutes=int((milis/60)%60)
            print(f"{minutes} minutes/s {seconds} second/s")
            break
        else:
            seconds=int(milis%60)
            minutes=int((milis/60)%60)
            hours=int((milis/(60*60))%60)
            print(f"{hours} hours/s {minutes} minutes/s {seconds} second/s")
            break