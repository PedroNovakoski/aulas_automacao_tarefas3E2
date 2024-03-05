def main():
    for i in range(1, 7):  
        for j in range(i):  
            print("*", end=" ")
           
            if j < i - 1:
                print(" ", end=" ")
        print()  

if __name__ == "__main__":
    main()
