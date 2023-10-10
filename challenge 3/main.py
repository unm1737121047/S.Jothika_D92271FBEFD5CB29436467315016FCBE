def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices

# example usage :
product=["shoes"," boot","loafer","shoes","sandal","shoes"]
target="shoes"
target='apple'
result = linearsearchproduct(product, target)
print(result)

l1=['shoes','cars','laptop']
for i,j in enumerate(l1):
  print(i,j)

                           
   