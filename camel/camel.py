camel = input("camelCase: ");
snake = camel;

upper = []
for i in range(len(camel)):
    if camel[i].isupper():
        snake = snake.replace(camel[i], f"_{camel[i].lower()}")

print("snake_case:", snake);