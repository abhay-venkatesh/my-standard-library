from threading import Thread
from queue import Queue

def get_urls(page):
    # returns a list of urls in the web page string
    return ["url_0", "url_1", "url_2"]
    
def get_page(url):
    # returns a string that represents a page pointed at by a url
    return "page"

def write_to_disk(page):
    print(page)
    
class WebCrawler:
    """
    Execution Trace:
    """
    def __init__(self, num_cores=1):
        self.num_cores = num_cores
        self.q = Queue()
        
    def crawler(self):
        while True:
            url, k = self.q.get()
            if k == 0:
                self.q.task_done()
                break
                
            page = get_page(url)
            write_to_disk(page)
            urls = get_urls(page)
            
            urls_k = [(url, k-1) for url in urls]
            for url_k in urls_k:
                self.q.put(url_k)
        
    def crawl(self, url, k=1):
        """
        Begin crawling at url,
        and crawl to a depth of k
        """
        self.q.put((url, k))
        for _ in range(self.num_cores):
            t = Thread(target=self.crawler)
            t.daemon = True
            t.start()
        self.q.join()
        
def main():
    wc = WebCrawler(num_cores=1)
    wc.crawl("yahoo.com", k=1)

if __name__ == '__main__':
    main()