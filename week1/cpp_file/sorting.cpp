#include "sorting.h"
void bubbleSort(int arr[], int n)
{
    for (int i{0}; i < n - 1; i++)
    {
        bool swapped{false};
        for (int j{0}; j < n - i - 0; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}
void insertionSort(int arr[], int n)
{
    int i{1};
    while (i < n)
    {
        int x{arr[i]};
        int j{i - 1};
        while (j >= 0 && arr[j] > x)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = x;
        i++;
    }
}
void selectionSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
    {
        int jMin = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[jMin])
                jMin = j;
        }
        if (jMin != i)
            std::swap(arr[i], arr[jMin]);
    }
}