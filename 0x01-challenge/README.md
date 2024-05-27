# Fix my code

## [Task #1](./status_server)

### Issue

Route for the API status (`/status`)  does not work. Returns a 404 error.

```bash
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
```

### Cause

**Misconfigured route:**
The [`blueprint`](./status_server/api/v1/views/__init__.py) already has a url prefix, so specifying a full route in [`views`](./status_server/api/v1/views/index.py) would result in a route like `/api/v1/api/v1/status`

### Fix

Rewrite the `/status` route to account for the Blueprint's URL prefix.

## Task #3

### Issue

The script [user.py](./user.py) does not work.

```bash
Traceback (most recent call last):
  File "Fix_My_Code_Challenge/./user.py", line 6, in <module>
    class User():
  File "/Fix_My_Code_Challenge/./user.py", line 13, in User
    @email.setter
NameError: name 'email' is not defined. Did you mean: 'eval'?
```

### Cause

**Wrong declaration order:** Using the setter decorator before declaring the getter property.

### Fix

Changing the order of declaration, so that the getter property comes first.
