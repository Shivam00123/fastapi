module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "uvicorn",
      args: "main:app --host 0.0.0.0 --port 8000",
      interpreter: "python3",
      watch: false,
      env: {
        DATABASE_URL: "mysql+pymysql://userdb:Abcd0011@localhost:3306/mydb",
      },
    },
  ],
};
