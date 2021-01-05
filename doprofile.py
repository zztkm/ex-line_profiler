import fizzbuzz
import line_profiler


def main():

    pr = line_profiler.LineProfiler()

    pr.add_function(fizzbuzz.fizzbuzz)
    pr.runcall(fizzbuzz.main)

    pr.print_stats()


if __name__ == "__main__":
    main()
