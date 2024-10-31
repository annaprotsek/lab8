def get_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors

def remove_extremes(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    return lst

def main():
    N = int(input("Введіть ціле число N: "))
    divisors = get_divisors(N)
    print(f"Додатні дільники числа {N}: {divisors}")
    updated_divisors = remove_extremes(divisors)
    print(f"Масив після видалення найбільшого та найменшого елементів: {updated_divisors}")

if __name__ == "__main__":
    main()
