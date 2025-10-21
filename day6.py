blog_views=[150,800,2500,600,1200,450,3000]
trending=0
total_views=0

for x in blog_views:
    if x>1000:
        print("Trending")
        trending+=1
    elif x>500 and x<1000:
        print("Average")
    else:
        print("Low Traffic")
    total_views+=x    



print("Total blog views:",total_views)
print("Number of trending blogs:",trending)