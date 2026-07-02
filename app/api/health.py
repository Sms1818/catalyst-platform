from fastapi import APIRouter

health_router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)


@health_router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}
