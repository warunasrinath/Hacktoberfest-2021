def accept_matrix(M) :
    print("\nEnter the order of the Matrix (row,col) : ")
    r = int(input("\trow = "))
    c = int(input("\tcol = "))
    print("Enter the elements of the Matrix : \n")
    for i in range(r) :
       A = []
       for j in range (c) :
          A.append(int(input()))
       M.append(A)
    print("\nMatrix accepted successfully\n")


def display_matrix(M,r,c): 
   print("Matrix (%d,%d) : "%(r,c))
   for i in range(r) :
      print("\t\t",end=' ')
      for j in range(c):
          print("%3d"%M[i][j],end=' ')
      print("")	

def check_for__saddlepoint(M,r,c) :
    count = 0;
    for i in range(r) :
        #Find the minimum element of row i
        
        min_row = M[i][0]
        ci = 0
        for j in range(1,c) :
            if (min_row > M[i][j]) :
                min_row = M[i][j];
                ci = j
        #Check if the min_row is also the maximum element of column or not
        flag = 1
        for ri in range(r) :
            if (min_row < M[ri][ci]):
                flag = 0
                break
        if (flag == 1) :
            count += 1           
            print("%d value is minimum in row(%d) and maximum in column(%d)"%(min_row,i+1,ci+1))
    if (count == 0) :
        print("No Saddle Point Exist for the given Matrix")
    else :
        print("%d Saddle Point Found in the given Matrix"%count)
    
       
def main():   
   while True :
       print("\t\t\t1: Accept Matrix");
       print("\t\t\t2: Display Matrix");
       print("\t\t\t3: Find the Saddle Point");
       print("\t\t\t4: Exit");
       ch = int(input("Enter your choice : "))       
       if (ch == 4):
           print ("End of Program")
           break
       elif (ch==1):
           Mat = []
           print("Input the Matrix ")
           accept_matrix(Mat)
           r = len(Mat)
           c = len(Mat[0])           
       elif (ch==2):
           display_matrix(Mat,r,c)           
       elif (ch==3):
           display_matrix(Mat,r,c)
           check_for__saddlepoint(Mat,r,c)
       else :
           print ("Wrong choice entered !! Try again")

main()
quit()

