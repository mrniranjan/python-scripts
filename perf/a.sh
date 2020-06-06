declare -i LOOKUP_MAX
LOOKUP_MAX=500
for i in `seq 1 $LOOKUP_MAX`
do 
   echo "i = $i"
   max=`expr $i - 1`
   for j in `seq 1 $max`
   do 
	   echo "j = $j"
   done
done   

