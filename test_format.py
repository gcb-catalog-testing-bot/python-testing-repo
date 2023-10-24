def greet(name: str) -> str:
    if name:
        greeting = 'Hello, ' + name + '!'
    else:
            greeting = 'Hello, World!'
    return greeting