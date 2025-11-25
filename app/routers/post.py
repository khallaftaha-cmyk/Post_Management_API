from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from .. import models, schemas
from ..database import get_db
from . import oauth2


router = APIRouter(
    tags = ['Posts']
)

@router.get("/sqlalchemy")
def get_posts(db: Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()

    return posts


@router.get("/posts", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    #return{"data": my_posts}
    #cursor.execute("""select * from posts""" )
    #posts = cursor.fetchall()
    # #posts = db.query(models.Post)
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).all()
    

    return posts


@router.post("/posts",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    
    #post_dict = post.dict()
    #post_dict['id'] = randrange(0,10000)
    #my_posts.append(post_dict)
    #return{"data": post_dict}
    
    #cursor.execute("""insert into posts (title, content) values (%s,%s) returning * """,
                  #(post.title, post.content))
    #new_post = cursor.fetchone()
    #conn.commit()

    new_post= models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/posts/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    #post = find_posts(id)

    #cursor.execute("""select * from posts where id=%s """, (str(id),))
    #post = cursor.fetchone()

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"the post with the id:{id} was no found")

    return post
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return("message":"the post with the id:{id} was no found") 
    #return{"post-detail" : post }

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    #index=find_index(id)
    
    #cursor.execute("""delete from posts where id=%s returning *""", (str(id),) )
    #deleted_post = cursor.fetchone()
    #conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id does not exist')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="not authorized to perform this action")
    post_query.delete(synchronize_session=False)
    db.commit()
    #my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}", response_model=schemas.Post)
def update_post(id:int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    #index=find_index(id)

    #cursor.execute("""update posts set title=%s, content=%s where id=%s returning * """ ,
                   #(post.title, post.content, str(id)))
    #post = cursor.fetchone()
    #conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id does not exist')
    post_query.update( updated_post.dict(), synchronize_session=False)
    db.commit()

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="not authorized to perform this action")
    
    #post_dict = post.dict()
    #post_dict['id'] = id
    #my_posts[index] = post_dict
    #print(post)
    
    return post_query.first()