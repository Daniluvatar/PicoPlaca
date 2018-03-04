# PicoPlaca
This is a "pico y placa" predictor implemented using Python3. To make the program work, just run the *predict_picoplaca.py* script in your favorite IDE or in the command prompt just type:

```shell
$python predict_picoplaca.py
```

The program will ask you to enter the plate number, date and time and it will inform you whether or not that car can be on the road.

To implement the program a *test-driven development* (TDD) approach was used. Therefore, you can check the unit tests on the folder **tests**.

You can also run the unit tests in any of your favorite IDE, just make sure you have *unittest* (https://docs.python.org/3/library/unittest.html) API installed. 
To run the test on the command prompt, for example if you want to run the script test *test_restrictionDay.py*. Just type the following in the terminal:

```shell
$python -m unittest -v tests.test_restrictionDay
```

The command above, will show you the results of the test directly on the terminal in a verbose way.
