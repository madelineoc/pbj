pbj-new
=======

playtime 1

pb = 30 
jelly = 0   
bread = 41
if (bread % 2) != 0 and pb > 0 and jelly > 0:
    print "You can make an open-faced sandwich"

if bread >= 2 and pb >= 1 and jelly == 0:
    print "you can make a peanut butter sandwich, but you should take a hard look at your life"

if bread >=2 and jelly >=1 and pb >=1:
    print "You can have a peanut butter and jelly sandwich"
elif jelly < 1:
    print "you need more jelly"
elif pb < 1:
    print "you need more peanut butter"
elif bread < 2:
    print "you need more bread"
    
if bread >=2 and jelly >=1 and pb >=1 and bread <= (2 * pb) + 1 and bread <= (2 * jelly) + 1:
    print "you can make {0} sandwiches".format(bread/2)
elif bread >=2 and jelly >=1 and pb >=1 and jelly <= pb:
    print "you can make {0} sandwiches".format(jelly)
elif bread >=2 and jelly >=1 and pb >=1 and pb <= jelly:
    print "you can make {0} sandwiches".format(pb)
