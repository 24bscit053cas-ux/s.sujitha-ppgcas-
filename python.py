items=["Shirt","Shoes","Watch","Bag","Cap"]
prices=[500,1200,800,650,300]
total = 0
item_count=0
print("="*35)
print("SHOPPING BILL RECEIPT")
print("="*35)
for i in range(len(items)):
  total += prices[i]
  item_count += 1
  print(f"{item_count}.{items[i]:}<10)-Rs.{prices[i]}")
print("-"*35)
print(f"Total items:{item_count}")
print(f"Subtotal:Rs.{total}")
if total>=3000:
  discount_percent=20
elif total>=2000:
  discount_percent=10
elif total>=1000:
  discount_percent=5
else:
  discount_percent=0
  discount_amount=(total * discount_percent)/100
  final_amount=total-discount_amount
  print(f"discount applied:{discount_percent}%")
  print(f"discount amount:Rs.{discount_amount}")
  print(f"final amount to pay:Rs.{final_amount}")
  print("-"*35)