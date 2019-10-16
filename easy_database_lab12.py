##Include func###
import itertools#
##Include func###
################################################## database ##################################################

##database type,amount##
str_m = ['men']
int_m = set('1234')

str_w = ['women']
int_w = set('123456789')
##database type,amount##

##combine type,amount database##
combine_m = list(itertools.product(str_m,int_m))
combine_w = list(itertools.product(str_w,int_w))
##combine type,amount database##

##join ' ' func & get full database##
data_m = set(''.join(loop0) for loop0 in combine_m)
data_w = set(''.join(loop1) for loop1 in combine_w)
##join ' ' func & get full database##

##all person data##
data_allmw = sorted(data_w.union(data_m))
##all person data##

################################################## database ##################################################