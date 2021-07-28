# Music Catalog Application - Django 

## PT

### Aplicação Web que faz uso da API Discogs https://github.com/joalla/discogs_client para recuperar dados da database do website Discogs https://www.discogs.com/ 

#### Após se cadastrar e fazer login na aplicação o usuário pode pesquisar um álbum e artista para adicionar ao seu catálogo. Se a consulta a database do Discogs for bem sucedida este álbum e suas informações são adicionados ao catálogo. 
#### O usuário tem a opção de fazer pesquisas avançadas e simples no seu catálogo e pode ver estatísticas do mesmo. Além disso o usuário pode entrar na página de detalhes de um álbum específico onde ele pode fazer edições.

### Vídeo da aplicação funcionando: <a href="https://drive.google.com/file/d/1LgL-jb4u6ruktaknNxZgkJwhrvV5vEHR/view?usp=sharing" target="_blank">MusicCatalog</a>

### Detalhes

- Apps: albums,users
- Database Postgres
- Foram realizados testes automatizados no app albums
- O foco do projeto é Backend entretanto para tornar o visual mais agradável foi usado Bootstrap. 
- Veja requirements.txt para mais detalhes quanto aos pacotes utilizados

### Execução

0 - Clonar repositorio
```
git clone git@github.com:JonatasLemos/MusicCatalogApplication.git
```
1 - Instalar requerimentos num ambiente virtual
```
pip install -r requirements.txt
```
2 - Criar SECRET_KEY http://www.miniwebtool.com/django-secret-key-generator/
```
export SECRET_KEY='<secret_key>'
```
3 - Fazer migrações para database Postgres
```
python manage.py makemigrations
python manage.py migrate
```
4 - Subir servidor de desenvolvimento
```
python manage.py runserver
```

## EN

### Web application that makes use of the Discogs API https://github.com/joalla/discogs_client to retrieve data from the Discogs website database https://www.discogs.com/

#### After registering and logging into the application, the user can search for an album and artist to add to their catalog. If the Discogs database query is successful this album and its information are added to the catalog.
#### The user has the option to carry out advanced and simple searches in his catalog and can see its Statistics. The user can also enter the details page of a specific album where he can make editions.

### Application video: <a href="https://drive.google.com/file/d/1LgL-jb4u6ruktaknNxZgkJwhrvV5vEHR/view?usp=sharing" target="_blank">MusicCatalog</a>

### Details

- Apps: albums,users
- Postgres database
- Automated tests were performed in the albums app
- The focus of the project is Backend however to make the look more pleasant Bootstrap was used.
- See requirements.txt for more details on packages used


## Author/Autor: Jônatas Oliveira Lemos


