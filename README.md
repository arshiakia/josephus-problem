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
```
Recursion relation of Josephus' problem

The recursive relation for the Josephus Problem helps us determine the position of the surviving person in a circle of \( n \) people, where every \( k^{th} \) person is eliminated. The relation is expressed as:

\[
J(n) = (J(n-1) + k) \mod n
\]

Explanation:
- \( J(n) \)**: The position of the survivor among \( n \) people.
- \( J(n-1) \)**: The position of the survivor among \( n-1 \) people.
- \( k \)**: The number of people to be eliminated.
- \( \mod n \)**: Ensures that the result remains within the range of \( 0 \) to \( n-1 \).

Base Case:
- For one person:
  \[
  J(1) = 0
  \]

Using this relation, we can calculate the position of the survivor for any number of participants. For example, with \( n = 5 \) and \( k = 2 \), we can find out that the survivor is in a specific position.

<p style="text-align: right;">  
رابطه بازگشتی مساله ژوزفوس به ما کمک می‌کند تا موقعیت فرد نجات‌یافته در یک دایره از ( n ) نفر را محاسبه کنیم، در حالی که هر ( k^{ام} ) نفر حذف می‌شود. این رابطه به شکل زیر است:  

[ J(n) = (J(n-1) + k) \mod n ]  

توضیحات:  
( J(n) ): موقعیت نجات‌یافته در میان ( n ) نفر.  
( J(n-1) ): موقعیت نجات‌یافته در میان ( n-1 ) نفر.  
( k ): تعداد نفراتی که باید حذف شوند.  
( \mod n ): می‌زند که نتیجه در بازه ( 0 ) تا ( n-1 ) باقی بماند.  
پایه:  
برای یک نفر: [ J(1) = 0 ]  
با استفاده از این رابطه، می‌توان موقعیت نجات‌یافته را برای هر تعداد نفر محاسبه کرد. برای مثال، با ( n = 5 ) و ( k = 2 )، می‌توان پی برد که فرد نجات‌یافته در موقعیت خاصی قرار دارد.  

بیایید یک مثال با ( n = 5 ) نفر و ( k = 2 ) بزنیم، به این معنی که هر دومین نفر حذف می‌شود.  

مقدمه: [ J(1) = 0 ] (برای یک نفر، او نجات‌یافته است)  

برای ( n = 2 ): [ J(2) = (J(1) + 2) \mod 2 = (0 + 2) \mod 2 = 0 ] (یعنی نفر اول نجات می‌یابد)  

برای ( n = 3 ): [ J(3) = (J(2) + 2) \mod 3 = (0 + 2) \mod 3 = 2 ] (یعنی نفر سوم نجات می‌یابد)  

برای ( n = 4 ): [ J(4) = (J(3) + 2) \mod 4 = (2 + 2) \mod 4 = 0 ] (یعنی نفر اول نجات می‌یابد)  

برای ( n = 5 ): [ J(5) = (J(4) + 2) \mod 5 = (0 + 2) \mod 5 = 2 ] (یعنی نفر سوم نجات می‌یابد)  

نتیجه:  
بنابراین، در یک دایره از 5 نفر که هر دومین نفر حذف می‌شود، فرد نجات‌یافته در موقعیت ( J(5) + 1 = 3 ) قرار دارد (چون از 0 شروع کرده‌ایم و شماره‌گذاری افراد معمولاً از 1 شروع می‌شود).  

پس نفر سوم در این دایره نجات می‌یابد.  
</p>
