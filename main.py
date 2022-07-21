from fastapi import FastAPI


api = FastAPI(title="Mon API pour les MAR22 CDE")

# GET /hello
# -> {"message": "hello!"}


@api.get(
    "/hello",
    tags=["hello", "world"],
    responses={
        200: {
            "description": "Tout va bien dans le meilleur des mondes!"
        }
    })
def get_hello():
    """Une fonction qui salue bien les gens qui utilisent cette API!

    Returns:
        dict: Message de salutations
    """
    return {
        "message": "hello"
    }


@api.get("/health")
def get_health():
    return {
        "status": 1
    }


@api.get("/")
def get_index():
    return {
        "message": "La documentation est disponible au /docs."
    }


@api.put("/bye")
def put_bye():
    return {
        "bye": "bye",
        "other": "ceci n'est pas testé c'est en plus mais ça pas"
    }
