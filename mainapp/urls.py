from django.urls import path
from mainapp.views import user_list, user_list2, add_user, user_update, user_delete, get_fruit_all, find_fruit, \
    find_store, all_store, count_fruit, login, loginHandler, find_nut, loginout, FruitCart, UserRegister, Add_Fruit, \
    success, pages

app_name = 'mainapp'

urlpatterns = [
    path('list/', user_list),
    path('list2/', user_list2),
    path('add/', add_user),
    path('update/', user_update),
    path('delete/', user_delete),
    path('fruits/', get_fruit_all),
    path('find',find_fruit,name='find'),
    path('store',find_store),
    path('store_all',all_store),
    path('count',count_fruit),
    path('login',login,name='login'),
    path('loging',loginHandler),
    path('f_nut',find_nut,name='f_nut'),
    path('loginout',loginout),
    path('cart',FruitCart,name='cart'),
    path('regis',UserRegister,name='regis'),
    path('add_fruit',Add_Fruit,name='add_fruit'),
    path('success',success,name='success'),
    path('pages',pages,name='pages'),
]
