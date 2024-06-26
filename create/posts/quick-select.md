ID="87070"
TITLE="Quick Select Makes Sense"
LINK="quick-select-eurkea"
IS_DRAFT=F
IS_POPULAR=F
----------

I was studying for an exam and came upon this question 

>  Design an algorithm for finding the k-th smallest element in an unsorted array of length n that is faster than O(n log n) amortized. Analyse the complexity of your algorithm assuming k as a constant. (5 marks)

This really stumped me, I couldn't figure out how do this in *less than* O(n * log(n)) time. But now after researching, I know. And I think the algorithm is pretty cool. So for your enjoyment and my retention here it is. 


We can use ***Quick Select*** to find the K-th smallest element in an unsorted array in average linear O(n) time. 

### Here's the steps to the algo

You pick a random element to partition. For simplicity sake I will just always select the last element in the array but in order to achieve the average complexity of o(n) you're going to be better off choosing random elements. 

The goal of the partition is to adjust the array so every element greater than the element you selected is to the left of the array and every element greater than or equal to the element is to the right. 

The way this works is by using two pointers initially both set to the first index of the array and increment the one of the pointers, (the j one in the graph below) at every step. Every time we increment J we are looking if the J element is greater than the partition. If it is then we swap j with wherever i is and increment i as well. We do this until we are at the partition. When we are at the partition element we swap it with wherever i currently is. Here's a visual example I drew up. (note the Exalidraw skillz). 

<img src="/images/quick-select/graph1.png" alt="graph1">


Obviously it's pretty unlikely that we find the correct index at the first element. But what we do know after the first element is that all elements to the left of wherever the partition ended up are less than the element and all elements greater than the partition are to the right. So we can just call the function recursively on either the right or left side of the array and do so repeatedly until the index where the element ended up is correct to the k-th smallest element (with 0-based indexing this is just going to be k-1). 

### Time complexity 

The worst case time complexity of the algorithm is going to occur when we repeatedly pick the largest or smallest element unsorted elements as the pivot, leading to one partition having n-1 elements and the other partition having 0 elements. As then we are going to have to sort the entire array to find our answer. 

  T(n) = T(n-1) + cn <br>
  = T(n-1) + T(n-2) + cn + c(n-1) <br>
  = T(n−2)=T(n−3)+c(n−2)
  *we can observe a general pattern in the expansions* 
  = T(n)=T(n−k)+c(n−k+1)+c(n−k+2)+…+cn
  *which can be summarised as* 
  = T(n)=T(1)+c⋅* ((n(n+1)) / 2 )
  = O(n<sup>2</sup>)


If you haven't seen this notation before T(n) is the time to solve the problem for an array of size n, and T(n-1) is the time to solve the problem for an array of size T(n-1), which is now the case since this is the side of the partition we are going to look at next. Here `cn` represents the linear time (c for constant) to partition the array of size n. Expanding and summarising the recurrence relation shows that the worst case time complexity is going to be quadratic O(n<sup>2</sup>). This is obviously unlikely though as we would have to continuously choose the worst options. 

The best case occurs when we partition the list into two roughly equal halves and continue with half the array.

  T(n) = T(n/2) + cn <br>
  = T(n/4) + c(n/2) + cn <br>
  = n (1 + 1/2 + 1/4 + ...) <br>
  = 2n <br>
  = O(n)


The average case (and thus the amortized complexity) of quick select can be shown to be O(n) (linear time) as we will partition log(n) times on average.

  T(n) = T(n/2) + O(n)


Solving this recurrence relation:

  T(n) = T(n/2) + cn <br>
  = T(n/4) + c(n/2) + cn <br>
  = T(n/8) + c(n/4) + c(n/2) + cn <br>
  = ... <br>
  = T(1) + c(n + n/2 + n/4 + ...)

The sum inside the parentheses is a geometric series:

  n + n/2 + n/4 + ... = 2n

which will sum up to:
 
  T(n) = O(n)

Showing that on average quick select takes linear time, super cool.



### Here's the python implementation ^_^ 

```python

# The code for the partition

def partition(arr, l, r):
  # for simplicity we will set the partition to the last element in the array
  pivot = arr[r]
  # set i to the leftmost element of the current partition
  i=l
  # increment j one step at a time
  for j in range(l,r):
    # if the current element is less than the pivot we need to swap it with i and increment i
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i+=1
  # once we are at the partition element we swap it with wherever i currently is
  arr[i], arr[r] = arr[r], arr[i]
  # return the index of the parition element (that is now in its correct spot)
  return i


def quick_select(arr, l, r, k):
  # partition relevant part of the array
  pivot = partition(arr, l, r)
  # if the pivot is in the correct spot return the element
  if pivot == (k-1):
    return arr[pivot]
  
  # if its greater than then we need to look at the left hand side of k
  if pivot > (k-1):
    return quick_select(arr, l, pivot-1,k)
  # else we need to check the right hand side
  else:
    return quick_select(arr,pivot+1,r,k)

```


[Very Useful video](https://www.youtube.com/watch?v=AqMiMkPOutQ&ab_channel=CSRobot) (whose code I stole and explains this far better than I do)  

