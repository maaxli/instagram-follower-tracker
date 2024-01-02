from bs4 import BeautifulSoup

# value of 0 means <->, 1 means only follower, -1 means only following
names = {}


def scrape_html(file):
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
                    names[name_string] = 1
                elif file == './input/following.html':
                    if name_element.text in names:
                        names[name_string] = 1
                    else:
                        names[name_string] = -1
                else:
                    raise IOError("Incorrect file provided as input.")

        except AttributeError:
            print("Invalid file provided as input")


scrape_html('./input/followers.html')
scrape_html('./input/following.html')
# dictionary is ready to be analyzed



print("Done scraping.")
