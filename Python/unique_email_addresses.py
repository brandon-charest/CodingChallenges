"""
929. Unique Email Addresses
Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
"""


def num_unique_emails(emails):
    result_set = set()
    for email in emails:
        name, domain = email.split("@")
        name = name.replace(".", "").split("+")[0]
        result_set.add(name + "@" + domain)

    return len(result_set)


email_list = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(num_unique_emails(email_list))
