import uvicorn

def main():
   uvicorn.run(
      app_dir='app',
      app="main:app",
      host="0.0.0.0",
      port=8000,
      reload=True,
   )

if __name__ == "__main__":
   main()
