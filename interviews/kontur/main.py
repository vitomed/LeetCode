"""
Реализуйте web-приложение, которое состоит из двух страниц: / и /news/{id}.

Для запуска проекта выберите в PyCharm конфигурацию start.
Для тестов выберите в PyCharm конфигурацию tests.
Все необходимые файлы находятся в папке с проектом.
"""
import json
from datetime import datetime

from flask import Flask, jsonify, abort
from typing import Tuple, List, Dict, Any, Optional

SOURCE_NEWS = "news.json"
SOURCE_COMMENTS = "comments.json"

app = Flask(__name__)


def loader() -> Tuple[dict, dict]:
    """
    Функция считывает данные из файлов и преобразует их в dict.
    Функция не должна нарушать изначальную структуру данных.
    Логика фильтрации и сортировки должна быть реализована в функциях 
    get_list и get_item.
    """
    with open(SOURCE_NEWS) as news_file:
        source_news = json.load(news_file)
    with open(SOURCE_COMMENTS) as comments_file:
        source_comments = json.load(comments_file)
    return source_news, source_comments


@app.route("/")
def get_list():
    """
    На странице / вывести json в котором каждый элемент - это:
    - неудалённая новость из списка новостей из файла news.json.
    - для каждой новости указано кол-во комментариев этой новости из файла comments.json
    - для каждой новости указана дата и время последнего (самого свежего) комментария

    В списке новостей должны отсутствовать новости, дата публикации которых ещё не наступила.
    Даты в файле хранятся в формате ISO 8601(%Y-%m-%dT%H:%M:%S) и должны отдаваться в том же формате.

    Формат ответа:
    news: [
        {
            id: <int>,
            author:	<str>,
            publishedAt: <str>,
            image:	<str>,
            teaser: <str>,
            isDeleted: <bool>,
            lastComment: <str>,
            commentsCount: <int>
        }
    ],
    totalResults: <int>
    """
    news, comments = loader()

    def filter_news(news_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        filtered_news = []
        for news_item in news_data["news"]:
            if not news_item["isDeleted"] and datetime.now() > datetime.fromisoformat(news_item["publishedAt"]):
                filtered_news.append(news_item)
        return filtered_news

    def get_comments_count(news_id: int, comments_data: Dict[str, Any]) -> int:
        comments = [comment for comment in comments_data["comments"] if comment["newsId"] == news_id]
        return len(comments)

    def get_last_comment_date(news_id: int, comments_data: Dict[str, Any]) -> Optional[str]:
        comments = [comment for comment in comments_data["comments"] if comment["newsId"] == news_id]
        if comments:
            last_comment = max(comments, key=lambda comment: comment["publishedAt"])
            return last_comment["publishedAt"]
        return None

    def sort_news_by_published_at(news: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(news, key=lambda news_item: news_item["publishedAt"], reverse=True)

    def format_news(news: List[Dict[str, Any]]) -> Dict[str, Any]:
        formatted_news = []
        for news_item in news:
            comments_count = get_comments_count(news_item["id"], comments)
            last_comment_date = get_last_comment_date(news_item["id"], comments)

            formatted_news.append({
                "id": news_item["id"],
                "author": news_item["author"],
                "publishedAt": news_item["publishedAt"],
                "image": news_item["image"],
                "teaser": news_item["teaser"],
                "isDeleted": news_item["isDeleted"],
                "lastComment": last_comment_date,
                "commentsCount": comments_count
            })

        return {
            "news": formatted_news,
            "totalResults": len(formatted_news)
        }

    filtered_news = filter_news(news)
    sorted_news = sort_news_by_published_at(filtered_news)
    formatted_news = format_news(sorted_news)

    return jsonify(formatted_news)


@app.route("/news/<int:news_id>")
def get_item(news_id):
    """
    На странице /news/{id} вывести json, который должен содержать:
    - новость с указанным в ссылке id
    - список всех комментариев к новости, отсортированных по времени создания, от самого свежего к самому старому

    Для следующих случаев нужно отдавать ошибку abort(404):
    - попытка получить новость не из списка
    - попытка получить удалённую новость
    - попытка получить новость с датой публикации из будущего


    Формат ответа:
    id: <int>,
    author:	<str>,
    publishedAt: <str>,
    image:	<str>,
    teaser: <str>,
    content: <str>,
    isDeleted: <bool>,
    comments: [
        user: <str>,
        newsId: <int>,
        comment: <str>,
        publishedAt: <str>
    ]
    """
    news, comments = loader()

    def get_news_by_id(news_id: int, news_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        for news_item in news_data["news"]:
            if news_item["id"] == news_id:
                if news_item["isDeleted"] or datetime.now() < datetime.fromisoformat(news_item["publishedAt"]):
                    return None
                return news_item
        return None

    def get_comments_by_news_id(news_id: int, comments_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        comments = [comment for comment in comments_data["comments"] if comment["newsId"] == news_id]
        sorted_comments = sorted(comments, key=lambda comment: comment["publishedAt"], reverse=True)
        return sorted_comments

    def format_comment(comment: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "user": comment["user"],
            "newsId": comment["newsId"],
            "comment": comment["comment"],
            "publishedAt": comment["publishedAt"]
        }

    def format_news(news_item: Dict[str, Any], formatted_comments: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "id": news_item["id"],
            "author": news_item["author"],
            "publishedAt": news_item["publishedAt"],
            "image": news_item["image"],
            "teaser": news_item["teaser"],
            "content": news_item["content"],
            "isDeleted": news_item["isDeleted"],
            "comments": formatted_comments
        }

    news_item = get_news_by_id(news_id, news)
    if news_item is None:
        abort(404)

    news_comments = get_comments_by_news_id(news_id, comments)
    formatted_comments = [format_comment(comment) for comment in news_comments]
    formatted_news = format_news(news_item, formatted_comments)

    return jsonify(formatted_news)
