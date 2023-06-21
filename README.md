## Multiprocessing Factorization

This program demonstrates the usage of multiprocessing to perform factorization of numbers in parallel. The `factorize` function takes a variable number of arguments, which are the numbers to be factorized. It calculates all the factors of each number and returns a list of factors for each input number.

### Usage

To use this program, you need to have Python installed on your system. Follow these steps:

1. Clone the repository or download the files.

2. Install the required dependencies by running the following command in the project directory:
   ```
   pip install -r requirements.txt
   ```

3. Open the `factorization.py` file in a text editor and uncomment the lines inside the `if __name__ == '__main__':` block. Comment out the last line of the file that invokes the `factorize` function directly.

4. Save the file and run it using the following command:
   ```
   python factorization.py
   ```

5. The program will calculate the factors of the provided numbers using multiprocessing. The output will be displayed in the console.

### Explanation

This program utilizes the `multiprocessing` module in Python to perform factorization in parallel using multiple processes. Here's a brief explanation of the key components:

- The `factorize` function calculates the factors of the input numbers using a nested loop. It stores the factors in a list and appends the result to the `result` list.

- The `if __name__ == '__main__':` block ensures that the code inside it is only executed when the script is run directly, not when it is imported as a module.

- The `Pool` class from the `multiprocessing` module is used to create a pool of worker processes. The number of processes is determined by `cpu_count()`, which returns the number of available CPU cores.

- The `map` method of the `Pool` class is used to apply the `factorize` function to each element of the input list in parallel. It divides the input list into chunks and assigns each chunk to a worker process for processing.

- The results of the `factorize` function for each input number are collected in the `r` list. The order of the results is preserved.

- The total execution time of the multiprocessing approach is printed at the end of the program.

### Notes

- The commented-out lines at the end of the file demonstrate the direct usage of the `factorize` function without multiprocessing.

- The code also includes commented-out lines for a callback function. This can be used to process the results of each worker process as soon as it completes. Uncomment those lines if you want to use the callback mechanism.

- The performance improvement achieved by multiprocessing depends on the number of CPU cores available and the nature of the calculations being performed. In some cases, the overhead of inter-process communication may outweigh the benefits of parallelization.

- This program serves as a basic example of multiprocessing in Python. Feel free to modify and extend it according to your requirements.

Enjoy parallel factorization with multiprocessing!
