for var in `seq 1 500`; do
curl http://127.0.0.1:8000/ > /dev/null 2>&1 &
done
wait