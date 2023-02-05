# weird-final
<div style="direction: rtl;">
  
# هیورستیک های استفاده شده
## MRV
سالنی که گروه های کمتری به امتحان دادن در آن علاقه مندند را برمیگرداند.
## LCV
برای سالن انتخاب شده، لیستی مرتب شده از گروه ها را برمیگرداند. این لیست به ترتیب میزان علاقه گروه ها به سالن ها همسایه مرتب شده است.
## الگوریتم های حل مسئله

### الگوریتم AC-3:
تمام ارک هارو با توجه به محدودیت ها میسازد و وارد یک صف میکند. سپس تا زمان خالی شدن صف هربار یک ارک را پاپ میکند و اگر برای هر مقدار ممکن از عنصر اول ارک هیج مقداری برای عنصر دوم ارک نبود که محدودیت هارا ارضا کند ان مقدار را از دامنه عنصر اول حذف میکند در غیر این صورت تغییری نمی دهد. اگر در پایان دامنه عنصر اول ارک تغییری کرده بود تمام ارک هایی که عناصر دومشان این عنصر است به صف اضافه میشوند. با پایان یافتن الگوریتم دامنه ممکن متغیر ها تا حد ممکن کاهش پیدا میکند و در نتیجه رسیدن به جواب سریع تر و آسان تر میشود.
پیچیدگی زمانی: O(e.d^3)
پیچیدگی فضایی: O(e) 
[e: تعداد ارک ها, d: طول بزرگترین دامنه]



</div>
<div style="direction: rtl;">




## تاریخچه کامیت ها:

</div>
<div >

```text
    {replace this line with output of: `git log --pretty="%h %aN '%s'"`}
