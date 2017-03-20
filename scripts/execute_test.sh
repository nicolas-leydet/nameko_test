run_test()
{
	nb_service=$1
	nb_worker=$2
	delay=$3
	nb_calls=$4 

	echo "nb_service: $nb_service, nb_worker: $nb_worker, delay: $delay, nb_calls: $nb_calls" >> nameko_test_results.txt

	for i in $(seq 1 $nb_service); do
		python nameko_test/service.py --workers ${nb_worker} --delay ${delay}&	
	done
		
	sleep 2

	python nameko_test/client.py --calls ${nb_calls} >> nameko_test_results.txt 

	killall python
}


echo '------------' >> nameko_test_results.txt

run_test 1 10 0.01 100
run_test 1 20 0.01 100
run_test 1 50 0.01 100
run_test 1 100 0.01 100

run_test 1 10 0.01 100
run_test 2 10 0.01 100
run_test 3 10 0.01 100
run_test 5 10 0.01 100

run_test 1 10 0.01 100
run_test 1 10 0.02 100
run_test 1 10 0.05 100
run_test 1 10 0.10 100

run_test 1 20 0.05 100
run_test 1 30 0.05 100
run_test 1 50 0.05 100
run_test 1 100 0.05 100

run_test 2 10 0.05 100
run_test 3 10 0.05 100
run_test 4 10 0.05 100
run_test 5 10 0.05 100


run_test 1 10 0.0 50
run_test 1 10 0.0 500
run_test 1 10 0.0 1000

