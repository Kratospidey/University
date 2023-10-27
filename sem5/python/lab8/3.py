users = [
    {"username": "seema", "tweets": ["i love chocolate", "i am a student"]},
    {"username": "arush", "tweets": []},
    {"username": "kumal", "tweets": ["India", "Python"]},
    {"username": "sam", "tweets": []},
    {"username": "lokesh", "tweets": ["i am good"]},
]

inactive_users = list(filter(lambda u: not u["tweets"], users))

inactive_users_upper = list(
    map(lambda u: u["username"].upper(), filter(lambda u: not u["tweets"], users))
)

names = list(
    map(
        lambda name: f"your name is {name.title()}",
        filter(lambda name: len(name) > 4, list(map(lambda u: u["username"], users))),
    )
)

print(inactive_users)
print(inactive_users_upper)
print(names)
