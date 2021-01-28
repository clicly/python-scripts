import requests, json, random, string

subreddits = ['wallstreetbets']
random_str_length = 20
printed_post_number = 15

COLOR_RED  = '\033[31m'
COLOR_GRAY = '\033[37m'
COLOR_CYAN  = '\033[36m'
COLOR_YELLOW  = '\033[33m'
COLOR_PURPLE  = '\033[35m'

class PostSearch:
    STANDARD = '/.json'
    TOP_TODAY = '/top/.json?t=day'
    TOP_WEEKLY = '/top/.json?t=week'
    TOP_MONTHLY = '/top/.json?t=month'
    TOP_YEARLY = '/top/.json?t=year'
    TOP_LIFE = '/top/.json?t=all'

def get_posts(subreddit, search):
    """
    Get prepared post data from reddit api.
    """
    url = f'https://www.reddit.com/r/{subreddit}{search}'
    result = request_api(url,  headers = {'User-agent': generate_random_str(random_str_length)}) # non-default user agent
    return result['data']['children']

def request_api(api_url, headers = None):
    """
    Creates a rest api call to parameter url with error handling.
    """
    r = requests.get(api_url, headers = headers)
    r.raise_for_status()
    return json.loads(r.content)

def print_posts(posts, number):
    """
    Print the specified number of posts from the list to the console.
    """
    for i, post in enumerate(posts[1:number+1]): # will skip first post about subreddit rules
        index = str(i)
        data = post['data']
        title = data['title']
        url = data['url']
        ups = data['ups']
        post_output = f'{COLOR_RED}{index}: [{COLOR_CYAN}{ups}] {COLOR_GRAY}{url} >> {COLOR_PURPLE}{title}'
        print(post_output)

def generate_random_str(str_length):
    """
    Generates a random string with the specified length.
    https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(str_length))

def print_console(obj, color = ''):
    print(F'{color}{obj}')

if __name__ == "__main__":
    for subreddit in subreddits:
        print_console(subreddit.upper(), COLOR_YELLOW)
        search = PostSearch.TOP_LIFE
        posts = get_posts(subreddit, search)
        print_posts(posts, printed_post_number)
