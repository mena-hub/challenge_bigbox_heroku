### Heroku
---
*Django a producción*

**¿Nos hace falta algo?**
- [Una cuenta](https://signup.heroku.com/login)
- El repositorio clonado
- Un entorno virtual
- Instalar requirements.txt

*Y también*

**ANOTACIONES**

**CLI commands**

```zsh
» heroku login
» heroku logout
```

Create

```zsh
» heroku create 
» heroku create <OPTIONAL_NAME>
```
Configuration and Config Vars

```zsh
» heroku config 
» heroku config:set <CONFIG_VAR>
```

<details>
<summary markdown="span">Ver</summary>

Por ejemplo

```zsh
» heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku
```
</details>

Postgres

```zsh
» heroku addons
» heroku addons:create heroku-postgresql:<PLAN_NAME>
```

**Material de consulta**

- [Documentación](https://devcenter.heroku.com/categories/reference)
- [Tutorial](https://www.youtube.com/watch?v=f6PVDxCB08A)

<details>
<summary markdown="span">Ver</summary>

*Uma pequena surpresa Ta-rán! Beleza...*

</details>

---
### Heroku Postgres
---

**Remote database**

```zsh
» heroku pg:psql
```

```zsh
--> Connecting to database

create <OPTIONAL_NAME>::DATABASE=> \d (n filas)(END) q
create <OPTIONAL_NAME>::DATABASE=> \d tablename
create <OPTIONAL_NAME>::DATABASE=> select * from tablename
```

**ANOTACIONES II**

Esto es un resumen, artículos específicos complementarios:

- Django Apps for Heroku
- Getting Started on Heroku with Python
- Deploying with Git

**LINK a la aplicación ya subida**: <a href="https://bigbox-production.herokuapp.com">herokuapp.com</a>

*AL MARGEN: Faltaría leer sobre django-environ.*

---
### Para cerrar
---

**¿Qué vamos a aprender?**

¡A desplegar nuestro proyecto en Heroku rápido y fácil!.

![Alt Text](https://i.imgur.com/dmet3rO.gif)

*Tá...*