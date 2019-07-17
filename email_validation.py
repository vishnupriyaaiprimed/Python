import re

def fun(s):
    match=re.match(r'^[a-zA-Z0-9]+([-_][a-zA-Z0-9]*)*@[a-zA-Z0-9]+\.[a-z]{1,3}$',s)

    if match:
        return True
    else:
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
