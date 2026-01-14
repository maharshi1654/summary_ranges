nums=[0,1,2,4,5,7]
l=[]
a=0
if not nums:
    print(l)
    exit()
for i in range(1,len(nums)):
    if (nums[i]-nums[i-1])!=1:
        if a==i-1:
            l.append(f"{nums[a]}")
            a=i
        else:   
            l.append(f"{nums[a]}->{nums[i-1]}")
            a=i
    else:
        continue
if a==len(nums)-1:
    l.append(f"{nums[a]}")
else:
    l.append(f"{nums[a]}->{nums[len(nums)-1]}")
print(l)