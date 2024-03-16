player1 = input("Player 1 memilih :")
player2 = input("Player 2 memilih :")

pilih1 = "batu"
pilih2 = "gunting" 
pilih3 = "kertas"

if player1 == pilih1 and player2 == pilih2:
  print(f"Player 1 menang")
elif player1 == pilih2 and player2 == pilih1:
  print(f"Player 2 menang")
elif player1 == pilih1 and player2 == pilih3:
  print(f"Player 2 menang")
elif player1 == pilih3 and player2 == pilih1:
  print(f"Player 1 menang")
elif player1 == pilih2 and player2 == pilih3:
  print(f"Player 1 menang")
elif player1 == pilih3 and player2 == pilih2:
  print(f"Player 2 menang")
else:
  print(f"Hasil seimbang")