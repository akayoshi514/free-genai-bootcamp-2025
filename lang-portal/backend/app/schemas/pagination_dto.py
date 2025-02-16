from pydantic import BaseModel

class Pagination(BaseModel):
    current_page: int
    total_pages: int
    total_items: int
    items_per_page: int 