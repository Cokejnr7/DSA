from typing import List,Any

# with loops
def reverse_array(arr:List[Any]) -> List[Any]:
    low:int = 0
    high:int = len(arr) - 1
    
    while low != len(arr)//2:
        arr[low], arr[high] = arr[high], arr[low]
              
        low += 1
        high -= 1 
        
    return arr

# with recursion
def reverse_with_recursion(arr:List[Any], low:int, high:int) -> List[Any]:
    
    if low != len(arr)//2:
        arr[low], arr[high] = arr[high], arr[low]
        reverse_with_recursion(arr, low + 1 , high - 1)

    return arr
   
    

if __name__ == '__main__':
    shop_list = ['earphones', 'jump ropes', 'boxing gloves', 'essentials']
    print(reverse_with_recursion(shop_list, 0, len(shop_list) - 1))