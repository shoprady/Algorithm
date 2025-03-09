s = input()
print(s[1:-1]) if s != '"' and s != '""' and s[0] == '"' and s[-1] == '"' else print('CE')