from pydantic import BaseModel
from typing import List

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True

class ReplyBase(BaseModel):
    content: str

class ReplyCreate(ReplyBase):
    pass

class Reply(ReplyBase):
    id: int
    comment_id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    comments: List[Comment] = []

    class Config:
        orm_mode = True
