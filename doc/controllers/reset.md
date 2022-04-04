# Reset

```python
reset_controller = client.reset
```

## Class Name

`ResetController`

## Methods

* [Forgot Password Locataire](../../doc/controllers/reset.md#forgot-password-locataire)
* [Reset Password Locataire](../../doc/controllers/reset.md#reset-password-locataire)
* [Forgot Password AM](../../doc/controllers/reset.md#forgot-password-am)
* [Reset Password AM](../../doc/controllers/reset.md#reset-password-am)


# Forgot Password Locataire

```python
def forgot_password_locataire(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteLocataireRequest`](../../doc/models/delete-locataire-request.md) | Body, Required | - |

## Response Type

[`ForgotPasswordLocataire`](../../doc/models/forgot-password-locataire.md)

## Example Usage

```python
body = DeleteLocataireRequest()
body.email = 'dou@esi.dz'

result = reset_controller.forgot_password_locataire(body)
```

## Example Response *(as JSON)*

```json
{
  "message": "password reset link sent to your email account"
}
```


# Reset Password Locataire

```python
def reset_password_locataire(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

[`ResetPasswordLocataire`](../../doc/models/reset-password-locataire.md)

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'resetreset'

result = reset_controller.reset_password_locataire(body)
```

## Example Response *(as JSON)*

```json
{
  "message": "password reset sucessfully."
}
```


# Forgot Password AM

```python
def forgot_password_am(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ForgotPasswordAMRequest`](../../doc/models/forgot-password-am-request.md) | Body, Required | - |

## Response Type

[`ForgotPasswordAM`](../../doc/models/forgot-password-am.md)

## Example Usage

```python
body = ForgotPasswordAMRequest()
body.email = 'id_bouloudene@esi.dz'

result = reset_controller.forgot_password_am(body)
```

## Example Response *(as JSON)*

```json
{
  "message": "password reset link sent to your email account",
  "success": true
}
```


# Reset Password AM

```python
def reset_password_am(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'resetreset'

result = reset_controller.reset_password_am(body)
```

