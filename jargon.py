emails = ['food@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
urls = ['www.a.com', 'www.b.com', 'www.c.com',]

count_email_domains = (emails, urls)

dict_map = {}
domain_list = []

# for item in count_email_domains:
#     # print(item)
#     for email_url in item:
#         print(email_url)
        
# for i in range(len(count_email_domains)):
#     # print(count_email_domains[i])
#     for email_url in count_email_domains[i]:
#         # print(email_url)
#         if '@' in email_url:
#             index = email_url.index('@')
#             index_domain = index + 1
#             # domain = email_url
#             domain = email_url[index_domain]
#             if domain not in domain_list:
#                 domain_list.append(domain)
#             print(index_domain)
#         if (email_url[0:4] == 'www.' and email_url[4] in domain_list):
#             for email in emails:
#                 if '@'
#             dict_map[email_url] = 1
# print(domain_list)
# print(dict_map)

for i in range(len(count_email_domains)):
    emails = count_email_domains[0]
    urls = count_email_domains[1]
    # print(emails, urls)
    for email in emails:
        index = email.index('@')
        domain_index = index + 1
        domain = email[domain_index]
        if domain not in domain_list:
            domain_list.append(domain)
    # for url in urls:
    for i in range(len(urls)):
        print(urls[i])
        if (urls[i][4] == domain_list[i]) and (domain_list[i] in emails[i]):
            # print(emails[i][domain_index])
            # if urls[i][4] == emails[i][domain_index]:
            dict_map[urls[i]] = emails[i]
    
print(domain_list)
print(dict_map)