from flask import Flask, render_template, request, redirect, session

from flask_app.models.user import User

app=Flask(__name__)
 app.secret_key="im a secret"