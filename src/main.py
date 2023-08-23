from service import TransferWindowService

#This call is used for transfer of player from transfer pool to a club
#First argument is club intrested and second argument is name of the player in pool
twindow = TransferWindowService()
transfer_news = twindow.transfer_player("Liverpool", "Pogba")
print(transfer_news)


