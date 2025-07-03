def hello_user(name: str) -> None:
    message = f"Hello, {name}! Welcome to the 21-day Python challenge."
    print(message)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    hello_user(user_name)