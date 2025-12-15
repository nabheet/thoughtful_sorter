from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sorter import Sorter, SorterParametersError

app = FastAPI(
    title="Thoughtful Sorter API",
    description="API for sorting packages based on dimensions and mass",
    version="1.0.0",
)

sorter = Sorter()


class PackageRequest(BaseModel):
    width: float = Field(..., gt=0, description="Width in cm")
    height: float = Field(..., gt=0, description="Height in cm")
    length: float = Field(..., gt=0, description="Length in cm")
    mass: float = Field(..., gt=0, description="Mass in kg")


# {"width": 50.0, "height": 30.0, "length": 20.0, "mass": 10.0}


class SortResponse(BaseModel):
    category: str = Field(..., description="Category of the package")


@app.post("/sort", response_model=SortResponse)
async def sort_package(package: PackageRequest):
    """
    Sort a package based on its dimensions and mass.

    Returns one of: STANDARD, BULKY, HEAVY, or REJECTED
    """
    try:
        category = sorter.sort(
            width=package.width,
            height=package.height,
            length=package.length,
            mass=package.mass,
        )

        # volume = package.width * package.height * package.length

        return SortResponse(
            category=category,
        )
    except SorterParametersError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    return FileResponse("index.html")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
