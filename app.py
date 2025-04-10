from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from flask_cors import CORS
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError

from model import Session
from model.anime_list import AnimeList
from model.manga_list import MangaList
from model.anime_genres import AnimeGenres
from model.manga_genres import MangaGenres
from model.genres import Genres
from schemas.anime_list import AnimeListSchema, AnimeSchema, AnimeSearchSchema
from schemas.manga_list import MangaSchema, MangaListSchema, MangaSearchSchema

info = Info(title='AniMangaTracker', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

#definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
anime_list_tag = Tag(name="Lista de animes", description="Adicão, remoçao e edição de animes na lista do banco de dados")
manga_list_tag = Tag(name="Lista de mangas", description="Adicão, remoçao e edição de mangas na lista do banco de dados")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get("/anime_list", tags=[anime_list_tag],
         responses={200: AnimeListSchema})
def get_anime_list():
    """Busca e retorna os animes cadastrados pelo usuário na lista
    """
    session = Session()
    anime_list = session.query(AnimeList).all()

    return { "data": anime_list }, 200

@app.get("/anime", tags=[anime_list_tag],
         responses={200: AnimeSchema})
def get_anime(query: AnimeSearchSchema):
    """Busca um anime na lista do usuário através do id
    """

    session = Session()
    anime = session.query(AnimeList).filter(AnimeList.id == query.id).first()

    return { "data": {
        "id": anime.id,
        "title_romaji": anime.title_romaji,
        "title_native": anime.title_native,
        "title_english": anime.title_english,
        "description": anime.description,
        "cover_image_medium": anime.cover_image_medium,
        "cover_image_large": anime.cover_image_large,
        "start_date": anime.start_date,
        "end_date": anime.end_date,
        "status": anime.status,
        "season": anime.season,
        "episodes": anime.episodes,
        "rating": anime.rating,
        "user_status": anime.user_status,
        "is_favorite": anime.is_favorite,
        "genres": anime.genres,
    }}, 200 

@app.post("/anime", tags=[anime_list_tag])
def add_anime(form: AnimeSchema):
    """Adiciona um anime na lista do usuário
    """

    anime = AnimeList(
        id = form.id,
        title_romaji= form.title_romaji,
        title_native=form.title_native,
        title_english=form.title_english,
        description=form.description,
        cover_image_medium=form.cover_image_medium,
        cover_image_large=form.cover_image_large,
        start_date=form.start_date,
        season= form.season,
        end_date=form.end_date,
        status=form.status,
        episodes=form.episodes,
        rating=form.rating,
        user_status=form.user_status,
        is_favorite=form.is_favorite,
    )
    try:
        session = Session()

        session.add(anime)

        for genre in form.genres:
            added_genre = {}
            if (session.query(Genres).filter(Genres.name == genre).first()) is None:
                new_genre = Genres(
                    name = genre 
                )

                session.add(new_genre)                
                session.commit()

                session.refresh(new_genre)

                added_genre = new_genre
            else:
                added_genre = session.query(Genres).filter(Genres.name == genre).first()

            session.execute(AnimeGenres.insert().values(
                anime_id=form.id,
                genres_id=added_genre.id,
            ))

        session.commit()

    except IntegrityError as e:
        error_msg = "O anime já existe na lista"
        return { "message": error_msg }, 409
    
    except Exception as e:
        error_msg = "Ocorreu um erro e não foi possível adicionar o anime"
        return { "message": error_msg }, 400

    return { "message": "O anime foi adicionado com sucesso"}, 200

@app.put("/anime", tags=[anime_list_tag],)
def edit_anime(form: AnimeSchema):
    """Altera um anime na lista do usuário
    """

    try:
        session = Session()
       
        session.execute(update(AnimeList).where(AnimeList.id == form.id).values(
            title_romaji= form.title_romaji,
            title_native=form.title_native,
            title_english=form.title_english,
            description=form.description,
            cover_image_medium=form.cover_image_medium,
            cover_image_large=form.cover_image_large,
            start_date=form.start_date,
            season= form.season,
            end_date=form.end_date,
            status=form.status,
            episodes=form.episodes,
            rating=form.rating,
            user_status=form.user_status,
            is_favorite=form.is_favorite,
        ))

        session.execute(delete(AnimeGenres).where(AnimeGenres.c.anime_id == form.id))

        for genre in form.genres:
            anime_genre = session.query(Genres).filter(Genres.name == genre).first()

            session.execute(AnimeGenres.insert().values(
                anime_id=form.id,
                genres_id=anime_genre.id,
            ))
                
        session.commit()
    
    except Exception as e:
        error_msg = "Ocorreu um erro e não foi possível atualizar o anime"
        return { "message": error_msg }, 400

    return { "message": "Anime foi atualizado com sucesso" }, 200

@app.delete("/anime", tags=[anime_list_tag])
def delete_anime(query: AnimeSearchSchema):
    """Exclui um anime da lista do usuário baseado na id
    """
    session = Session()

    session.execute(delete(AnimeGenres).where(AnimeGenres.c.anime_id == query.id))

    response = session.query(AnimeList).filter_by(id = query.id).delete()

    session.commit()

    if response:
        return { "message": "Anime removido da lista com sucesso" }, 200
    else:
        return { "message": "Ocorreu um erro e não foi possível remover o anime da lista" }, 400

@app.get("/manga_list", tags=[manga_list_tag],
         responses={200: MangaListSchema})
def get_manga_list():
    """Busca e retorna os mangás cadastrados pelo usuário na lista
    """
    session = Session()
    manga_list = session.query(MangaList).all()

    return { "data": manga_list }, 200

@app.get("/manga", tags=[manga_list_tag],
         responses={200: MangaSchema})
def get_manga(query: MangaSearchSchema):
    """Busca um mangá na lista do usuário através do id
    """

    session = Session()
    manga = session.query(MangaList).filter(MangaList.id == query.id).first()

    return { "data": {
        "id": manga.id,
        "title_romaji": manga.title_romaji,
        "title_native": manga.title_native,
        "title_english": manga.title_english,
        "description": manga.description,
        "cover_image_medium": manga.cover_image_medium,
        "cover_image_large": manga.cover_image_large,
        "start_date": manga.start_date,
        "end_date": manga.end_date,
        "status": manga.status,
        "volumes": manga.volumes,
        "chapters": manga.chapters,
        "story": manga.story,
        "art":manga.art,
        "rating": manga.rating,
        "user_status": manga.user_status,
        "is_favorite": manga.is_favorite,
        "genres": manga.genres,
    }}, 200

@app.post("/manga", tags=[manga_list_tag])
def add_manga(form: MangaSchema):
    """Adiciona um mangá na lista do usuário
    """
    manga = MangaList(
        id = form.id,
        title_romaji= form.title_romaji,
        title_native=form.title_native,
        title_english=form.title_english,
        description=form.description,
        cover_image_medium=form.cover_image_medium,
        cover_image_large=form.cover_image_large,
        start_date=form.start_date,
        end_date=form.end_date,
        status=form.status,
        volumes=form.volumes,
        chapters=form.chapters,
        story=form.story,
        art=form.art,
        rating=form.rating,
        user_status=form.user_status,
        is_favorite=form.is_favorite,
    )
    try:
        session = Session()

        session.add(manga)

        for genre in form.genres:
            added_genre = {}
            if (session.query(Genres).filter(Genres.name == genre).first()) is None:
                new_genre = Genres(
                    name = genre 
                )

                session.add(new_genre)                
                session.commit()

                session.refresh(new_genre)

                added_genre = new_genre
            else:
                added_genre = session.query(Genres).filter(Genres.name == genre).first()

            session.execute(MangaGenres.insert().values(
                manga_id=form.id,
                genres_id=added_genre.id,
            ))

        session.commit()

    except IntegrityError as e:
        error_msg = "O mangá já existe na lista"
        return { "message": error_msg }, 409
    
    except Exception as e:
        error_msg = "Ocorreu um erro e não foi possível adicionar o mangá"
        return { "message": error_msg }, 400

    return { "message": "O mangá foi adicionado com sucesso"}, 200

@app.put("/manga", tags=[manga_list_tag],)
def edit_manga(form: MangaSchema):
    """Altera um mangá na lista do usuário
    """
    try:
        session = Session()
       
        session.execute(update(MangaList).where(MangaList.id == form.id).values(
            title_romaji= form.title_romaji,
            title_native=form.title_native,
            title_english=form.title_english,
            description=form.description,
            cover_image_medium=form.cover_image_medium,
            cover_image_large=form.cover_image_large,
            start_date=form.start_date,
            end_date=form.end_date,
            status=form.status,
            volumes=form.volumes,
            chapters=form.chapters,
            story=form.story,
            art=form.art,
            rating=form.rating,
            user_status=form.user_status,
            is_favorite=form.is_favorite,
        ))

        session.execute(delete(MangaGenres).where(MangaGenres.c.manga_id == form.id))

        for genre in form.genres:
            manga_genre = session.query(Genres).filter(Genres.name == genre).first()

            session.execute(MangaGenres.insert().values(
                manga_id=form.id,
                genres_id=manga_genre.id,
            ))
                
        session.commit()
    
    except Exception as e:
        error_msg = "Ocorreu um erro e não foi possível atualizar o mangá"
        return { "message": error_msg }, 400

    return { "message": "Mangá foi atualizado com sucesso" }, 200

@app.delete("/manga", tags=[manga_list_tag])
def delete_manga(query: MangaSearchSchema):
    """Exclui um mangá da lista do usuário baseado na id
    """
    session = Session()

    session.execute(delete(MangaGenres).where(MangaGenres.c.manga_id == query.id))

    response = session.query(MangaList).filter_by(id = query.id).delete()

    session.commit()

    if response:
        return { "message": "Mangá removido da lista com sucesso" }, 200
    else:
        return { "message": "Ocorreu um erro e não foi possível remover o mangá da lista" }, 400