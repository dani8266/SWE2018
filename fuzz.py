from fuzzing.fuzzer import FuzzExecutor

file = ["python rle.py -e".replace(" ","&")]

testfile = ["fuzztests.txt"]

number_of_runs = 20

def test():
    print("start test")
    fuzz_executor = FuzzExecutor(file,testfile)
    fuzz_executor.run_test(number_of_runs)
    print("Tests finished")
    return fuzz_executor.stats

def main():
    print("hello")
    stats = test()
    print(stats)

if __name__ == "__main__":
    main()
