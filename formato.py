yes_votes=42
no_votes=43
percentuale = yes_votes / (yes_votes + no_votes) 
s='{:-9} yes votes {:2.2%}'.format(yes_votes, percentuale)
print(s)
