from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def get_articles_by_date(db: Session, publication_date: date):
    return db.query(models.Article).filter(models.Article.published_at == publication_date).all()

def get_articles_by_category(db: Session, category: str):
    return db.query(models.Article).filter(models.Article.category == category).all()

def get_articles_sorted_by_date_latest(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).order_by(models.Article.published_at.desc()).offset(skip).limit(limit).all()

def get_articles_sorted_by_title_asc(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).order_by(models.Article.title.asc()).offset(skip).limit(limit).all()

def get_articles_by_language(db: Session, language: str, skip: int = 0, limit: int = 100):
    return db.query(models.Article).filter(models.Article.language == language).offset(skip).limit(limit).all()