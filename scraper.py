from bs4 import BeautifulSoup

# value of 0 means <->, 1 means only follower, -1 means only following
names = {}
followers = 0
following = 0


def scrape_html(file):
    global followers
    global following
    with open(file) as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')

        try:
            follower_container = soup.find('div', class_='_aano').div.div
            user_containers = follower_container.find_all('div', recursive=False)
            for user_container in user_containers:
                name_container = user_container.div.div.div.div.find_next_sibling('div')
                name_element = name_container.div.div.div.div.div.a.div.div.span
                name_string = name_element.text
                if file == './input/followers.html':
                    followers += 1
                    names[name_string] = 1
                elif file == './input/following.html':
                    following += 1
                    if name_element.text in names:
                        names[name_string] = 0
                    else:
                        names[name_string] = -1
                else:
                    raise IOError("Incorrect file provided as input.")

        except AttributeError:
            print("Invalid file provided as input")


scrape_html('./input/followers.html')
scrape_html('./input/following.html')
# dictionary is ready to be analyzed...

print(f'Followers: {followers}')
print(f'Following: {following}')

with open('./output/statistics.txt', 'w') as file:
    file.write(f'Followers: {followers}\n')
    file.write(f'Following: {following}\n')

with open('./output/following_you', 'w') as file:
    for name, num in names.items():
        if num == 1:
            file.write(f'{name}\n')

with open('./output/you_follow', 'w') as file:
    for name, num in names.items():
        if num == -1:
            file.write(f'{name}\n')

print("Done scraping.")
