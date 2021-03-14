def solution(phone_book):
    phone_book.sort() #[0],[1] 0~9까지 순으로 되어있다. 즉 91,19 가 있으면 19 ,91/ 148과 14 가있으면 14,148
    for i in range(len(phone_book)-1):
        if  phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
    return True