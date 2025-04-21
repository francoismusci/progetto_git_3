yes_votes=42
no_votes=43
percentuale = yes_votes / (yes_votes + no_votes) 
s='{:-9} yes votes {:2.2%}'.format(yes_votes, percentuale)
print(s)



m_s=30
k=3.6 
km_h=m_s*k
suffisso="km/h"
print("la velocità misurata e' pari a {} {}".format(km_h,suffisso))


j=3.6
km_h1=40
m_s1=km_h1/j

print("la velocità misurata  e\' pari a {:.2f} in m/s".format(m_s1))

