from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def observation_not_found(request:Request, exec: Exception):
    return JSONResponse(
            status_code=404,
            content={"message": str(exec)}
        )

async def observation_status_error(request:Request, exec: Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exec)}
    )

async def observation_create_error(request:Request, exec:Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exec)}
    )