# Web Development
## Web Servers / WGSI
### [Gunicorn](https://gunicorn.org/)
#### FAQs
##### How do I include access logs?
By default, Gunicorn won't output anything but the log statements from within the application (and of those, only the ones matching the particular log level). In a regular setup, your access logs will be sitting in an `access_log file, maintained by Apache or nginx. If you want to output those in the standard log output of Gunicorn too (stdout by default), you should explicitly configure Gunicorn to do so:[^access]

``` bash hl_lines="4 5"
gunicorn \
 --bind 0.0.0.0:8080 \
 --workers 4 \
 --access-logformat '%(t)s %(p)s %(h)s %(m)s %(U)s %(s)s - %(L)ss' \
 --access-logfile - \
my_app.wsgi:app
```

**NOTE:** Make sure that you are also usign the right output. In my example, `--access-logfile -` means, use `stdout`

[^access]: [Access log format | Gunicorn Docs](https://docs.gunicorn.org/en/latest/settings.html#access-log-format)
