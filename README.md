# Replicator
![](Replicator.png)
 
Репликатор - это приложение, которое позволит копировать FBD блоки в среде разработки Unimod c автоматической заменой тегов и комментариев.
 
Это приложение поможет вам тратить меньше времени на создание проектов в среде Unimod. Replicator эмулирует ввод с вашей клавиатуры и мыши, поэтому он очень требователен к вашему разрешению и скейлингу экрана в параметрах персонализации. Так что для того, чтобы это приложение работало корректно, внимательно прочтите инструкцию перед запуском.

## Инструкция

Репликатор копирует FBD блоки с автоматической заменой тегов или чаcтей тегов, так же коментариев.

Важно, что бы параметры вашей персонализации экрана были аналогичными: 

![](/img/Picture1.png)

Теперь идем в диск С, создаем там папку Replicator, а в этой папке текстовый файлик damp и damp2, соблюдаем регистры, не надо писать «.txt» в конце имени файла, это важно

![](/img/Picture2.png)

В damp пихаем теги построчечно, по задумке, можно будет из таблицы подключений целый модуль вставить просто, естественно, каждая из этих строчек будет использованна для автозамены. Предпологается, что тут будут перечисленны полные теги без дискрипторов, то есть та часть имени переменной, которая идет до |IVXX

В damp2 складываем комментарии к этим тегам в том же порядке, что и сами теги.

![](/img/Picture3.png)![](/img/Picture4.png)

Все, сохраняем, зкрываем

Открываем UMPro на весь экран и не трогам расположение элементов в окне.

![](/img/Picture5.png)

Открываем проект

Мы открываем вкладки, как на картинке ниже, в том же порядке. RRS(можно назвать как хочется) будет программой, куда будут скидываться готовые блоки, TEST(тоже можно назвать как хочется) – это чисто буфферная подпрограмма, в которой будет происходить автозамена.

![](/img/Picture6.png)

Первый блок необходимо создать самостоятельно, оставить его в SSR.
!!!Коментарий нужно писать используя _ вмето пробела!!!
Удостоверьтесь, что в меню автозамены нет двух слов написанных через пробел
В TEST копируем блок из SSR

![](/img/Picture7.png)

Запускаем Replicator. 

![](/img/Picture8.png)

В верхнюю строчку пишем тег или его часть, которую будем заменять автозаменой.
В нижнюю часть пишем комментарий, который будем заменять

Перед тем, как подтвердить пуск репликатора удостоверьтесь, что ничего, включая окно приложения не загораживает пятую вкладку в UMPro, в нашем примере это вкладка ![](/img/Picture9.png)

Скрипт остановится сам, когда переберет все строчки в файлике damp. Последнюю обработает два раза, я уже знаю почему, но выличить пока не успел.
Если что-то пошло не так и репликатор необходимо остановить досрочно, зажимаем и держим RShift до тех пор, пока он не остановится.

!!!ВНИМАНИЕ!!!
1)	Ненадо пытаться осуществить никакой ввод с компьютера, на котором работает репликатор, пока репликатор не остановаится. 
2)	У UM есть некоторые проблемы с кодированием кириллицы, поэтому перед тем, как нажать на кнопку пуска репликатора убедитесь, что вы русской раскладке! ![](/img/Picture10.png)

Скачать .exe: https://drive.google.com/drive/folders/1ZoXmk9Yk8iEm-d7qSyLL8qykDq6COHOi?usp=share_link
