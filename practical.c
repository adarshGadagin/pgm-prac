// 1) Develop a program in C to implement Binary Search with Approrpiate Input and Output
#include <stdio.h>
#include <stdlib.h>
int main(){
    int i, n, low, mid, high, tar;
    printf("Enter the size of array : ");
    scanf("%d",&n);
    low=0;
    high=n-1;
    int arr[n];
    printf("Enter %d elements in sorted array : ",n);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the target : ");
    scanf("%d",&tar);
    while(low<=high){
        mid=(low+high)/2;
        if(arr[mid]==tar){
            printf("Target found at %d\n",mid+1);
            exit(0);
        }
        if(tar<arr[mid]){
            high=mid-1;
        }
        else{
            low=mid+1;
        }
    }
    printf("Target not found\n");
    return 0;
}

// 2) Develop a program in C using a while loop to test whether a number is prime.
#include <stdio.h>
int main(){
    int i=2, n, isPrime=1;
    printf("Enter a positive integer : ");
    scanf("%d",&n);
    if(n<=1){
        isPrime=0;
    }
    else{
        while (i<n/2){
            if(n%i==0){
                isPrime=0;
            }
            i++;
        }
    }
    if(isPrime==1){
    printf("%d is prime\n",n);
    }
    else{
        printf("%d is not prime\n",n);
    }
    return 0;
}

// 3) Develop a Program in C for string processing to count vowels and consonants without using string handling library functions.
#include <stdio.h>
int main(){
    int i=0, vowels=0, consonants=0;
    char str[100];
    printf("Enter a string : ");
    fgets(str,sizeof(str),stdin);
    while(str[i]!='\0' && str[i]!='\n'){
        char ch=str[i];
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
            vowels++;
        }
        else if(ch>='a'&&ch<='z'||ch>='A'&&ch<='Z'){
            consonants++;
        }
        i++;
    }
    printf("Nnumber of vowels : %d\n",vowels);
    printf("Nnumber of consonants : %d\n",consonants);
    return 0;
}

// 4) Develop a program in C using structures to find the distance between two points.
#include <stdio.h>
#include <math.h>
typedef struct{
    float x,y;
}point;

int main(){
    point p1, p2;
    float distance;
    printf("Enter coordinates of first point (x1,y1) : ");
    scanf("%f%f",&p1.x,&p1.y);
    printf("Enter coordinates of second point (x2,y2) : ");
    scanf("%f%f",&p2.x,&p2.y);
    distance=sqrt((p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y));
    printf("Distance between two points = %.2f",distance);
    return 0;
}

// 5) Develop a program in C using functions and switch case to implement a basic calculator that performs addition, subtraction, multiplication, division, and modulus operations.
#include <stdio.h>
int add(int a, int b){
    return a+b;
}
int subtract(int a, int b){
    return a-b;
}
int multiply(int a, int b){
    return a*b;
}
float divide(int a, int b){
    return (float)a/b;
}
int modulus(int a, int b){
    return a%b;
}

int main(){
    int num1, num2, result, choice;
    float result1;
    printf("Enter two numbers : ");
    scanf("%d%d",&num1,&num2);
    printf("===== Basic Calculator =====\n1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Modulus(%%)\n");
    printf("Enter your choice : ");
    scanf("%d",&choice);
    switch (choice){
    case 1:
        result=add(num1,num2);
        printf("Addition : %d + %d = %d",num1,num2,result);
        break;
    case 2:
        result=subtract(num1,num2);
        printf("Subtraction : %d - %d = %d",num1,num2,result);
        break;
    case 3:
        result=multiply(num1,num2);
        printf("Multiplication : %d * %d = %d",num1,num2,result);
        break;
    case 4:
        if(num2!=0){
            result1=divide(num1,num2);
            printf("Division : %d / %d = %.2f",num1,num2,result1);
        }
        else{
            printf("Error : Division by zero is not allowed.\n");
        }
        break;
    case 5:
        if(num2!=0){
            result=modulus(num1,num2);
            printf("Modulus : %d %% %d = %d",num1,num2,result);
        }
        else{
            printf("Error : Modulus by zero is not allowed.\n");
        }
        break;
        
    default:
        printf("Enter valid choice.\n");
        break;
    }
    return 0;
}