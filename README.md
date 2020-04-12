## ArticleAggregator

Агрегатор контента, т.е веб-приложение, осуществляющее индивидуальный подбор научно-полулярных статей 
в зависимости от тематических категорий, которые выбирает пользователь.


### Описание

**Пользователь имеет возможность:**

1. Подписаться на рассылку статей по нескольким выбранным категориям 
2. Просматривать на главной странице новости *(статьи по подпискам)*
3. Определять желаемое количество статей в день, которое будет помещаться на главную страницу *(1/2/3)*
4. В отдельном блоке просматривать статьи покатегориям, на которые нет подписки
*(Перенаправление на станицу с выбранной категирией)*
5. Осуществлять поиск среди уже имеющегося контента в новостной ленте 
6. Изменять настройки аккаунта в личном кабинете

**Реализация**

Подбор контента осуществляется из нескольких достоверных источников(в частности - портала Naked Science), 
вся необходимая информация помещается в базу данных, в которой содержатся статьи, имеющие определяющий тег.
Статьи отображаютя на странице пользователя в заданном количестве и в соответствии с заданными категориями. 
Написано на Python с использованием Django.

**Как это на самом деле выглядит**

Будет реализован пользовательский интерфейс. Будет реализована регистрация и личный кабинет.
При регистрации будет возможность подписаться на определенные категории.
В личном кабинете будет функция отписки и подписки на другие категории статей. 
На главной странице будут отображаться ваши новости (статьи по подпискам), 
а также будет блок «Вам могло бы быть интересно» с категориями, на которые пользователь не подписан.
При выборе одной из таких категорий, пользователя будет перенаправлять на страницу с статьями, 
отсортированными только по выбранному тегу. Возможно, будет реализован поиск среди уже имеющегося контента
в новостной ленте пользователя.



