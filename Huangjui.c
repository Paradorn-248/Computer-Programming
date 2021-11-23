#include<stdio.h>
int main()
{
    int i,j,column,row;
    float sum;
    float minccw = 9999999,mincw = 9999999;
    printf("Input row : ");
    scanf("%d" , &row);
    printf("Input column : ");
    scanf("%d" , &column);
    float area[row][column], price1,price2,price3 ; 
    for (i = 0 ; i < row ; i++)
    {
        for (j = 0 ; j < column ; j++)
        {
            scanf("%f" , &area[i][j]);
        }
    } 
    for (i = 0 ; i < row - 1 ; i++) //clockwise
    {
        for (j = 0 ; j < column - 1 ; j++)
        {
            price1 = area[i][j + 1] * 1.1 ; 
            price2 = area[i + 1][j] * 1.1 * 1.1; 
            price3 = area[i + 1][j + 1] * 1.1;
            sum = area[i][j] + price1 + price2 + price3;
            //printf("%.2f\n",sum);
            if (sum < mincw)
            {
                mincw = sum ;
            }
        }
    }
    // printf("%.2f\n" , mincw);
    for (i = 1 ; i < row ; i++) //counterclockwise
    {
        for (j = 0 ; j < column - 1 ; j++)
        {
            price1 = area[i][j + 1] * 1.1 ; 
            price2 = area[i - 1][j] * 1.1 * 1.1; 
            price3 = area[i - 1][j + 1] * 1.1;
            sum = area[i][j] + price1 + price2 + price3;
            // printf("%.2f\n",sum);
            if (sum < minccw)
            {
                minccw = sum ;
            }
        }
    }
    //printf("%.2f\n" , minccw);
    if(mincw < minccw)
    {
        printf("%.2f\n", mincw);
    }
    else
    {
        printf("%.2f\n",minccw);
    }
}

//คิดได้แล้วค้าบบบบ เย่ๆๆๆ