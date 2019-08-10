from webcrawl.bugsmusic import BugsCrawler

if __name__ == '__main__':
    print('a. 국회 크롤링:\n')
    print('b. 벅스 크롤링:\n')
    print('0. 종료')
    bm = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=10')
    bm.scrap()