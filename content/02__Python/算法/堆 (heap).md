tags:[算法]

### 堆 (heap)

数据结构中的堆跟平时我们讲的内存的堆还是有点区别的。数据结构中的堆其实是**利用完全二叉树的结构来维护一组数据**。



#### 完全二叉树

**若设二叉树的深度为h，除第h层外，其它各层(1～h-1)的结点数都达到最大个数，第h层所有的结点都连续集中在最左边，这就是完全二叉树**

个人理解就是铺满的感觉。



#### 堆的分类

一般我们把堆分为**大根堆**与**小根堆**，**也称最大堆，最小堆。**顾名思义，就是堆的每个节点都大于它的子孙节点称为大根堆，堆的每个节点小于他的左右子孙节点称为小根堆。

这里，兄弟之间并没有大小关系，只跟父节点有大小关系。

![](http://claymore.wang:5000/uploads/big/21fa4f140a9f138288ce77d7ae761935.png)

#### 实现一个堆

因为堆是一颗完全二叉树，所以，我们可以用**数组**来实现一个堆。

完全二叉树中，对于每一个节点，如果它的下标为i,

1.父结点索引：(*i*-1)/2（这里计算机中的除以2，省略掉小数）

2.左孩子索引：2**i*+1

3.右孩子索引：2**i*+2

![](http://claymore.wang:5000/uploads/big/15f8543219dbcf07c63fc576a0e53cec.png)

### 堆的操作

堆的几个基本操作：
 1. **上浮 shift_up；**

    **从当前结点开始，和它的父亲节点比较，若是比父亲节点来的小，就交换，**

    **然后将当前询问的节点下标更新为原父亲节点下标；否则退出**

 2. **下沉 shift_down**

    **让当前结点的左右儿子(如果有的话)作比较，哪个比较小就和它交换，**

    **并更新询问节点的下标为被交换的儿子节点下标，否则退出。**

 3. **插入 push**

    **其实很简单，每次插入的时候呢，我们都往最后一个插入，让后使它上浮。**

 4. **弹出 pop**

    **让根节点元素和尾节点进行交换，然后让现在的根元素下沉就可以了**

 5. **取顶 top**

    **返回堆[ 1 ]**

 6. **堆排序 heap_sort**



### 堆排序

堆排序的时间复杂度O(N*logN),额外空间复杂度O(1)，是一个不稳定性的排序

**基本思想：**

1.首先将待排序的数组构造成一个大根堆，此时，整个数组的最大值就是堆结构的顶端

2.将顶端的数与末尾的数交换，此时，末尾的数为最大值，剩余待排序数组个数为n-1

3.将剩余的n-1个数再构造成大根堆，再将顶端数与n-1位置的数交换，如此反复执行，便能得到有序数组

具体：https://blog.csdn.net/u010452388/article/details/81283998

```python
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
```



floor() 返回数字的下舍整数,



### 堆排序的稳定性

堆排序是不稳定的算法，它不满足稳定算法的定义。它在交换数据的时候，是比较父结点和子节点之间的数据，所以，即便是存在两个数值相等的兄弟节点，它们的相对顺序在排序也可能发生变化。

**算法稳定性 -- 假设在数列中存在a[i]=a[j]，若在排序之前，a[i]在a[j]前面；并且排序之后，a[i]仍然在a[j]前面。则这个排序算法是稳定的！**

 



### **堆的应用**

- 二叉堆通常被用来实现堆排序算法，堆排序可以`sort in place`，堆排序的时间复杂度的上界是`O(nlogn)`，是一种很优秀的排序算法。由于存在相同键值的两个元素处于两棵子树中，而两个元素的顺序可能会在后续的堆调整中发生改变，因此堆排序不是稳定的。降序排序需要建立小顶堆，升序排序需要建立大顶堆。

-  优先级队列:与普通队列的先进先出不同，这种队列插入和删除时取决于元素的优先级 ，这是一种非常有用的队列。操作系统就是使用这样一种数据结构来表示一组任务。而用堆实现同有序序列和无序序列相比，在插入和删除（或者叫提取）的效率上比较折中。

     优先队列有3个常用的函数：

     （1） 取最大（小）优先级的元素，其时间复杂度为 O（1）

     （2） 插入新的元素，过程相当于插入堆尾，然后进行堆调整。只是这里不需要重新做一遍建堆过程，而是从新插入的元素沿着它的父节点一直到根节点这 log（n+1)个节点。因此其时间复杂度为：

        T(n) = log(2,n+1) + (log(2,n+1)-1) + ... +2 + 1 
     
               = (1+log(2,n+1))* log(2,n+1)/2
          
               = (log(2,n+1)+1/2)^2 / 2 -1/8
          
               ≈ log(2,n+1)^2 /2  
     
       粗略计算的可以认为是：log(2,n)     

    （3）出去最大元素，并调整，这个时间复杂度就是 log(2,n)  

- 堆的另一个应用就是在海量数据中找到TopK个数，思想是维护一个大小为K的二叉堆，然后不断地比较堆顶元素，判断是否需要执行替换对顶元素的操作，采用
  此方法的时间复杂度为`n*logk`，当`k`和`n`的数量级差距很大的时候，这种方式是很有效的方法。

- 寻找M个数中的前K个最小的数并保持有序

  这里我们使用最大堆来解决：

  1. 用M个数里面的前K个数创建一个K个元素的最大堆。

  2. 将第M-k个数到第M个数依次和上面最大堆的第一个元素（存储这个最大堆的第1个数据，也即是抽象的完全二叉树的根结点数据）比较，如果大于等于堆顶元素，继续下一个数进行比较（堆顶元素在最大堆中最大），如果小于堆顶元素，就把堆顶元素值设置为这个数，然后重新对这个堆进行重新最大堆化，使之符合最大堆的要求。

  3. 结束之后最大堆里面放的就是最小的K个数了，这时对最大堆进行堆排序，就解决这个问题了。