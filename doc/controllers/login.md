# Login

```python
login_controller = client.login
```

## Class Name

`LoginController`

## Methods

* [Locataire Login](../../doc/controllers/login.md#locataire-login)
* [Am Login](../../doc/controllers/login.md#am-login)
* [Admin Login](../../doc/controllers/login.md#admin-login)


# Locataire Login

```python
def locataire_login(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocataireLoginRequest`](../../doc/models/locataire-login-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = LocataireLoginRequest()
body.email = 'im_gouaouri@esi.dz'
body.password = 'password'

result = login_controller.locataire_login(body)
```


# Am Login

```python
def am_login(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocataireLoginRequest`](../../doc/models/locataire-login-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = LocataireLoginRequest()
body.email = 'ia_yalaoui@esi.dz'
body.password = 'resetreset'

result = login_controller.am_login(body)
```


# Admin Login

```python
def admin_login(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocataireLoginRequest`](../../doc/models/locataire-login-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = LocataireLoginRequest()
body.email = 'admin@nexcode.dz'
body.password = 'password'

result = login_controller.admin_login(body)
```

