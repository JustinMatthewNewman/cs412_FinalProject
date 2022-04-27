# Running exact solution tests
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_1.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_2.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_3.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_4.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_5.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_6.txt
python3 exact_solution/cs412_exact.py < exact_solution/test_cases/test_7.txt

# Running approximate solution tests
echo 'Approx Solution'
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_1.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_2.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_3.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_4.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_5.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_6.txt
python3 approximation_solution/cs412_approx.py < exact_solution/test_cases/test_7.txt
