
![Quicksort](https://www.bing.com/th?id=OSK.d4e5d0a778dba725091d8317e6bac939&pid=cdx&w=320&h=189&c=7&rs=1)

### Quick Sort

- Quick Sort is a **Divide and Conquer** algorithm.
- It picks an element as **pivot** and partitions the given array around the picked pivot.
- There are many different versions of quickSort that pick pivot in different ways:
    - Always pick first element as pivot.
    - Always pick last element as pivot.
    - Pick a random element as pivot.
    - Pick median as pivot.

#### Example

Consider the array: `10, 80, 30, 90, 40, 50, 70`

- We choose 70 as the pivot. We start from the first element and keep moving until we find an element greater than the pivot, and we also start from the last element and keep moving until we hit an element less than the pivot. If we do find such elements, we swap them.
- After we have finished processing the array, we have two halves of the array such that each element in the first half is less than or equal to the pivot and each element in the second half is greater than the pivot. The pivot is in its final sorted position.
- We then recursively apply the same process to the two halves.

#### Best Case Scenario

- The best case occurs when the partition process always picks the middle element as pivot.
- The complexity in this case is **O(n log n)**.

#### Average Case Scenario

- The average case occurs when the partition process can pick the pivot in a way that it divides the array into two halves.
- The complexity in this case is also **O(n log n)**.

#### Worst Case Scenario

- The worst case occurs when the partition process always picks greatest or smallest element as pivot.
- If we consider a sorted array and we pick the last element as pivot always, then the complexity in this case is **O(n^2n2)**.

### Comparison with Merge Sort

- Merge Sort works better than Quick Sort for larger arrays or lists of data.
- Quick Sort is faster for smaller arrays or lists.
- Merge Sort requires **O(n)** extra space, Quick Sort requires **O(log n)** extra space.
- Merge Sort is a stable sort, unlike Quick Sort.
- Quick Sort is an in-place sort (it doesn’t require any extra storage) whereas merge sort requires **O(N)** extra storage, N denoting the array size which may be quite expensive.
- Implementing Quick Sort is not as straightforward as Merge Sort.