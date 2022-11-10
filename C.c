#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

int includes(int array[], int length, int value)
{
  int i;

  i = 0;
  while (i < length)
  {
	if (array[i] == value)
		return (1);
	i++;
  }
  return (0);
}

int *array_copy(int *array, int length)
{
  int   *c;
  int   i;

  i = 0;
  c = malloc(length * sizeof(int));
  if (!c)
	return (0);
  while (i < length)
  {
	c[i] = array[i];
	i++;
  }
  return (c);
}

int *ft_intcat(int *a1, size_t len1, int *a2, size_t len2)
{
  int *new_array;

  new_array = malloc(sizeof(int) * (len1 + len2));
  if (!new_array)
	return (0);
  ft_memcpy(new_array, a1, sizeof(int) * len1);
  ft_memcpy(new_array + len1, a2, sizeof(int) * len2);
  return new_array;
}

int bin_to_dec(char *string)
{
  int slen;
  int total;
  int decval;
  int i;

  decval = 1;
  total = 0;
  slen = strlen(string);
  i = slen - 1;
  while (i >= 0)
  {
	if (string[i] == '1')
		total += decval;
	decval *= 2;
	i--;
  }
  return (total);
}

int binary_search(int a[], int e, int l, int r)
{

  // find the mid-way index between index l and index r
  int mid;

  mid = l + (r - l) / 2;

  // if l is ever > r, it means the element is not in the array
  if (l > r)
  	return (-1);
  // if we've found the element at the mid-way index, return the index
  // else if the element MUST be in the left-portion of the portion of the
  //         array we are currently looking at, search for it in this portion
  // else if the element MUST be in the right-portion of the portion of the
  //         array we are currently looking at, search for it in this portion
  if (a[mid] == e)
    return mid;
  else if (a[mid] > e)
    return binary_search(a, e, l, mid - 1);
  else
    return binary_search(a, e, mid + 1, r);
}

float dot_product(float v1[], float v2[], int length)
{
  float sum;
  int i;

  i = 0;
  sum = 0;
  while (i < length)
  {
	sum += v1[i] * v2[i];
	i++;
  }
  return (sum);
}

int find_min(int array[], int length)
{
  int min;
  int	i;
  int	index;

  index = 0;
  i = 1;
  min = array[0];
  while (i < length)
  {
	if (array[i] < min)
	{
		min = array[i];
		index = i;
	}
	i++;
  }
  return min;
}

void insertion_sort(int a[], int length)
{
  int	i;
  int key;
  int j;

  i = 1;
  while (i < length)
  {
	j = i - 1;
	key = a[i];
    while (j >= 0 && a[j] > key)
    {
      a[j + 1] = a[j];
      j = j - 1;
    }
    a[j + 1] = key;
	i++;
  }
}

bool is_prime(int number)
{
  int i;

  i = 2;
  if (number <= 1)
	return false;
  while (i <= (number / 2))
  {
    if (number % i == 0)
		return false;
	i++;
  }
  return true;
}

