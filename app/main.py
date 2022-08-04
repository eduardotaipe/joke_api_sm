from app.api.app import init_app


app = init_app()

if __name__ == "__main__":
    from uvicorn import run

    run("app.main:app", reload=True)
