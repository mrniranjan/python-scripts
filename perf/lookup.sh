#//Lookup users to fill the memcache
declare -i LOOKUP_MAX
LOOKUP_MAX=500
MEMCACHE_TIMEOUT=600
DATA_DIR="/root/group_${LOOKUP_MAX}_5"
LOOKUP_TIME_DATA="$DATA_DIR/getent_group_results.txt"
MEMCACHE_FULL_TIME="$DATA_DIR/memcache_full_group.txt"
MEMORY_CACHE_TRACE_DIR="$DATA_DIR/memory_cache"
LDB_CACHE_TRACE_DIR="$DATA_DIR/ldb_cache"

mkdir -p $DATA_DIR
mkdir -p $MEMORY_CACHE_TRACE_DIR
mkdir -p $LDB_CACHE_TRACE_DIR

	for i in `seq 1 $LOOKUP_MAX`
	do	
		IDM_GID=$i
		{ time getent group idmgroup$IDM_GID 1> /dev/null 2> time.stderr; } 2> /tmp/time.txt
		echo -e "group is idmgroup${IDM_GID}-first for loop"
		MAX_GID=`expr $i - 1`
		for j in `seq 1 $MAX_GID`
		do 
			echo -e "i = $i"
			echo -e "j = $j"
			echo -e "group is idmgroup${j}-second for loop"
			STRACE_FILE_NAME="$MEMORY_CACHE_TRACE_DIR/idmgroup${j}.trace"
			strace -fxvto $STRACE_FILE_NAME getent group idmgroup${j} 1> /dev/null
			NSS=$(grep  "/var/lib/sss/pipes/nss" $STRACE_FILE_NAME)
			if [[ ! -z $NSS ]]; then
				echo "!!!!!!!!!!!MEMCACHE IS FULL FOR idmgroup${j}!!!!!!!!!"
				echo "idmgroup${j} $(date)" >> $MEMCACHE_FULL_TIME
				mv -f $STRACE_FILE_NAME $LDB_CACHE_TRACE_DIR
				exit 1
			fi		
		done
		LOOKUP_TIME=$(cat /tmp/time.txt | grep real | awk -F " " '{print $2}')
		echo "idmgroup$IDM_GID	 $LOOKUP_TIME   $(date) " >> $LOOKUP_TIME_DATA
	done
