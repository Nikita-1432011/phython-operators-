amount=int(input("Enter the Amount for Withdraw:"))

note1= amount // 100
note2 = (amount%100) // 50
note3 = ((amount%100)%50) // 10

print("Notes of 100 rupee:",note1)
print("Notes of 50 rupee:",note2)
print("Notes of 10 rupee:",note3)