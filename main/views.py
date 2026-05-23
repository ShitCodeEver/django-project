from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import News, Projects

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Главная',
            'theme' : {
                'one': 'Мы специалисты в области архитектуры',
                'two': 'Дизайн, в котором вы почувствуете себя дома',
                'three' : 'Готовы построить дом вашей мечты'
            },
            'text': {
                'one': 'Мы специалисты в своей области и готовы воплотить ваши идеи в жизнь',
                'two': 'Создаем уютные и функциональные пространства, отражающие вашу индивидуальность',
                'three' : 'Начните путь к идеальному жилью вместе с нашей командой профессионалов'
            }            
        }
        return context
    
class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'О нас',
            'theme' : 'О нас',
            'text': 'Здесь вы сможете узнать о нас', 
        }
        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Контакты',
            'theme' :'Наш контакты',
            'text': 'здесь вы сможете отправить нам свое письмо',
        }
        return context

class ProjectView(TemplateView):
    template_name = 'service.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Проекты',
            
        }
        return context

class ServicesView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Сервис',
        }
        return context
    
class BlogView(ListView):
    template_name = 'main/blog.html'
    model = News
    context_object_name = 'News'
    paginate_by = 8 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Блог',
            'theme' :'Наш Блог',
            'text': 'Здесь вы сможете прочитать новости',
        }
        return context
    
class ErrorView(TemplateView):
    template_name = 'error.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Ошибка',
        }
        return context
# Create your views here.
