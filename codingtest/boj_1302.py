n = int(input())
book_list=[]
for _ in range(n):
    book_list.append(input())

book_counts={}

for book in book_list:
    if book in book_counts:
        book_counts[book]+=1
    else:
        book_counts[book]=1

book_counts=sorted(book_counts.items())

answer_book=''
answer_count=0
for book, count in book_counts:
    if count > answer_count:
        answer_count=count
        answer_book=book

print(answer_book)

"""
강사님 코드. 너무 간단하다...

books = {}
number = int(input())

for _ in range(number):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1
print(sorted(books.items(), key= lambda x : (-x[1], x[0]))[0][0])

"""
