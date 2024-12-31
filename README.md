# josephus-problem
Implementation of the Josephus problem in Python

Josephus problem

Josephus was one of 41 Jews who were trapped in a cave. Instead of surrendering, this group decided to commit suicide. They all agreed that every second person among the living would kill themselves, and the order would continue until only one person remained. However, Josephus, being bigger and cleverer than the others, calculated where to sit and how to avoid being killed from the start.

Problem in General: If there are n people numbered from 1 to n standing in a circle and starting from number 1, every time the next person kills themselves, which position will the last remaining person hold?

Suicide Sequence for n=5

1, 2, 3, 4, 5 ⇒ 1, 3, 4, 5 ⇒ 3, 5 ⇒ 3

Suicide Sequence for n=6

1, 2, 3, 4, 5, 6 ⇒ 1, 3, 5 ⇒ 5, 1, 3 ⇒ 1, 5 ⇒ 5


مساله ژوزفوس

ژوزفوس یکی از ۴۱ پیودی ای بود که به وسیله در یک غار محاصره شده بودند. به جای تسلیم، این گروه تصمیم گرفتند که همگی خودکشی کنند. آنها قرار گذاشتند تا نفر دوم زنده ها خود را بکشند و نوبت به نفر زنده باقی بماند. ولی ژوزفوس بزرگتر از آنها بود و مکان نشستن آخری فردی را که باید خودکشی می کرد و از محاسبه کرد و از ابتدا در مکان نشسته جان سالم برد.

مسئله در حالت کلی: اگر n نفر با شماره های ۱ تا n در دایره ای قرار بگیرند و به شروع از شماره ۱، هر بار یکی نفر زنده خود را بکشند، آخرین نفر چه شماره ای دارد؟


نسبت خودکشی برای n=5
1, 2, 3, 4, 5 ⇒ 1, 3, 4, 5 ⇒ 3, 5 ⇒ 3

نسبت خودکشی برای n=6 
1, 2, 3, 4, 5, 6 ⇒ 1, 3, 5 ⇒ 5, 1, 3 ⇒ 1, 5 ⇒ 5


```
def josephus(n, k):  
    if n == 1:  
        return 0  
    
    return (josephus(n - 1, k) + k) % n  

n = int(input("Enter the number of people (n): "))  
k = 2  

position = josephus(n, k) + 1  
print(f"The safe position is {position}")
