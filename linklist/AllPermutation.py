def AllPermutation(nums,N,idx,current):
    if(idx == N):
        print(current)
        return
    else:
        for i in range(0,N):
            if(nums[i] not in current):
                current.append(nums[i])
                AllPermutation(nums,N,idx+1,current)
                current.pop()

def AllCombination(nums,N,current,n,idx,prev):
    if(idx == n):
        print(current)
        return
    else:
        for i in range(prev+1,N):
            current.append(nums[i])
            AllCombination(nums,N,current,n,idx+1,i)
            current.pop()

nums = [1,2,3,4,5]
#AllPermutation(nums,len(nums),0,[])
AllCombination(nums,len(nums),[],3,0,-1)