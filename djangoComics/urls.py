from django.contrib import admin
from django.urls import path
from superheroes.views import character_views
from superheroes.views import universe_views
from superheroes.views import user_view
from superheroes.views import power_view
from superheroes.views import power_character_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('UniverseComics', character_views.listPrincipal, name="UniverseComics"),
    path('login', user_view.loginView, name="login"),
    path('logout', user_view.logout_v, name="logout"),
    path('character', character_views.list, name="characters"),
    path('characters/detail/<int:id>', character_views.detail, name="characters_detail"),
    path('characters/update/<int:id>', character_views.update, name="update_character"),
    path('characters/create', character_views.create, name="form_character"),
    path('characters/search', character_views.search, name="search_character"),
    path('characters/search_universe', character_views.search_universe, name="search_character_universe"),
    path('characters/search_power', character_views.search_power, name="search_character_power"),
    path('characters/delete/<int:id>', character_views.delete, name="delete_character"),
    path('universes', universe_views.list, name="universes"),
    path('universes/detail/<int:id>', universe_views.detail, name="universe_detail"),
    path('universes/update/<int:id>', universe_views.update, name="update_universe"),
    path('universes/create', universe_views.create, name="form_universe"),
    path('universe/delete/<int:id>', universe_views.delete, name="delete_universe"),
    path('powers', power_view.list, name="powers"),
    path('powers/update/<int:id>', power_view.update, name="update_power"),
    path('powers/delete/<int:id>', power_view.delete, name="delete_power"),
    path('powers/create', power_view.create, name="form_power"),
    path('power_character/create', power_character_view.create, name="form_power_character"),
    path('power_character/update/<int:id>', power_character_view.update, name="update_power_character"),
    path('power_character/delete/<int:id>', power_character_view.delete, name="delete_power_character"),

    # path('characters/form_save',character_views.form_save,name="form_character"),
    # path('characters/save',character_views.save, name="save_character"),

]
