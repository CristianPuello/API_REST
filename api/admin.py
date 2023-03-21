from django.contrib import admin
from  .models import  Jokes, Profile, JokeAssignment

class JokesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'joke', 'joker_type')
    search_fields= ['joke']
    list_filter = ['joker_type']
    actions = ['make_joke_black', 'make_joke_green']

    def make_joke_black(self, request, queryset):
        queryset.update(joker_type='BLACK')
    make_joke_black.short_description = "Cambiar chiste negro"

    def make_joke_green(self, request , queryset):
        queryset.update(joker_type='GREEN')
    make_joke_green.short_description = "Cambiar chiste verde"

admin.site.register(Jokes, JokesListAdmin)

class ProfileListAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
    search_fields= ['name', 'document']

admin.site.register(Profile, ProfileListAdmin)

class AssignmentListAdmin(admin.ModelAdmin):
    list_display = ('profile', 'joke')
    search_fields = ['profile__name', 'joke__joke']

admin.site.register(JokeAssignment, AssignmentListAdmin)

