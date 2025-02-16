from fastapi import FastAPI, Depends

#from .dashboard import dashboard_router
#from .groups import groups_router
#from .study_activities import study_activities_router
#from .study_sessions import study_sessions_router
#from .settings import settings_router
from app.words.technical.words_router import words_router

app = FastAPI(title="Lang Portal API")

# Include routers
#app.include_router(dashboard_router.router)
#app.include_router(groups_router.router)
#app.include_router(study_activities_router.router)
#app.include_router(study_sessions_router.router)
#app.include_router(settings_router.router) 
app.include_router(words_router) 

