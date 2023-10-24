import argparse


def greet(name):
    """Returns a greeting for a given name."""
    return f"Hello, {name}!"


def sum_of_squares(n):
    """Returns the sum of squares of numbers up to n."""
    return sum(i**2 for i in range(n + 1))


def is_even(n):
    """Determines if a number is even."""
    return n % 2 == 0


def main():
    parser = argparse.ArgumentParser(
        description="A fun script for greeting and doing some math!"
    )

    parser.add_argument(
        "--name", type=str, help="The name you want to greet.", required=True
    )
    parser.add_argument(
        "--number",
        type=int,
        help="A number to compute the sum of squares up to.",
        required=True,
    )

    args = parser.parse_args()

    print(greet(args.name))
    print(f"The sum of squares up to {args.number} is {sum_of_squares(args.number)}.")

    if is_even(args.number):
        print(f"{args.number} is even!")
    else:
        print(f"{args.number} is odd!")


if __name__ == "__main__":
    main()
